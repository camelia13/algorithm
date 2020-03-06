## 파이썬 SW문제해결 기본

### String

```python
# 4864. 문자열 비교
def Boyer_Moore(pattern, text):  # 보이어 무어 검색 알고리즘 구현
    N = len(pattern)
    M = len(text)
    shift = list(pattern)
    shift.reverse()

    j = 0
    i = N - 1
    while i > 0 and j < M:
        if pattern[i] != text[j]:
            i = N - 1
            if text[j] not in pattern:
                j += N
            else:
                j += shift.index(text[j])
        else:
            i -= 1
            j -= 1
    if i == 0: return 1
    else: return 0

T = int(input())
for t in range(1, T + 1):
    str1 = input()
    str2 = input()
    print("#{} {}".format(t, Boyer_Moore(str1, str2)))

# 4861. 회문
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    L = []
    for _ in range(N):
        l = list(input())
        L.append(l)

    for l in L:
        i = 0
        while i <= N-M:
            valid = l[i:M+i]
            if valid == valid[::-1]:
                print("#{} {}".format(t, ''.join(valid)))
            i += 1

    L_t = list(zip(*L)) # 2-d matrix transpose
    for l in L_t:
        i = 0
        while i <= N-M:
            valid = l[i:M+i]
            if valid == valid[::-1]:
                print("#{} {}".format(t, ''.join(valid)))
            i += 1
```
