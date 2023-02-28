n=[int(i) for i in input().split()]
x=int(input())
count=0
for i in range(len(n)):
    if (x-n[i])<x-count and x-n[i]>0:
        count=i
print(n[count])