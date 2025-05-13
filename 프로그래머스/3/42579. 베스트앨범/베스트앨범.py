from collections import defaultdict

def solution(genres, plays):
    genre_play_count = defaultdict(int)
    genre_song_list = defaultdict(list)
    
    # 1. 장르별 총 재생 횟수 및 노래 목록 저장
    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_play_count[g] += p
        genre_song_list[g].append((p, i))  # (재생 수, 고유번호)

    # 2. 장르를 총 재생 수 기준으로 정렬
    sorted_genres = sorted(genre_play_count.items(), key=lambda x: x[1], reverse=True)

    answer = []
    for genre, _ in sorted_genres:
        # 3. 해당 장르의 노래들을 재생 수 기준 내림차순, 같으면 고유번호 오름차순 정렬
        sorted_songs = sorted(genre_song_list[genre], key=lambda x: (-x[0], x[1]))
        # 4. 최대 2곡까지 수록
        answer.extend([song[1] for song in sorted_songs[:2]])
    
    return answer