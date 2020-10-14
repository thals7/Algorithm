# 부스트캠프 자가진단 테스트 문제 : 함수 구현
# 자연수가 들어있는 배열 arr가 매개변수로 주어짐.
# 배열 arr 안의 숫자들 중에서 앞에 있는 숫자들부터 뒤에 중복되어 나타나는 숫자들 중복 횟수를 계산해서 배열로 return하도록 solution함수를 완성하라.
# 만약 중복되는 숫자가 없다면 -1을 채워서 return하라.

arr = list(map(int,input().split()))
list = []
for i in range(1,max(arr)+1):
    if arr.count(i)>1:
        list.append(arr.count(i))
if len(list) == 0:
    print([-1])
else:
    print(list)