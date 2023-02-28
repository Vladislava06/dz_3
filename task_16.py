
n = int (input())
list = map(int, (input().split()))
count = 0
for i  in list:
    if i == n:
        count +=1
print(count)