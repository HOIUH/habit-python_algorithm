# 20220501
# 다이얼
# https://www.acmicpc.net/problem/5622

alphabet = 'ABC DEF GHI JKL MNO PQRS TUV WXYZ'
alphabet_list = list(alphabet.split())

input_str = input().upper()

# ABC  DEF  GHI
# 0    1    2
# 3초  4초   5초

result = 0
for val in alphabet_list:
    v_cnt = 0
    for v in val:   # alphabet_list 에서 각 요소를 꺼내어 한 글자씩 분리
        v_cnt = input_str.count(v)  # 분리한 알파벳이 입력값에서 총 몇개 있는지 세기
        result += (alphabet_list.index(val) + 3) * v_cnt    # 분리한 알파벳이 속한 요소의 인덱스에 +3 한 뒤,
                                                            # 개수만큼 곱하기

print(result)
