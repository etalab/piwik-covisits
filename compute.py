import networkx as nx
import glob
import json
#from itertools import combinations
from itertools import permutations

# agregate
def build_graph():

    g = nx.Graph()

    for day in glob.glob('visits/*'):
        print(day)

        visits = json.load(open(day, 'r'))

        covisits = [ list(permutations(urls, 2)) for urls in visits ]

        for edges in covisits:
            for e in edges:
                if g.has_edge(e[0], e[1]):
                    g[e[1]][e[0]]['covisits'] += 1
                else:
                    g.add_edge(e[0], e[1], covisits=1)

                if 'links' in g.nodes[e[0]]:
                    g.nodes[e[0]]['links'] += 1
                else:
                    g.nodes[e[0]]['links'] = 1

    return g


g = build_graph()

print(len(g.nodes))
print(len(g.edges))

nx.write_gexf(g, 'covisits.gexf')
