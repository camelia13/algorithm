## 파이썬 SW문제해결 기본

### Stack1

```python
# 4869. 종이붙이기
def count_paper(N):
    if N > 1:
        if N % 2 == 0:
            return count_paper(N-1) * 2 + 1 # 사실 수학 문제에 가깝다
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
            if not L: # 닫기 괄호가 열기 괄호보다 먼저 나온 경우 검사 
                L = 'error'
                break
            elif c == ')' and L[-1] == '(':
                a += L.pop()
            elif c == '}' and L[-1] == '{':
                a += L.pop()
            else: # 이 부분 없으면 test case 10번째에서 실패한다. 근데 왜 필요하지??
                L.append(c)
                break
    if not a: # 공백만 입력으로 넣어준 경우 검사
        L = 'empty'
    if not L and sent:
        valid = 1
    print("#{} {}".format(t, valid))

# 4871. 그래프 경로
T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    graph = {}
    for _ in range(E):
        k, v = input().split()
        graph[k] = {v} | (set() if graph.get(k) is None else graph[k]) # '|'은 합집합 기호
    start, end = input().split()
    stack = [(start, [start])]
    result = []
    valid = 0
    while stack:
        n, path = stack.pop() # dfs (cf. bfs: queue.pop(0))
        if n == end:
            result.append(path)
            break
        else:
            try:
                for m in (graph[n] - set(path)):
                    stack.append((m, path + [m]))
            except: pass
    if result:
        valid = 1
    print("#{} {}".format(t, valid))
```

### Stack2
```python
# 4874. Forth
def operator(op, n1, n2):
    return {'+':n1+n2, '-':n1-n2, '*':n1*n2, '/':int(n1/n2)}[op] # 이 문제에서는 정수로 받아야함

T = int(input())
for t in range(1, T+1):
    formula = list(input().split())
    num = []
    try:
        for i in range(len(formula)):
            if formula[i].isdigit():
                num.append(int(formula[i]))
            elif formula[i] == '.':
                if len(num) == 1:
                    v = num.pop()
                else:
                    v = 'error'
            else:
                a2, a1 = num.pop(), num.pop()
                num.append(operator(formula[i], a1, a2))
    except:
        v = 'error'
    print("#{} {}".format(t, v))
```
