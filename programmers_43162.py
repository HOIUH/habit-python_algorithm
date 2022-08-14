# 220814
# 네트워크
# https://school.programmers.co.kr/learn/courses/30/lessons/43162

# 참고
# https://han-py.tistory.com/242 : [코딩테스트] 쉽게 이해하고 바로 쓰는 DFS (깊이 우선 탐색)
# https://kangsu-2ji.tistory.com/75

'''
1. 그래프 재귀로 DFS 구현
'''


def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]     # 방문플래그는 정점 개수 만큼 0으로 초기화

    def dfs(i):
        visited[i] = 1  # computers[i][i]인 경우도 1로 표시되므로 함수 호출하면 바로 방문플래그를 1로 변경

        for j in range(n):
            # i정점에 j정점과 연결된 간선 있는 경우 and j정점 아직 방문하지 않은 경우
            # dfs 재귀 호출
            if computers[i][j] and not visited[j]:
                dfs(j)

    for v in range(n):
        if not visited[v]:  # 한번도 방문한 적 없는 정점에 대해해 dfs 함수 호출
            dfs(v)
            answer += 1     # 연결된 정점들 다 돌고 오기 때문에 +1

    return answer
