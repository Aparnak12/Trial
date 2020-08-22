import operator

def hasArrived(currentTime,arrivalTime) :
    if(arrivalTime < currentTime) :
        return True
    else :
        return False
    
#start here    
#input
n = int(input("Enter no. of processes : "))
P = [] #list of tuples
for i in range(0,n) :
    AT = int(input("Enter arrival time of P"+str(i+1)+" : "))
    BT = int(input("Enter burst time of P"+str(i+1)+" : "))
    P.append((("P"+str(i+1)),AT,BT))
    
print(P)

ZAT = []
NZAT = []
for process in P :
    if(process[1] == 0) :
        ZAT.append(process)
    else :
        NZAT.append(process)
ZAT.sort(key = operator.itemgetter(2)) #sorting zero AT processes by their BT
NZAT.sort(key = operator.itemgetter(2,1))

print(ZAT)
print(NZAT)

GC = []
GC.append(0)
i = 0
for ele in ZAT :
    GC.append((ele[0],GC[i],GC[i]+ele[2])) #might throw an error here
    i = i+1

print(GC)

ct = 0
for ele in NZAT :
    if(hasArrived(ct,ele[1])) :
        GC.append(GC[i]+ele[2])
        i = i+1
        ct = ct + GC[i]
    else :
        #doubt 
print(GC)

