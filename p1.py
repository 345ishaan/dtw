import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

seq1=np.array([1,1,2,3,2,0])
seq2=np.array([0,1,1,2,3,2,1])

'DTW - finds the path with maximum correlation or minimum distance'

path=[[0 for i in range(len(seq1))]for j in range(len(seq2))]

for i in range(len(seq2)):
    for j in range(len(seq1)):
        path[i][j]=(seq2[i]-seq1[j])**2

cost=[[0 for i in range(len(seq1))]for j in range(len(seq2))]

'Filling the cost table by using the distance'

for i in range(len(seq2)):
    for j in range(len(seq1)):
        if i == 0:
            if j==0:
                cost[i][j]=path[i][j]
            else:
                cost[i][j]=cost[i][j-1]+path[i][j]
        elif j == 0:
            cost[i][j]=cost[i-1][j]+path[i][j]
        else:
            cost[i][j]=min(cost[i-1][j],cost[i][j-1],cost[i-1][j-1])+path[i][j]

'Backtracking the cost table to find the path'
final_cost=cost[len(seq2)-1][len(seq1)-1]
final_path=[(len(seq2)-1,len(seq1)-1)]
while (1):
    length=len(final_path)
    x=final_path[length-1][0]
    y=final_path[length-1][1]
    if x==0:
        break
    if y != 0:
        min_cost=min(cost[x-1][y-1],cost[x-1][y],cost[x][y-1])
        if min_cost == cost[x-1][y-1]:
            final_path.append((x-1,y-1))
        elif min_cost == cost[x][y-1]:
            final_path.append((x,y-1))
        else:
            final_path.append((x-1,y))
    else:
        final_path.append((x-1,y))
final_path.reverse()
print final_path

'Visualize the plot'

plt.plot(seq1,'bo-',label='x')
plt.plot(seq2,'g^-',label='y')

plt.legend();

for pathx,pathy in final_path:
    print "{},{}".format(pathx,pathy)
    plt.plot([pathx,pathy],[seq2[pathx],seq1[pathy]],'r')

    

plt.show()
    
                    
