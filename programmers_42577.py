# 220910
# 해시 > 전화번호 목록
# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    # 나의 풀이에서 sort key를 기본으로 변경 => for문을 1번만 사용
    # 요소값 기준 오름차순 정렬하면 현재 인덱스와 다음 인덱스가 각각 가리키는 값만 확인하면 됨
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    return True

# 나의 풀이
# 정확성 테스트는 통과하지만, 효울성 테스트에서 시간 초과되는 풀이
'''
    phone_book.sort(key=len)

    for i in range(len(phone_book)):
        element = phone_book[i]
        for cmp_element in phone_book[i+1:]:
            if cmp_element.startswith(element):
                return False

    return True
'''

pb = ["567","12","123","1235","88"]
print(solution(pb))