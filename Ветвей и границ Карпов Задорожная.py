from pprint import pprint
n=int(input("сколько будет точек?"))
inf=float("Inf")
a=[[inf,6,4,8,7],[6,inf,7,11,7],[4,7,inf,4,3],[8,11,4,inf,5],[7,7,3,5,inf]]
b=[]
ch=0
s=""
for q in range(n-1):
    j1=0
    i1=0
    mx0=0
    for i in range(n):
        min1=min(a[i])
        if min1==inf:
            min1=0
        ch+=min1
        for j in range(n):
            a[i][j]-=min1
    for i in range(n):
        mas=[]
        for j in range(n):
            mas.append(a[j][i])
        min1=min(mas)
        if min1==inf:
            min1=0
        ch+=min1
        for j in range(n):
            a[j][i]-=min1

    for i in range(n):
        for j in range(n):
            if a[i][j]==0:
                mas=[]
                mas1=[]
                for k in range(n):
                    if k!=i:
                        mas.append(a[k][j])
                    if k!=j:
                        mas1.append(a[i][k])
                if min(mas)+min(mas1)> mx0:
                    i1=i
                    j1=j
                    mx0=min(mas)+min(mas1)
    for i in range(n):
        for j in range(n):
            if i==i1 or j==j1:
                a[i][j]=inf
    if s=="":
        s=str(i1)+str(j1)
    else:
        b.append(str(i1)+str(j1))
        for i in b:
            if i[1] in s:
                s=i+s
                b.remove(i)
            elif i[0] in s:
                s=s+i
                b.remove(i)
            else:
                a[int(i[1])][int(i[0])]=inf
    a[int(s[-1])][int(s[0])]=inf
print(ch, s)