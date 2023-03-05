# Feedback
## 230214
### 1644
- 소수를 찾을 때 dp 방식을 이용하였는데, 속도가 느려 알아본 결과 에라토스테네스 체 방법이 있다는 것을 발견 후 사용

### 1766
- 우선순위를 가장 낮은 문제를 풀 때 선행하는 것을 먼저 풀어야 한다고 생각함. 실제로는 먼저 풀 수 있는 문제들 중 가장 숫자가 낮은 것을 뽑아야 했음.
- 1 문제를 풀 면 먼저 풀 수 있는 문제의 종류가 달라지므로, 우선순위를 다시 재정렬 해주어야 함
#### 위상정렬
1. 진입차수가 0인 정점을 큐에 삽입
2. 큐에서 원소를 꺼내 해당 원소와 연결된 간선을 모두 제거
3. 제거한 후에 진입차수가 0인 정점을 큐에 삽입
4. 이후 2~3의 과정을 반복

### 12100
#### Copy and Deepcopy

#### List 2차원 정렬
- Trnspose: matrix = [list(x) for x in zip(*matrix)]
- *는 unpacking zip은 여러 개의 리스트 각 요소를 합쳐줌
- 상하 변경
    for i in range(N):
        tmp = matrix[i]
        tmp.reverse()
        matrix2.append(tmp)

### 20040
- iteration 횟수 증가: sys.setrecursionlimit(10**7)
- unionfind

### 16724
- cycle이 먼저 있지 않은 경우에 대해서 고려하지 못함

### 1018
- 체스판 다시 칠하기
- 체스판 8x8크기로 잘라서 한다는 것을 못 읽어서 푸는 데 오래 걸림
- 부등호는 원래 문자를 최대한 덜 바꾸는 쪽으로 작성하기

### 1202
- 보석 상인
- heapq.heappush(jew_pos, -heapq.heappop(jew)[1]) #jew를 뺴고 뺸 jew의[0][1]을 jew_pos에 넣음
- 가장 가벼운 무게의 가방에 들어간다는 건 다른 가방에 들어갈 수 있으므로 이 데이터를 계속 활용.
- 답을 구할 때는 값이 높은 것이 중요하므로 push할 때 부호를 바꾸어서 넣으면 값이 큰 것부터 출력 가능

### 15089: 펠린드롬 분할
- 펠린드롬을 할 때 mid값을 기준으로 해야 이전 펠린드롬을 사용하기 용이한 것을 간과하고 dp를 사용함(펠린드롬 경우의 수에서는 dp를 사용하지 않았음)
- dp[2500] dp[i+1] = min((dp[i]+1),dp[i+1-k]+1) k=arr[i+1-k][i+1]이 펠린드롬이 되는 수
- 펠린드롬의 좌표 또한 dp로 구해야 시간 초과가 안남, 펠린드롬 구할 시 길이가 짝수인 것과 홀수인 것 구별
- [*range(5)] = [0,1,2,3,4]
- 참고 숏코딩
```python
A = input()
n = len(A)
D = [*range(n+1)]
if A == A[::-1]:exit(print(1))
for i in range(n):
    for j in range(i+1, n+1):
        t = A[i:j]
        if t == t[::-1]:D[j] = min(D[j], D[i]+1)
print(D[-1])
```
- ;는 줄넘기기 기능 있음

### 1562: 계단 수
- dp[i][j][1<<10]: j는 마지막 숫자, i는 사용한 계단 수, [1<<10]은 bitmasking을 이용하여 사용한 계단 숫자를 확인

## 1620: 나는야 포켓몬 마스터 이다솜
- key-value 문제
- value를 통해 key를 얻고 싶으면 역함수 만들어놓기
- sys.stdin.readline()은 줄 단위로 받아와서 개행문자 제거 필수

### 1644: 소수의 연속합
- 에라토스테네스의 체

### 1766: 문제집
- 우선순위 큐를 이용해서 먼저 풀 문제를 뺴고, 이걸로 다시 풀 수 있게 되는 문제를 집어넣는 방식
- 발상: 먼저 풀 문제는 가장 번호가 낮으면서, 먼저 풀 문제가 없어야 하는 것-->어떻게 먼저 풀 문제가 있는지 없는지 확인할 것인가. 문제 풀 때마다 바뀌는데 -->문제를 풀 때마다 먼저 풀 수 있는 문제인지 확인하기
### 1799: 비숍
- 체스에서 비숍은 검은색 판만/흰색 판만 가능함--> counting 개수를 1/2개로 줄일 수 있음
- 홀/짝에 따라서 체스판 규칙이 달라짐-->짝수개 판은 홀수개 판으로 변환

### 2098: 외판원 순회
- e다시 풀기

### 2143: 두 배열의 합
- '부 배열' 개념을 읽지 않고 품

### 2162: 선분 그룹
- CCW를 통해 선분이 일치하는지 확인
- Unionfind를 통해 그룹 묶기

### 2239: 스도쿠
- 숏코딩: https://www.acmicpc.net/source/49110487
```python
import sys
arr = [list(map(int, input())) for _ in range(9)]
def fun(cnt, arr):
    if cnt == 81:
        for nums in arr:
            for num in nums:
                print(num, end="")
            print()
        sys.exit()
    i = cnt // 9
    j = cnt % 9
    if arr[i][j] !=0:
        fun(cnt+1,arr)
        return
    temp = set(arr[i])
    for t in range(9):
        temp.add(arr[t][j])
    for a in range(i//3*3, i//3*3+3):
        for b in range(j//3*3, j//3*3+3):
            temp.add(arr[a][b])
    temp = set([1,2,3,4,5,6,7,8,9]) - temp
    for t in temp:
        arr[i][j] = t
        fun(cnt+1, arr)
    arr[i][j]=0

fun(0, arr)
```
- 코드 차이점: 행과 열을 i,j를 따로 관리하는 대신 cnt//9, cnt%9로 나누어 간결해짐
- split()쓰면 strip() 쓸 필요 없음. strip 쓰면 숫자가 한 글자씩 묶임
- ex) arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(9)]

### 2252: 줄 세우기
- '1766 문제집'에서 우선순위 큐가 필요 없는 것

### 2342: Dance Dance Revolution
- dp[i][j][10000]: 250000개 이므로 dp로 채우기
- 사고: dp를 쓸 수 있는 이유: 중간 상태 필요 없이 최종 발 상태와 최소 힘 상태가 중요.
### 2407: 조합
- comb(*map(int, sys.stdin.readline()))에서 *를 써야 값으로 반환되서 나옴
### 2447: 별 찍기-10
- 재귀로 풀려고 했ㅇ나생각이 안 나서, 빈 칸을 만드는 거 이용

### 2568: 전깃줄 -2
- binaryserch 코드 복습하기(st=-1 ed=len(x) while st+1 < ed), 발상할 떄는 홀홀 홀짝 짝홀 짝짝 경우와 몇 차이나는 지 생각하기

### 2623: 음악 프로그램
- '1766'문제집에서 불가능한 케이스를 찾는 것 추가

### 2887: 행성 터널
- 좌표 뺴서 값 구하기: 마지막과 첫번째 거도 빼서 구해야 함--> 최소 스패닝 트리(unionfind)
- 숏코딩 일부(https://www.acmicpc.net/source/18052822)
```python
for k in range(3):
    nl.sort(key=lambda x: x[k])
    for i in range(N-1):
        ml.append([abs(nl[i][k] - nl[i+1][k]), nl[i][3], nl[i+1][3]])
```
- 차이점: for 문을 이용하여 비용을 한번에 처리함

### 7579: 앱
- N(앱 개수)*cost총합 으로 array를 만들고 dp를 이용해서 각 cost를 이용해 최대로 비울 수 있는 공간 저장
- N*M(모든 앱 메모리 합)으로 만들고 cost를 최소화하는 dp를 만드는 건 가능한지 구현해보기

### 9252: LCS2
- 최장 부분 공통 수열 문제: dp를 이용해서 마지막거 같으면 (i-1,j-1)값에 문자 추가, 다르면 이전 값(i,j-1),(i-1,j)중 큰 것

### 9328: 열쇠
- BFS를 이용한 탐색. 열쇠를 찾으면 초기화, 보물 찾으면 체크
- 함수 안에서 새로 같은 이름의 list를 만들면 local이 되므로 함수 안에 list를 넣어줘야 오류가 발생하지 않음

## ***BFS와 DFS를 적용하는 차이 공부하기

### 9466: 텀 프로젝트
- 우선순위 큐를 이용하기, cycle이 있으면 cnt가 1이라 못나오고 cycle이 없으면, 결국에는 나와짐

### 10172: 개
- 특수문자의 출력: 앞에\ 추가히기

### 10815 숫자 카드
- 피드백 x

### 10775: 공항
- 최대한 큰 번호에 비행기를 도킹시키는 방식: Unionfind 이용. doking하면 parent 1 감소되 므로, union(a,find(a)-1)을 이용함

### 11725: 트리의 부모 찾기
- dict를 이용한 코딩. get: 없으면 none값 반환
```python
import sys
sys.setrecursionlimit(1000000000)

def dfs(n):
    for i in d[n]:
        if not ret.get(i, 0):
            ret[i] = n
            dfs(i)
        

N = int(input())
d = dict()
ret = dict()
for i in range(N - 1):
    a, b = map(int, input().split())
    d[a] = d.get(a, []) + [b]
    d[b] = d.get(b, []) + [a]

dfs(1)
for i in range(2, N + 1):
    print(ret[i])
```
### 11729: 하노이
- f(n-1)과 f(n)의 차이는 f(n)을 1에서 3으로 옮기고 f(n-1)을 1에서 3이 아닌 2에서 3으로 옮긴다는 차이
-->f(n,st,ed)=f(n-1,6-st-ed, ed)+f(1,st,ed)+f(n-1,st,6-ed-st)을 이용한 재귀 사용

### 12100: 2048
- 움직이는 방향에 따라 함수를 다르게 사용하는 것이 아니라 행렬을 옮겨서 사용
--> 행렬 옮기기-->왼쪽으로 모으기 방식으로 dfs, 다음 dfs를 들어가기 전에 copy
- 한 번에 여러 번 합쳐질 수 있다는 것을 못 봐서 늦게 품
- 2차원 최댓값: max = max([max for i in range A])
- roate를 각각 만들었으나, 숏코딩에서는 dfs-->90도 회전 반복문으로 진행함

### 12850: 본대 산책2
- 한 지점에서 다른 지점으로 가는 경로의 수는 두 행렬의 곱 성분이라는 것을 까먹었음

### 13560:구슬 탈출2
- 두 구슬을 다른 구슬이 없다고 생각하고 움직인 뒤에 겹칠 경우 기존 좌표가 무엇인지에 따라 계산하는 방식
- 숏코딩에서는 cnt를 이용하여, 4 방향을 구분할 필요가 없게 함

### 14003: 가장 긴 증가하는 부분 수열 5
- 2568 전깃줄-2와 일치

### 14425: 문자열 집합
- 문제 조건이 애메해서 두 가지 케이스를 테스트 해봄

### 14939: 불 끄기
- 가장 위에 경우의 수 2*10
- 그 다음에 위에 있는 것을 끄는 방법은 밑에 전구밖에 없는 것을 이용

### 15650: N과 M(2)
- 숏코딩: https://www.acmicpc.net/source/30572635
```python
from itertools import combinations

n, m = map(int, input().split())
for elem in combinations(range(1, n+1), m):
  print(*elem)
```
- 제너레이터와 yield 활용: https://juhee-maeng.tistory.com/91
### 16724: 피리 부는 사나이
- 모든 시작점은 cycle로 마무리 되거나 cycle 안으로 들어간다---> 사이클 당 1개의 safe 존이 있다

### 16946: 벽 부수고 이동하기 4
- 각 점에 대해 dfs를 통해 점의 개수를 센 후 벽을 깨고 상하좌우 개수+1을 해준다. 다만 겹치는 점을 확인하기 위해 동선에 cnt를 넣어준다

### 17143: 낚시왕
- 시키는 대로 구현, 방향 맞추는 조건 맞추기 어려웠음

### 17387: 선분 교차 2
- 두 선분이 일치하는 경우에는 따로 처리해야 한다는 것을 고려하지 못함
#### CCW 
- https://gaussian37.github.io/math-algorithm-ccw/ 참고
- 외적을 통해 결과가 음수면 시계뱡향, 양수면 반시계방향으로 벡터를 통해 방향을 구하는 방법

### 17404: RGB거리 2
- dp 이용. 마지막 점만 주의

### 20040: 사이클 게임
- 유니온 파인드 이용