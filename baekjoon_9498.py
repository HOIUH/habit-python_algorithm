#20220410

score = int(input())

while score < 0 or score > 100:
    print('시험 점수는 0 이상 100 이하의 정수입니다')
    score = int(input())

    if score >= 0 and score <= 100:
        break

if score >= 90 and score <= 100:
    print('A')
elif score >= 80 and score < 90:
    print('B')
elif score >= 70 and score < 80:
    print('C')
elif score >= 60 and score < 70:
    print('D')
else:
    print('F')

