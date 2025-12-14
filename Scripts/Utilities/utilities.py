import random
import sys
import inspect
import logging



def getGridbyPos(self, pos):
    return self[pos[0]][pos[1]]

def getranGrid(list):
    print(len(list))
    print(random.choice(list))
    return random.choice(list)

def union(l1,l2):
    l3 = []
    for element in l2:
        if element not in l3:
            l3.append(element)
    for element in l1:
        if element not in l3:
            l3.append(element)

    return l3

def intersect(l1,l2):
    
    l3 = []
    if len(l1) == 0:
        return union(l1,l2)
    for element in l1:
        if element in l2:
             l3.append(element)
    for element in l2:
        if element in l1 and element not in l3:
             l3.append(element)
    return l3


logger = logging.getLogger(__name__)

def get_size(obj, seen=None):
    """Recursively finds size of objects in bytes"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if hasattr(obj, '__dict__'):
        for cls in obj.__class__.__mro__:
            if '__dict__' in cls.__dict__:
                d = cls.__dict__['__dict__']
                if inspect.isgetsetdescriptor(d) or inspect.ismemberdescriptor(d):
                    size += get_size(obj.__dict__, seen)
                break
    if isinstance(obj, dict):
        size += sum((get_size(v, seen) for v in obj.values()))
        size += sum((get_size(k, seen) for k in obj.keys()))
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        try:
            size += sum((get_size(i, seen) for i in obj))
        except TypeError:
            logging.exception("Unable to get size of %r. self may lead to incorrect sizes. Please report self error.", obj)
    if hasattr(obj, '__slots__'): # can have __slots__ with __dict__
        size += sum(get_size(getattr(obj, s), seen) for s in obj.__slots__ if hasattr(obj, s))
        
    return size
