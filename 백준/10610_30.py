N = int(input())
N = str(N)
S = 0
a = [0] * 10

for i in range(len(N)):
    a[int(N[i])] += 1

if a[0] != 0:
    for i in range(len(N)):
        S += int(N[i])

    if S % 3 == 0:
        for i in range(9, -1, -1):
            if a[i] != 0:
                print(str(i) * a[i], end='')
            else:
                continue
    else:
        print(-1)
else:
    print(-1)
