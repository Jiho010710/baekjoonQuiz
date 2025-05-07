N = int(input())
ans = [0]*10
start, digit = 1, 1
while start <= N:
    while N % 10 != 9 and start <= N:
        for i in str(N):
            ans[int(i)] += digit
        N -= 1
    if N < start: break
    while start % 10 != 0 and start <= N:
        for i in str(start):
            ans[int(i)] += digit
        start += 1
    cnt = (N//10 - start//10 + 1)
    for i in range(10):
        ans[i] += cnt * digit
    start //= 10
    N //= 10
    digit *= 10
print(*ans)
