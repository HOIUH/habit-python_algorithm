# 220704
# 2022 KAKAO BLIND RECRUITMENT > 신고 결과 받기
# https://programmers.co.kr/learn/courses/30/lessons/92334

# 나의 풀이
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    declaration = {}    # 딕셔너리 (key, value 쌍)

    for r in report:
        key = r.split()[1]      # 신고당한 유저 ID
        value = r.split()[0]    # 신고한 유저 ID

        if key not in declaration:
            declaration[key] = set()    # value는 set에 담음 => 중복제거 위함

        declaration[key].add(value)

    # 딕셔너리는 리스트처럼 인덱스 접근이 안 됨
    # key로만 접근가능해서 enumerate와 .items() 사용함
    for i, (key, value) in enumerate(declaration.items()):
        if len(value) >= k:

            # set 타입은 not subscriptable 해서 for문 사용하려면 list로 형변환 해줘야함
            value = list(value)

            for j in range(len(value)):
                answer[id_list.index(value[j])] += 1

    return answer

# solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)