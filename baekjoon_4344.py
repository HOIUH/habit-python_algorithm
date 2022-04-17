# 20220417
# 평균은 넘겠지
# https://www.acmicpc.net/problem/4344

cnt = int(input())

for i in range(cnt):
    input_list = []

    # TypeError: unsupported operand type(s) for /: 'int' and 'map' 에러 발생
    # input_list.append(map(int, input().split()))
    input_list = list(map(int, input().split()))

    # 평균 구하기
    avg = sum(input_list[1:]) / input_list[0]

    # 평균과 대소 비교
    student_cnt = 0
    for k in range(1, len(input_list)):
        if input_list[k] > avg:
            student_cnt += 1

    # 평균 넘는 학생수 비율 구하기
    # 소수점 셋째 자리까지 반올림
    rnd = round(student_cnt / input_list[0] * 100, 3)

    # 제출 시 틀린 결과라고 나옴옴
    #result = '%.3f' % rnd
    #print(result, '%')

    # f-string 은 파이썬 3.6 버전 이후부터 사용 가능
    # 문자열 지정하는 따옴표 앞에 f를 접두사로 붙임
    # 중괄호 {} 안에서 구분자 : 기준으로 왼쪽엔 문자 or 숫자를, 오른쪽엔 정렬 기호와 숫자 및 서식지정자 알파벳 써줌
    # 서식 지정자 => 문자열 s / 정수 d / 실수 f
    # 예) 글자 수 10개인 경우, 왼쪽 정렬 {문자:10s} / 가운데 정렬 {정수:^10d} / 오른쪽 정렬 {실수:>10f}
    print(f'{rnd:.3f}%')


