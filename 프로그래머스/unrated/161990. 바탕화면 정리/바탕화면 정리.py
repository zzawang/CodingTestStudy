def solution(wallpaper):
    answer = []
    lux = []
    luy = []
    
    for i1, v in enumerate(wallpaper):
        for i2, v in enumerate(v):
            if v == '#':
                lux.append(i1)
                lux.append(i1 + 1)
                luy.append(i2)
                luy.append(i2 + 1)
            
    return [min(lux), min(luy), max(lux), max(luy)]