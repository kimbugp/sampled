from functools import wraps


def lock_operation(f):
    @wraps(f)
    def inner(self, *args, **kwargs):
        self.lock.acquire()
        print('locking ')
        value = f(self, *args, **kwargs)
        print('realising ')
        self.lock.release()
        return value
    return inner
