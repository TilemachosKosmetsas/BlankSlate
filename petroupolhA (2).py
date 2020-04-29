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
       

    




def petroupolh2000():   #edw rixnoume to zari polles fores gia na doume ti 
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
        
    while x < 1000:
          petroupol(arxikoposo)
          if (starter - money2) <= 0:
                totalneg = float(counterneg) + float(starter - money2)
                counterneg = float(totalneg)
                
          elif (starter - money2) > 0:
                totalpos = float(counterpos) + float(starter - money2)
                counterpos = float(totalpos)
                
          
                
          x += 1
    '''
    print ("you paid",arxikoposo,"dollars for every round, and that is a total of",int(arxikoposo)*(x),"finally \n you left  the house with ",float(totalpos)+float(totalneg),end="")
    if (float(totalpos)+float(totalneg))>= 0 :
        
        print (" profit ")
        print ("therefore , for every dollar you paid you WON",(float(totalpos)+float(totalneg))/(int(arxikoposo)*(x)),"dollars\n")
        
    else :
        print (" loss")
        print ("therefore , for every dollar you paid you LOST",(float(totalpos)+float(totalneg))/(int(arxikoposo)*(x)),"dollars \n")
    '''
    factor =(float(totalpos)+float(totalneg))/(int(arxikoposo)*(x))
    


def median():
    global vara
    y=0
    factorlist = []
    while y < 30:  #edw to paixnidi paizetai apo polloys paiktes
    
        
    
    
        petroupolh2000()
        factorlist.append(factor)
        y +=1
            
    print ("\n When this number",sum(factorlist),"\n","tends to zero the game is fair")
    print (" and this is the initial value you gave : ", arxikoposo)
    vara=(sum(factorlist))
    

k = 0
varadd=[]
while k < 10 :   #edw epanalamvanw ti diadikasia gia na dw ksana kai ksana ti ginetai me χι paiktes pou paizoun o kathenas ψι paixnidia
    median()
    varadd.append(vara)
    k+=1
print ("\n",sum(varadd))    






