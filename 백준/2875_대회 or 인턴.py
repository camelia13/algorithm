n, m, k = map(int, input().split())
answer = 0
v = n - 2 * m

if v >= 0:
    if k - v > 0:
        answer = m - ((k - v) // 3 + 1)
        if (k - v) % 3 == 0:
            answer += 1
    else:
        answer = m

else:
    if k - (m - n // 2) > 0:
        answer = n // 2 - ((k - (m - n // 2)) // 3 + 1)
        if (k - (m - n // 2)) % 3 == 0:
            answer += 1
        if answer < 0:
            answer = 0
    else:
        answer = n // 2
print(answer)
