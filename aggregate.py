import glob
import json
import re

regex_datasets = r'^https?://www\.data\.gouv\.fr/(?:fr|en|es)/datasets/([a-z\-0-9]+)/$'
detect = re.compile(regex_datasets)

# agregate logs to co-visits
def ag_visits(log):
    data = json.load(open(log, 'r'))

    # print(data)

    visits = [ visit['actionDetails'] for visit in data ]
    print(len(visits))
    
    actions = [ [ action['url'] for action in actions if action['type'] == "action" ] for actions in visits ]
    
    # deduplicate
    actions = [ list(set(a)) for a in actions ]

    # keep only datasets
    actions = [ [ url for url in urls if detect.match(url) ] for urls in actions ]

    # remove visits without at least 2 datasets visits
    return [ urls for urls in actions if len(urls) > 1 ]

def write_visits(log, visits):
    name = log.replace('logs/', '')

    with open('visits/'+name, 'w') as f:
        json.dump(visits, f, sort_keys=True, indent=4, separators=(',', ': ')) 

logs = glob.glob('logs/*')

for log in logs:
    visits = ag_visits(log)
    write_visits(log, visits)    

