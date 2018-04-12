import glob
import json
import re
from tqdm import tqdm

from collections import Counter

regex_datasets = r'^https?://www\.data\.gouv\.fr/(?:fr|en|es)/datasets/([a-z\-0-9]+)/$'
detect = re.compile(regex_datasets)

def top50(logs):
    hits = []

    for log in tqdm(logs):
        # print(log)
        visits = json.load(open(log, 'r'))
        hits += [ action['url'].split('/')[-2] for visit in visits for action in visit['actionDetails'] if action['type'] == 'action' and detect.match(action['url']) ]
        #print(hits)

    return Counter(hits).most_common(50)

logs = glob.glob('logs/*.json') 
json.dump(top50(logs), open('top50.json', 'w'), indent=4, separators=(',', ': '))
