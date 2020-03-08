## 파이썬 SW문제해결 기본

### Stack1

```python
# 4869. 종이붙이기
def count_paper(N):
    if N > 1:
        if N % 2 == 0:
            return count_paper(N-1) * 2 + 1
        else:
            return count_paper(N-1) * 2 - 1
    else:
        return 1 
        
T = int(input())
for t in range(1, T+1):
    N = int(input()) // 10
    print("#{} {}".format(t, count_paper(N)))

# 4866. 괄호검사
T = int(input())
for t in range(1, T + 1):
    sent = input()
    L = []
    valid = 0
    a = ''
    for c in sent:
        if c == '(' or c == '{':
            L.append(c)
        elif c == ')' or c == '}':
            if not L:
                L = 'error'
                break
            elif c == ')' and L[-1] == '(':
                a += L.pop()
            elif c == '}' and L[-1] == '{':
                a += L.pop()
            else:
                L.append(c)
                break
    if not a:
        L = 'empty'
    if not L and sent:
        valid = 1
    print("#{} {}".format(t, valid))
```
