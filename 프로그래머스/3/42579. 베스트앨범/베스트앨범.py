from collections import defaultdict

def solution(genres, plays):
    answer = []
    play_count = defaultdict(int)
    music_count = defaultdict(list)
    
    for index, (genre, play) in enumerate(zip(genres, plays)):
        play_count[genre] += int(play)
        music_count[genre].append((index, play))
    
    play_count = sorted(play_count.items(), key=lambda x:-x[1])
    for key, value in music_count.items():
        music_count[key] = sorted(value, key=lambda x:-x[1])
        
    for genre, play_sum in play_count:
        for index, _ in music_count[genre][:2]:
            answer.append(index)
    
    return answer