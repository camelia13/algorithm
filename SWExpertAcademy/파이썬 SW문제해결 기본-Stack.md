## 파이썬 SW문제해결 기본

### Stack1

```python
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
    
```
