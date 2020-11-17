<!-- 이 레포지토리는 과거에 받은 질문내용을 정리하여 재 구성한 것입니다. -->

# 피보나치 수열 / 소수

어떻게 구할 수 있을까요?

## 피보나치 수열

### 규칙

피보나치 수열은 다음을 만족하는 수열입니다.

![](https://latex.codecogs.com/gif.latex?F_0=0,F_1=1)

and

![](https://latex.codecogs.com/gif.latex?F_n=F_{n-1}+F_{n-2})

for n > 1.

수열의 시작부분은 다음과 같습니다:

![](https://latex.codecogs.com/gif.latex?0,1,1,2,3,5,8,13,21,34,55,89,144,...)

### 제약조건

> 아직 Python의 list를 배우지 않은 상태입니다.

리스트를 사용하면 피보나치 수열을 매우 간단하게 표현할 수 있습니다.

```python
F = [0,1]
for n in range(2, 100):
    F.append( F[n-1] + F[n-2] )
print(F)
```

하지만 아직 리스트를 사용할 수 없으므로, 조금 더 돌아가는 방법으로 코드를 작성하였습니다.

> `fibonacci.py`

## 소수

소수(Prime number)는 오직 1과 자기 자신으로만 나누어 떨어지는 수 입니다.

이를 정리하면,

> 임의의 수 ![](https://latex.codecogs.com/gif.latex?n)이 소수이려면 ![](https://latex.codecogs.com/gif.latex?n)이 ![](https://latex.codecogs.com/gif.latex?2) 와 ![](https://latex.codecogs.com/gif.latex?n-1) 사이의 수로 나누어 떨어지지 않으면 됩니다.

이는 다음과 같이 구현할 수 있습니다.

```python
n = 101 # 소수인지 검사 할 수

isprime = True
for x in range(2, n): # 2부터 n-1까지 차례대로 x에 대입
    if n % x == 0: # 만약 나머지가 없다면 => 즉, 나누어 떨어진다면 소수가 아니다.
        isprime = False

print('소수입니까?: ', isprime)
```

> `prime.py`
