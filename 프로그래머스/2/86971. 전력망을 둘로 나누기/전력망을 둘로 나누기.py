from collections import deque

def solution(n, wires):
    answer = n

    for cut in range(len(wires)):
        graph = [[] for _ in range(n + 1)]

        # 1) 그래프 만들기 (cut 간선 제외) — 여기까지만!
        for i, (a, b) in enumerate(wires):
            if i == cut:
                continue
            graph[a].append(b)
            graph[b].append(a)

        # 2) BFS는 그래프 완성 후에 "딱 한 번"
        queue = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True
        cnt = 1

        while queue:
            cur = queue.popleft()
            for nxt in graph[cur]:
                if not visited[nxt]:
                    visited[nxt] = True
                    cnt += 1
                    queue.append(nxt)

        # 3) 차이 계산
        diff = abs(cnt - (n - cnt))
        answer = min(answer, diff)

    return answer