## 파이썬 SW문제해결 기본

### LIST1

```python
# 4831. 전기버스

T = int(input()) # 그리디 서치 문제 같은데 아직 개념을 제대로 이해하지 못한듯. 더 간단한 풀이가 있을듯

for j in range(T):
    K, N, M = map(int, input().split())
    ind = list(map(int, input().split()))

    L = [0] * N
    X = K

    for i in range(len(ind)):
        try:
            if ind[i] > X:
                L[ind[i-1]] = 1
                X = K + ind[i-1]

        except:
            L = [0] * N

    if X < N:
        if (ind[i] + K) >= N:
            L[ind[i]] = 1
        else:
            print(1)
            L = [0] * N
            break

    indices = [i for i, x in enumerate(L) if x == 1]
    for i in range(len(indices)-1):
        if indices[i+1] - indices[i] > K:
            L = [0] * N
            break

    print("#{0} {1}".format(j + 1, sum(L)))
```
