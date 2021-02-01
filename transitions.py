import json
import re
import requests
from functools import reduce


# get the top 50
BASE_URL = "https://stats.data.gouv.fr/"
params = {
    "module": "API",
    "method": "Actions.getPageUrls",
    "idSite": "109",
    "period": "month",
    "date": "yesterday",
    "format": "json",
    "filter_limit": "50",
    "flat": "1",
    "filter_pattern": "^https://www.data.gouv.fr/fr/datasets/.*\W",
    "filter_column": "url",
}

r = requests.get(BASE_URL, params=params)
data = r.json()

# make unique by slug
# TODO: deduplicate id/slug or remove slugs
unique_slugs = []
unique_data = []
for d in data:
    slug = d["url"].split("/")[5]
    if slug not in unique_slugs:
        unique_slugs.append(slug)
        unique_data.append((slug, d))


# get transitions for those
results = []

for idx, (slug, d) in enumerate(unique_data):
    print(f"Processing {slug} ({idx + 1}/{len(unique_data)})...")
    result = {}

    params = {
        "module":"API",
        "method":"Transitions.getTransitionsForPageUrl",
        "pageUrl": d["url"],
        "idSite":109,
        "period":"month",
        "date":"yesterday",
        "format":"json",
        "limitBeforeGrouping":10,
    }
    r = requests.get(BASE_URL, params=params)
    data = r.json()

    result["id"] = slug
    result["recommendations"] = []

    max_score_ds = 0
    max_score_re = 0
    for d in data["followingPages"]:
        # max_score is supposed to be the first one
        if re.match("data.gouv.fr/fr/datasets/\w+", d["label"]):
            max_score_ds = max_score_ds if max_score_ds else d["referrals"]
            score = round(d["referrals"] / max_score_ds * 100)
            result["recommendations"].append({
                "id": d["label"].split("/")[3],
                "type": "dataset",
                "score": int(score),
            })
        elif re.match("data.gouv.fr/fr/reuses/\w+", d["label"]):
            max_score_re = max_score_re if max_score_re else d["referrals"]
            score = round(d["referrals"] / max_score_re * 100) / 2
            result["recommendations"].append({
                "id": d["label"].split("/")[3],
                "type": "reuse",
                "score": int(score),
            })

    if result["recommendations"]:
        results.append(result)

with open("prod/recommendations.json", "w") as outfile:
    outfile.write(json.dumps(results))
