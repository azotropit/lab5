import sys
with open('graph1.txt', 'r') as f:
    graph1 = []
    for line in f:
        row = [int(num) for num in line.split()]
        graph1.append(row)

with open('graph2.txt', 'r') as f:
    graph2 = []
    for line in f:
        row = [int(num) for num in line.split()]
        graph2.append(row)

if (len(graph1) != len(graph2)):
    print("Not isomorphic")
    sys.exit()
else:
    l = len(graph1)
    for i in range(l):
        for j in range(l):
            if ((graph1[i][j] == 0 != graph2[i][j]) or (graph1[i][j] != 0 and graph2[i][j] ==0)):
                print("Not isomorphic")
                sys.exit()

print("Isomorphic")