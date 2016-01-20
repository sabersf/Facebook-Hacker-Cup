import numpy as np
import os
import networkx as nx
import math
from collections import Counter

f = open("ccc.txt","r")
out = open("ccc_out.txt","w")
n = int(f.readline())
for cnt in range(n):
    k = int(f.readline())
    x = {}
    x = f.readline().split()
    x = map(int, x)
    sol = 0
    for i in range(1,k):
        if x[i] == x[i-1]:
            sol += 3
        if x[i] - x[i-1] > 10:
            sol += math.floor( (x[i] - x[i-1] - 1)/10 )
    if (sol + k) % 4 != 0:
        sol += 4 - ((sol + k) % 4)
    print cnt + 1, int(sol)
    out.write("Case #" + str(cnt+1) + ": " + str(int(sol)) + "\n")
out.close()
