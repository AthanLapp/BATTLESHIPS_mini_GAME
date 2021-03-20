# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 19:26:53 2021

@author: athan
"""

import random

aq = [0,0,0,0,0,0,0,0,0,0]
bq = [0,0,0,0,0,0,0,0,0,0]
cq = [0,0,0,0,0,0,0,0,0,0]
dq = [0,0,0,0,0,0,0,0,0,0]
eq = [0,0,0,0,0,0,0,0,0,0]
fq = [0,0,0,0,0,0,0,0,0,0]
gq = [0,0,0,0,0,0,0,0,0,0]
hq = [0,0,0,0,0,0,0,0,0,0]
iq = [0,0,0,0,0,0,0,0,0,0]
jq = [0,0,0,0,0,0,0,0,0,0]

errors = 0
hits = 0

onex = random.randint(0,7)
oney = random.randint(0,9)

twox = random.randint(0,9)
twoy = random.randint(0,8)


#print(onex, oney, twox, twoy)
print(0,aq)
print(1,bq)
print(2,cq)
print(3,dq)
print(4,eq)
print(5,fq)
print(6,gq)
print(7,hq)
print(8,iq)
print(9,jq)


for i in range (100):
    x = int(input('x'))
    y = int(input('y'))
    if((( x == onex or x == (onex +1) or x == (onex + 2)) and (y == oney))) or ((x == twox) and (y == twoy or y == (twoy + 1))):
        hits += 1
        print('hit no', hits)
        if(y==0):
            aq[x]=8
        elif(y==1):
            bq[x]=8
        elif(y==2):
            cq[x]=8
        elif(y==3):
            dq[x]=8
        elif(y==4):
            eq[x]=8
        elif(y==5):
            fq[x]=8
        elif(y==6):
            gq[x]=8
        elif(y==7):
            hq[x]=8
        elif(y==8):
            iq[x]=8
        elif(y==9):
            jq[x]=8
    elif((( x == onex or x == (onex +1) or x == (onex + 2)) and (y == oney)) and ((x == twox) and (y == twoy or y == (twoy + 1)))):
        hits += 2
        print('Hitted double !!! hits no', hits)
        if(y==0):
            aq[x]=9
        elif(y==1):
            bq[x]=9
        elif(y==2):
            cq[x]=9
        elif(y==3):
            dq[x]=9
        elif(y==4):
            eq[x]=9
        elif(y==5):
            fq[x]=9
        elif(y==6):
            gq[x]=9
        elif(y==7):
            hq[x]=9
        elif(y==8):
            iq[x]=9
        elif(y==9):
            jq[x]=9
    else:
        errors += 1
        print('Error no', errors)
        if(y==0):
            aq[x]=1
        elif(y==1):
            bq[x]=1
        elif(y==2):
            cq[x]=1
        elif(y==3):
            dq[x]=1
        elif(y==4):
            eq[x]=1
        elif(y==5):
            fq[x]=1
        elif(y==6):
            gq[x]=1
        elif(y==7):
            hq[x]=1
        elif(y==8):
            iq[x]=1
        elif(y==9):
            jq[x]=1
    print(0,aq)
    print(1,bq)
    print(2,cq)
    print(3,dq)
    print(4,eq)
    print(5,fq)
    print(6,gq)
    print(7,hq)
    print(8,iq)
    print(9,jq)
    
    if errors == 10:
        print('You loose...')
        break
    
    if hits == 5:
        print('Operation succesful !!! Aihoo Captain !!!')
        break