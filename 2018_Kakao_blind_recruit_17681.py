# 220927
# 2018 KAKAO BLIND RECRUITMENT > [1차] 비밀지도
# https://school.programmers.co.kr/learn/courses/30/lessons/17681

'''
1. bin() 리턴 타입은 str
2. list(map(lambda 매개변수들: 식1 if 조건식 else 식2, str이나 list))
cf) https://dojang.io/mod/page/view.php?id=2360
3. string.rjust(문자열길이, 채울문자)
string.zfill(문자열길이) => '0'으로 채움
cf) https://alphahackerhan.tistory.com/55
'''

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a1, a2 = arr1[i], arr2[i]

        # 비트 연산자 OR 사용해서 두 수 자릿수 비교하여 하나만 1이여도 1 리턴
        after_or = bin(a1|a2)[2:]   # bin() 리턴 타입은 str

        # str 형식인 after_or 자릿수 하나씩 # or 공백으로 치환 -> rjust로 길이 부족한 결과는 맨앞에 공백 채우기
        result = ''.join(list(map(lambda x: '#' if x == '1' else ' ', after_or))).rjust(n, ' ')
        answer.append(result)
    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))
