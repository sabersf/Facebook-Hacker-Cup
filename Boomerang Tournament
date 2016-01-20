

import numpy as np
import os
import networkx as nx
import math
import itertools
from collections import Counter



f = open("boomerang.txt","r")
out = open("boomerang_out.txt","w")
test_cases = int(f.readline())
for cnt in range(test_cases):
    n = int(f.readline())
    pos = [0] * n
    best = [n] * n
    worst = [1] * n
    W = [0 for i in range(n)]
    for i in range(n):
        pos[i] = i
        W[i] = map(int, f.readline().split())
    perm = itertools.permutations(pos, n)
    for x in perm:
        #process list x to see who's the winner
        position = [0] * n
        win = [0] * n
        new_list = x
        while len(new_list) > 1:
            tmp = [0] * (len(new_list)/2)
            for i in range(len(tmp)):
                if W[new_list[2*i]][new_list[(2*i) + 1]] == 1:
                    win[new_list[2*i]] += 1
                    tmp[i] = new_list[2*i]
                else:
                    win[new_list[(2*i)+1]] += 1
                    tmp[i] = new_list[(2*i) + 1]
            new_list = tmp
        for i in range(n):
            tmp_count = 0
            for j in range(n):
                if win[j] > win[i]:
                    tmp_count += 1
            position[i] = 1 + tmp_count
            if position[i] < best[i]:
                best[i] = position[i]
            if position[i] > worst[i]:
                worst[i] = position[i]


    out.write("Case #" + str(cnt+1) + ":\n")
    #print "Case  #",str(cnt+1),":"
    for i in range(n):
        out.write(str(best[i]) + " " + str(worst[i]) + "\n")
        #print best[i] ," " , worst[i]
out.close()
