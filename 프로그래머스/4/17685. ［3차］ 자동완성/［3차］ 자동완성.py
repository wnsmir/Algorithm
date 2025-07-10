def solution(words):
    # 1) 사전 순 정렬
    words.sort()
    
    # 2) 공통 접두사 길이를 구하는 헬퍼
    def common_prefix_len(a, b):
        m = min(len(a), len(b))
        cnt = 0
        # 앞에서부터 한 글자씩 비교
        while cnt < m and a[cnt] == b[cnt]:
            cnt += 1
        return cnt
    
    total_input = 0
    n = len(words)
    
    for i, w in enumerate(words):
        # 이전 단어와의 LCP
        lcp_prev = common_prefix_len(w, words[i-1]) if i > 0 else 0
        # 다음 단어와의 LCP
        lcp_next = common_prefix_len(w, words[i+1]) if i < n-1 else 0
        
        # 더 긴 쪽 + 1 만큼 입력 (단어 길이 초과 금지)
        needed = min(len(w), max(lcp_prev, lcp_next) + 1)
        total_input += needed
    
    return total_input