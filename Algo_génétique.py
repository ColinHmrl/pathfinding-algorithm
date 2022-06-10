from matplotlib import pyplot
import random
import math
import time
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

fig = pyplot.figure()
ax = Axes3D(fig)
fig.add_axes(ax)




def distance(pointA,pointB):
    dist = math.sqrt((pointA[0]-pointB[0])*(pointA[0]-pointB[0])+(pointA[1]-pointB[1])*(pointA[1]-pointB[1])+(pointA[2]-pointB[2])*(pointA[2]-pointB[2]))
    return dist

def distanceTotal(List):
    tempList = List[:]
    total = 0
    for x in range(1,len(tempList)):
        total += distance(tempList[x-1],tempList[x])
    return total
    
#réalise une mutation chez un individu
#echange 2 donnée voisine chez l'individu
def mutation(individu):
    '''if(random.randint(1,10)<=8):
        value = random.randint(1,len(individu)-2)
        #print(value)
        temp = individu[value]
        individu[value] = individu[value+1]
        individu[value+1] = temp
    '''
    #nouveau type de mutation :
    #échange 2 gènes aléatoires
    if(random.randint(1,10)<=8):
        value1 = random.randint(1,len(individu)-1)
        value2 = random.randint(1,len(individu)-1)

        temp = individu[value1]
        individu[value1] = individu[value2]
        individu[value2] = temp
    
    return individu


#réalise une hybridation entre 2 individus
# l'hybridation est réalisé par la moitié du parent 1 et l'autre moitié du parent 2, les données en doublons vont à la fin
def hybridation(individu1,individu2):
    crossoverPoint = int(len(individu1)/3)
    child = []
    for x in range(crossoverPoint):
        child.append(individu1[x])
    for y in range(crossoverPoint,len(individu2)):
        if (individu2[y] not in child):
            child.append(individu2[y])
    for z in range(crossoverPoint):
        if(individu2[z] not in child):
            child.append(individu2[z])
    return child

def newGen(individu):
    generation= []
    for x in range(int(len(individu)*2)):
        indi = mutation(individu[:])
        generation.append(indi)
    return generation

def triIndividu(gen,distGen):
    for x in range(len(distGen)):
        for y in range(len(distGen)-1):
            if( distGen[y]>distGen[y+1]):
                tempDistGen = distGen[y]
                tempIndividu = gen[y]

                distGen[y] = distGen[y+1]
                gen[y] = gen[y+1]

                distGen[y+1] = tempDistGen
                gen[y+1] = tempIndividu

def drawLines(tab) :
    for p in range(len(tab)) :
        if(p != len(tab)-1) :
            draw(tab[p],tab[p+1])

def draw(point1,point2):
    ax.plot([point1[0]] + [point2[0]], [point1[1]] + [point2[1]], [point1[2]] + [point2[2]])

def main():

    jeuDonneeTest=[[0,0,0],[9,2,4],[2,6,2],[5,4,6],[3,0,8],[2,8,6],[2,6,9],[8,6,5],[7,8,8],[6,5,3],[9,2,7]]
    #jeuDonneeTest=[[0,0,0],[9,2,4],[2,6,2],[5,4,6],[3,0,8],[2,8,6],[2,6,9],[8,6,5],[7,8,8],[6,5,3],[9,2,7],[1, 3, 0], [2, 6, 1], [2, 9, 4], [6, 9, 7], [7, 8, 4], [9, 5, 5], [5, 5, 2], [3, 0, 4], [2, 0, 4], [4, 3, 9]]
    jeuDonneeTest2=[[0,0,0],[1, 3, 0], [2, 6, 1], [2, 9, 4], [6, 9, 7], [7, 8, 4], [9, 5, 5], [5, 5, 2], [3, 0, 4], [2, 0, 4], [4, 3, 9]]
    jeuDonneeTest=[[9,2,4],[2,6,2],[5,4,6],[3,0,8],[2,8,6],[2,6,9],[8,6,5],[7,8,8],[6,5,3],[9,2,7],[1, 3, 0], [2, 6, 1], [2, 9, 4], [6, 9, 7], [7, 8, 4], [9, 5, 5], [5, 5, 2], [3, 0, 4], [2, 0, 4], [4, 3, 9]]

    bestScore = distanceTotal(jeuDonneeTest)
    print("How many generations would you want?")
    nbrGen = int(input())
    start = time.time()
    
    #init du jeu de donnee et shuffle de la premiere generation
    gen = newGen(jeuDonneeTest)
    for elem in range(len(jeuDonneeTest)):
        random.shuffle(gen,lambda: random.random())

    for generation in range(nbrGen):
        gen = newGen(hybridation(gen[0],gen[1]))
        distGen = []
        for x in range(len(gen)):
            dist = distanceTotal(gen[x])
            distGen.append(dist)
        triIndividu(gen,distGen)

        
        #print("Génération n° "+str(generation)+" distGen :"+str(distGen[0]))
        #print("gen :"+str(gen))
        #print("distGen :"+str(distGen[0]))
        
        
        #meilleur individu trouvé, toutes générations confondues 
        if(distGen[0]<bestScore):
            bestScore = distGen[0]
            bestTime = time.time() - start
            bestWay = gen[0]
            print("Current best is : "+str(bestScore)+" in "+str(int((time.time() - start)*1000))+" ms, at the "+str(generation)+"th generation")

    print("Best found is : "+str(bestScore)+" in "+str(int(bestTime*1000))+" ms")
    print("The way is : "+str(bestWay))
    print("Total time : "+str(int((time.time() - start)*1000))+" ms")
    drawLines(bestWay)

main()
pyplot.show()
