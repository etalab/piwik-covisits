import networkx as nx
from tqdm import tqdm

import json

def clean_label(g):
    g = nx.relabel_nodes(g, { n :  n.split('/')[-2] for n in g })

    return g

slug_id = json.load(open('slug_id.json', 'r'))

def mapping_slug_id(slug):
    return slug_id[slug] if slug in slug_id.keys() else slug

def rule_of_thumb(mylist): 
    '''Compute rule of thumb on a list
    eg: [100, 80, 20, 14, 12, 11, 1]  => [100, 80] (return the index where to cut)


    mylist = [100, 80, 20, 14, 12, 11, 1]
    mylist[:rule_of_thumb(mylist)]
    '''
    if len(mylist) > 1:
                # list of drops
        difflist = [mylist[el] - mylist[1:][el] for el in range(0, len(mylist) - 1)]
        max_drop = max(difflist)

        # index of maximum(s)
        max_drop_index = max([i for i, j in enumerate(difflist) if j == max(difflist)])

        return max_drop_index + 1

    return mylist[0]

top50 = json.load(open('top50.json','r'))

g = nx.read_gexf('covisits.gexf')
g = clean_label(g)

for n in tqdm(list(g)):
    print()
    print(n)

    # print([ edge for edge in g[n] ])

    edges = sorted(g[n], key=lambda e: -g[n][e]['covisits'])
    
    # keep only top 10
    edges = edges[:10]

    # reduce with rule of thumb
    edges = edges[:rule_of_thumb([ g[n][n2]['covisits'] for n2 in edges ])]
    
    for n2 in edges:
        print("    " + n2 + " - "+ str(g[n][n2]['covisits']))

    data = {
        "id": n,
        "recommendations": [ { "id": n2, "score": g[n][n2]['covisits'] } for n2 in edges ]
    }

    # json.dump(data, open('scores/'+n+".json", "w"), indent=4, separators=(',', ': '))

top50recos = []

for n in tqdm(list(g.nbunch_iter( top50.keys() ))):
    print()
    print(n)

    # print([ edge for edge in g[n] ])

    edges = sorted(g[n], key=lambda e: -g[n][e]['covisits'])
    
    # keep only top 10
    edges = edges[:10]

    # reduce with rule of thumb
    edges = edges[:rule_of_thumb([ g[n][n2]['covisits'] for n2 in edges ])]
    
    for n2 in edges:
        print("    " + n2 + " - "+ str(g[n][n2]['covisits']))

    data = {
        "id": mapping_slug_id(n),
        "recommendations": [ { "id": mapping_slug_id(n2), "score": g[n][n2]['covisits'] } for n2 in edges ]
    }

    json.dump(data, open('prod/'+mapping_slug_id(n)+".json", "w"), indent=4, separators=(',', ': '))

    top50recos.append(data)

json.dump(top50recos, open('prod/all.json', "w"), indent=4, separators=(',', ': '))
