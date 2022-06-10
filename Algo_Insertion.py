from hashlib import new
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import random
import math
import time

def distanceCoo(pointA,pointB):
    dist = math.sqrt((pointA[0]-pointB[0])*(pointA[0]-pointB[0])+(pointA[1]-pointB[1])*(pointA[1]-pointB[1])+(pointA[2]-pointB[2])*(pointA[2]-pointB[2]))
    return dist

def totalDistance(List):
    tempList = List[:]
    total = 0
    for x in range(1,len(tempList)):
        total += distanceCoo(tempList[x-1],tempList[x])
    return total

def bestInsert(List,point):
    tempList = List[:]
    tempList.insert(1,point)
    currentBestDist = totalDistance(tempList)
    currentBestPlace = 1
    for x in range(2,len(tempList)):
        tempList = List[:]
        tempList.insert(x,point)
        total = totalDistance(tempList)
        if(total < currentBestDist):            
            currentBestDist= total
            currentBestPlace = x
    return currentBestPlace

def draw(vect1,vect2):
    ax.plot([vect1[0]] + [vect2[0]], [vect1[1]] + [vect2[1]], [vect1[2]] + [vect2[2]])

    
#Init matplotlib
fig = pyplot.figure()
ax = Axes3D(fig)
fig.add_axes(ax)

#init parameters 
numberOfFly = 10
listOfFly = []
pointDeDepart = [0,0,0]
bestWay = [pointDeDepart]





#ALGO avec donnée random
#init jeu de donnée et affichage sur le graph
'''
for x in range(numberOfFly):
    a = [random.randint(0,10),random.randint(0,10),random.randint(0,10)]
    listOfFly.append(a)
    ax.scatter(a[0],a[1],a[2])

for x in range(len(listOfFly)):
    pos = bestInsert(bestWay,[listOfFly[x][0],listOfFly[x][1],listOfFly[x][2]])
    bestWay.insert(pos,[listOfFly[x][0],listOfFly[x][1],listOfFly[x][2]])
print(str(bestWay))
for x in range(len(bestWay)-1):
    draw(bestWay[x],bestWay[x+1])'''

#ALGO avec jeu de donnée test
jeuDonneeTest=[[9,2,4],[2,6,2],[5,4,6],[3,0,8],[2,8,6],[2,6,9],[8,6,5],[7,8,8],[6,5,3],[9,2,7]]
jeuDonneeTest=[[9,2,4],[2,6,2],[5,4,6],[3,0,8],[2,8,6],[2,6,9],[8,6,5],[7,8,8],[6,5,3],[9,2,7],[1, 3, 0], [2, 6, 1], [2, 9, 4], [6, 9, 7], [7, 8, 4], [9, 5, 5], [5, 5, 2], [3, 0, 4], [2, 0, 4], [4, 3, 9]]

start = time.time()
for x in range(len(jeuDonneeTest)):
    pos = bestInsert(bestWay,[jeuDonneeTest[x][0],jeuDonneeTest[x][1],jeuDonneeTest[x][2]])
    bestWay.insert(pos,[jeuDonneeTest[x][0],jeuDonneeTest[x][1],jeuDonneeTest[x][2]])
print(str(bestWay))
print(totalDistance(bestWay))
for x in range(len(bestWay)-1):
    draw(bestWay[x],bestWay[x+1])



print("Total time : "+str(int((time.time() - start)*1000))+" ms")
pyplot.show()

