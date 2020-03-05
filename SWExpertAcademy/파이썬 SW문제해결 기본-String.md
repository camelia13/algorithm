## 파이썬 SW문제해결 기본

### String

```python
# 4864. 문자열 비교
T = int(input())

for t in range(1, T+1):
    cnt = 0
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)
    j = 0
    i = N - 1
    while i > 0 and j < M:
        if str1[i] != str2[j]:
            j += N - 1 - i
            i = N -1
            if str2[j] not in str1:
                j += N
            else: j += 1
        else:
            i -= 1
            j -= 1
    if i == 0: cnt = 1
    else: cnt = 0
    print("#{} {}".format(t, cnt))
    
## 보이어 무어 검색 알고리즘 구현
# 찾으면 1 못 찾으면 -1 반환
def Boyer_Moore(pattern, text):
    N = len(pattern)
    M = len(text)
    j = 0
    while i > 0 and j < M:
        if pattern[i] != text[j]:
            j += N - 1 - i
            i = N - 1
            if text[j] not in pattern:
                j += N
            else:
                j += 1
        else:
            i -= 1
            j -= 1
    if i == 0: return 1
    else: return -1

```
