import random

def random_contraction():
    global g

    # random selection of edge
    v1 = list(g.keys())[random.randint(0, len(g)-1)]
    v2 = g[v1][random.randint(0, len(g[v1])-1)]

    # contraction of selected edge
    # merge v2 into v1 and remove v2 from graph
    g[v1].extend(g[v2])
    del g[v2]

    # replace all occurences of v2 value with v1
    for key, l in g.items():
        g[key] = [v1 if x == v2 else x for x in l]

    # remove self-loops
    g[v1] = [x for x in g[v1] if x != v1]


def load_graph():
    g = {}

    # read the text file
    with open('KargerMinCut.txt', 'r') as f:
        adj_list = f.readlines()

    for i, list in enumerate(adj_list):
        list = list.strip().split('\t')
        g[int(list[0])] = [int(v) for v in list[1:]]
    return g

############################################################


min_cut = []
for i in range(100):
    g = load_graph()

    while(len(g) > 2):
        random_contraction()

    min_cut.append(len(g[list(g.keys())[0]]))

print(min_cut)
print(min(min_cut))