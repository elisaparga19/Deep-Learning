import random
import numpy as np

index_list = list(range(0, 50, 1))
print(index_list)

def test(index_lst, mini):
    if len(index_lst) <= 5:
        mini.append(index_lst)
        return mini
    else:
        index_btch = random.sample(index_lst, 5)
        mini.append(index_btch)
        for element in index_btch:
            index_lst.remove(element)
        return test(index_lst, mini)
  
test = test(index_list, [])
print(len(test))