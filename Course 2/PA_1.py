
# OUTPUT FORMAT
# You should output the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes, separated by
# commas (avoid any spaces).

import copy
import sys
import sys, time, threading

sys.setrecursionlimit(800000)
threading.stack_size(67108864)

# TODO: refractor the code
# https://github.com/ladamalina/coursera-algo/blob/master/PQ4.%20SCCs/kosaraju.py
# https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
# https://www.coursera.org/learn/algorithms-graphs-data-structures/discussions/weeks/1/threads/JiHDKJnVEeetAQoC-amJYg

def load_graph():
    # read the text file
    with open('SCC.txt', 'r') as f:
        lists = f.readlines()

    for i, list in enumerate(lists):
        list = list.strip().split(' ')
        lists[i] = [int(v) for v in list]
    return lists


def lists_to_dict(lists):
    g = {}

    for list in lists:
        if int(list[0]) not in g:
            g[int(list[0])] = [int(list[1])]
        else:
            g[int(list[0])].append(int(list[1]))
    return g


def reverse_lists(ll):
    for l in ll:
        l[0], l[1] = l[1], l[0]


def DFS_Loop(G):
    for k in G.keys():
        if not explored[k]:
            DFS(G, k)


def DFS(G, i):
    global t, explored, f
    explored[i] = True              # mark i as explored
    for j in G.get(i, [0]):
        if not j:
            break
        if not explored[j]:
            DFS(G, j)
    t += 1
    f[i] = t


def DFS_Loop_2(G):
    global s
    for label in reversed(range(1, len(nodes)+1)):   # finishing time from large to small
        if not explored[r_f[label]]:
            s = r_f[label]
            DFS_2(G, r_f[label])

def DFS_2(G, i):
    global catg
    explored[i] = True
    for j in G.get(i, [0]):
        if not j:
            break
        if not explored[j]:
            DFS_2(G, j)
    catg[i] = s


def main():
    global t, explored, nodes, f, r_f, catg

    lists = load_graph()
    g = lists_to_dict(lists)

    r_lists = copy.deepcopy(lists)
    reverse_lists(r_lists)
    r_g = lists_to_dict(r_lists)

    t = 0

    nodes = set(r_g.keys()).union({item for sublist in r_g.values() for item in sublist})
    explored = dict(zip(nodes, [False] * len(nodes)))                # at the beginning, assume all the nodes unexplored
    f = dict(zip(nodes, [0] * len(nodes)))

    DFS_Loop(r_g)
    # print(f)
    r_f = dict(zip(f.values(), f.keys()))
    # print(r_f)

    #----------------------------------------------------------

    nodes = set(g.keys()).union({item for sublist in g.values() for item in sublist})
    explored = dict(zip(nodes, [False] * len(nodes)))  # at the beginning, assume all the nodes unexplored
    catg = dict(zip(nodes, [0] * len(nodes)))

    DFS_Loop_2(g)
    # print(catg)

    leaders = list(set(catg.values()))
    counter = dict(zip(leaders, [0]*len(leaders)))

    for k, v in catg.items():
        counter[v] += 1

    print(sorted(list(counter.values()), reverse=True)[:5])     # [434821, 968, 459, 313, 211]


thread = threading.Thread(target=main)
thread.start()


