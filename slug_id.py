import json
from tqdm import tqdm

data = {}

for l in tqdm(open('datasets.slug.json', 'r').readlines()):
    j = json.loads(l)

    data[j['slug']]  = j['_id']['$oid']

json.dump(data, open('slug_id.json', 'w'))
