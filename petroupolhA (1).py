import random
import matplotlib
import matplotlib.pyplot as plt

print("Kalws irthes stin Petroupoli, \nme posa lefta theleis na ksekiniseis to paixnidi? ")
arxikoposo = input("")
global vx
global vy


def coin():
    x = random.randint(1,2)
    if x == 1 :
        return True
        #print (x)
    else:
        return False
        #print ("dyo")


        
def petroupol(money1):  #edw to paixnidi paizetai mia fora
    global starter
    global money2
    money2= int(money1)
    starter = int(2)
     
    while True:
        if coin():
            telikoposo = (starter*2)
            starter= telikoposo
            
            continue
        else:
            #if starter - money2 > 0 :
                #print ("you made it! , you won",  starter - money2, "money")
                #print ("and the game is over")
            #else:
                #print("you lost", starter - money2, "money")
            break
       

    




def petroupolh2000():   #edw to paixnidi paizetai polles fores gia na doume ti 
    counterneg = int(0) #ginetai telika (enas paikths)
    counterpos = int(0)
    global totalpos
    global totalneg
    totalpos = int(0)
    totalneg= int(0)
    totalneg =  float(0)
    global x
    global factor
    x = 0
        
    while x < 100000:
          petroupol(arxikoposo)
          if (starter - money2) <= 0:
                totalneg = float(counterneg) + float(starter - money2)
                counterneg = float(totalneg)
                
          elif (starter - money2) > 0:
                totalpos = float(counterpos) + float(starter - money2)
                counterpos = float(totalpos)
                
          vx.append(x)
          vy.append(counterpos+counterneg)
                
          x += 1
     
    print ("you paid",arxikoposo,"dollars for every round, and that is a total of",int(arxikoposo)*(x),"finally \n you left  the house with ",float(totalpos)+float(totalneg),end="")
    if (float(totalpos)+float(totalneg))>= 0 :
        
        print (" profit ")
        print ("therefore , for every dollar you paid you WON",(float(totalpos)+float(totalneg))/(int(arxikoposo)*(x)),"dollars\n")
        
    else :
        print (" loss")
        print ("therefore , for every dollar you paid you LOST",(float(totalpos)+float(totalneg))/(int(arxikoposo)*(x)),"dollars \n")
    factor =(float(totalpos)+float(totalneg))/(int(arxikoposo)*(x))
    

y=0
factorlist = []
while y < 100:  #edw to paixnidi paizetai apo polloys paiktes
    
    vx = []
    vy = []
    
    
    petroupolh2000()
    factorlist.append(factor)
    
    plt.plot(vx,vy)
    y +=1
print ("\n",sum(factorlist),"\n","when this value tends to zero the game is fair")
print ("\n This is the initial value you gave :" ,arxikoposo)   
    



plt.ylabel('posa sta opoia kinoumaste')
plt.xlabel('game counter')
plt.show()


