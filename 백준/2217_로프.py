k = int(input())
a = []

for i in range(k):
    a.append(int(input()))
a.sort()

m = 0

for i in range(1, k+1):
    weight = a[-i] * i
    m = max(m, weight)
print(m)
