## 파이썬 SW문제해결 기본

### LIST1

```python
# 4831. 전기버스
T = int(input()) 

for j in range(T):
    K, N, M = map(int, input().split())
    ind = list(map(int, input().split()))

    L = [0] * N
    X = K

    for i in range(len(ind)): # 마지막 정류소는 검사하지 않는다. 비효율적인 코드
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

    indices = [i for i, x in enumerate(L) if x == 1] # 리스트 L의 값이 1인 인덱스를 가져옴
    for i in range(len(indices)-1):
        if indices[i+1] - indices[i] > K:
            L = [0] * N
            break

    print("#{0} {1}".format(j + 1, sum(L)))
    
### 더 나은 풀이
# 각 정류장 사이를 하나의 구간으로 버스의 현재 위치 갱신과 정류소의 잘못된 설치를 판별하고, 
# while loop로 위 방법을 반복하면 더 쉽게 답을 찾을 수 있다. (이 방법이 문제가 요구하는 그리디 알고리즘인듯)

T = int(input())
for j in range(T):
    K, N, M = map(int, input().split())
    ind = list(map(int, input().split()))

    L = [0] * N
    for e in ind:
        L[e] = 1

    s = 0
    e = K
    cnt = 0

    while True:
        valid = 0
        for i in range(s+1, e+1): # for loop로 정류소 사이에서 사이클 돌린다.
            if L[i] == 1:
                s = i
            else:
                valid += 1

        if valid == K:
            cnt = 0
            break

        cnt += 1
        e = s + K
        if e >= N:
            break

    print('#%d %d'%(j+1, cnt))

```
### LIST2
```python
# 4836. 색칠하기
T = int(input())

for t in range(1,T+1):
    N = int(input())
    L = [[0] * 10 for _ in range(10)]
    cnt = 0
    for _ in range(N):
        r1,c1,r2,c2,c = map(int, input().split())

        if c == 1:
            for i in range(c1, c2+1): 
                for j in range(r1, r2+1):
                    L[i][j] += 1
        elif c == 2:
            for i in range(c1, c2+1):
                for j in range(r1, r2+1):
                    L[i][j] += 2

    for l in L:
        cnt += l.count(3)

    print("#{} {}".format(t, cnt))
    
# 4837. 부분집합의 합
T = int(input())
arr = list(range(1, 13))
n = len(arr)

for t in range(1,T+1):
    N, K = map(int, input().split())
    cnt = 0

    for i in range(1<<n): # 강의에 나온 부분집합 구하는 코드 이해안됨. 외워야할듯
        L = []
        for j in range(n):
            if i&(1<<j):
                L.append(arr[j])

        if len(L) == N and sum (L) == K:
            cnt += 1

    print("#{} {}".format(t, cnt))
    
# 4839. 이진탐색
def binarySearch(low, high, key, cnt): # 이진 검색 재귀함수로 구현
    if low > high:
        return False
    else:
        middle = (low + high) // 2
        if key == middle:
            return cnt
        elif key < middle:
            return binarySearch(low, middle-1, key, cnt+1)
        elif key > middle:
            return binarySearch(middle+1, high, key, cnt+1)

T = int(input())

for t in range(1,T+1):
    P, A, B = map(int, input().split())
    CA = binarySearch(1, P, A, 0)
    CB = binarySearch(1, P, B, 0)

    if CA > CB:
        print("#{} B".format(t))
    elif CA < CB:
        print("#{} A".format(t))
    else:
        print("#{} 0".format(t))

```
