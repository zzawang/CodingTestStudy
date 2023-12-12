
from itertools import product
def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U', ""]
    my_dict = set()
    
    for p in product(alpha, repeat = 5):
        my_dict.add("".join(p))
    
    my_dict = sorted(my_dict)
    return my_dict.index(word)