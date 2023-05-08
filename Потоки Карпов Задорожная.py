from pprint import pprint
x,y=map(int, input("точка 1 и точка 2 ").split())
x-=1
orx=x
y-=1
ory=y
n=int(input("сколько будет точек? "))
a=[]
gsch=0
ormin=1
for i in range(n):
    a.append([])
#for i in range(n):
#    for j in range(n):
#        inp=int(input())
#        a[i].append(inp)
#        m.append(inp)
a=[[0, 3, 0, 4, 0],
 [0, 0, 6, 0, 5],
 [0, 0, 0, 0, 2],
 [0, 3, 0, 0, 3],
 [0, 0, 0, 0, 0]]
l="1"
while l!="":
    rast=[]
    m=[100]
    pos=[]
    for i in range(n):
        rast.append(max(m)**10)
        pos.append(0)
    rast[x]=0
    put=[]
    nach=""
    for j in range(n):
        m=[]
        x1=x
        for i in range(n):
            if a[x][i]!=0 and pos[i]==0:
                rast[i]=min(rast[i],rast[x]+a[x][i])
                if rast[i]==rast[x]+a[x][i]:
                    put.append(str(x)+str(i))
                    nach+=str(x)
                m.append(a[x][i])
                if min(m)==a[x][i]:
                    x1=i
            pos[x]=1
        x=x1
    for i in put:
        for j in put:
            if i[-1]==j[0]:
                put.append(i+j)
    l=""
    ormin=0
    x=orx
    y=ory
    for i in put:
        sch = 0
        min1 = float("Inf")
        if i[0]==str(x) and i[-1]==str(y):
            for j in range(0,len(i),2):
                sch+=a[int(i[j])][int(i[j+1])]
                min1=min(min1,a[int(i[j])][int(i[j+1])])
            if sch==rast[y]:
                l=i
                ormin=min1
    gsch+=ormin
    for i in range(0,len(l),2):
        a[int(l[i])][int(l[i+1])]-=ormin
print(gsch)