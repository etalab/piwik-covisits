import networkx as nx
import json


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

g = nx.read_gexf('covisits.gexf')

# data = { n : list(g[n]) for n in g }
# json.dump(data, open('scores/all.json', 'w'), indent=4, separators=(',', ': '))   

for n in list(g):
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
