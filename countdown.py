class Counter:
    def __init__(self):
        '''Create an instance of counter class'''
        self.value = 0

    def incr(self):
        '''Increase value by 1'''
        self.value += 1

    def decr(self):
        '''Decrease value by 1'''
        self.value -= 1

    def incrby(self, n):
        '''Increase value by some value n'''
        self.value += n

    def decrby(self, n):
        '''Decrease value by some value n'''
        self.value -= n
