from queue import Queue

class ThiefQueue(Queue):

    pass

instance = ThiefQueue(5)

def thief_queue():
    return instance

del ThiefQueue

