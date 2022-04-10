n = int(input())
sum = n
cnt = 0

while True:
    a = sum // 10
    b = sum % 10
    c = (a + b) % 10
    sum = (b * 10) + c

    cnt = cnt + 1
    if(sum == n):
        break
    
print(cnt)