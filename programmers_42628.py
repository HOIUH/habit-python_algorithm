# 221113
# 힙(Heap) > 이중우선순위큐
# https://school.programmers.co.kr/learn/courses/30/lessons/42628

# heapq 안 쓰는 게 더 나은 듯
def solution(operations):
    answer = []

    for operation in operations:
        tmp = operation.split()
        command, data = tmp[0], tmp[1]

        if command == 'I':
            answer.append(int(data))
        else:
            if answer:
                if data == '1':
                    mx = max(answer)
                    answer.remove(mx)
                else:
                    mn = min(answer)
                    answer.remove(mn)

    if not answer:
        return [0, 0]
    else:
        mx, mn = max(answer), min(answer)
        return [mx, mn]


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
