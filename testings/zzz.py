import sys
import tracemalloc as tm 

tm.start()

def deepgso(ob):
    size = sys.getsizeof(ob)
    if isinstance(ob, (list,tuple,set)):
        for element in ob:
            size+=deepgso(element)
    if isinstance(ob, dict):
        for k,v in ob.items():
            size+=deepgso(k)
            size+=deepgso(v)
    return size



list_=[[1],1,"1"]
print("Space consumed by the list using getsizeof:",sys.getsizeof(list_))
print("Total space consumed by the list:",deepgso(list_))

ss = tm.take_snapshot


print(ss)