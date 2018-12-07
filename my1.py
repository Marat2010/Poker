import random

a = random.randrange(1,11)

liC = ['c2','c3','c4','c5','c6','c7','c8','c9','c10','cv','cd','ck','ct']
liB = ['b2','b3','b4','b5','b6','b7','b8','b9','b10','bv','bd','bk','bt']
liP = ['p2','p3','p4','p5','p6','p7','p8','p9','p10','pv','pd','pk','pt']
liK = ['k2','k3','k4','k5','k6','k7','k8','k9','k10','kv','kd','kk','kt']


li = liC + liB + liP + liK

#print(li)
#li = random.choice(liC,liB,liP,liK)

stol = []
#n = input("Еще? (1-стоп): ")
while str(input("Еще? (y-продолжить): ")) == 'y':
    stol = []
    i = 0
    while i < 5 :
        kart = random.choice(li)
        li.remove(kart)
        stol.append(kart)
        i+=1
    print(stol)
    print(li)

# n = 2 + 3
# print(n)



