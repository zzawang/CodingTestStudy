from collections import deque

def deep_copy(visited):
    new_arr = []
    for word in visited:
        new_arr.append(word)
        
    return new_arr

def can_be_next_step(find, word):
    not_matched = 0
    for index, letter in enumerate(find):
        if letter != word[index]:
            not_matched += 1
    
    return not_matched == 1
        
def solution(begin, target, words):
    q = deque([])
    q.append((begin, 0, [begin]))
    
    while q:
        find, count, visited = q.popleft()
        if find == target: # begin이 target에 도달한 경우
            return count
        for word in words:
            if word not in visited and can_be_next_step(find, word):
                new_visited = deep_copy(visited)
                new_visited.append(word)
                q.append((word, count + 1, new_visited))
        
    return 0