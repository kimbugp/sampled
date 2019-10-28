from functools import wraps


def lock_operation(f):
    """Decorator to lock thread when called

    Args:
        f (func): function that  is called
    """
    @wraps(f)
    def inner(self, *args, **kwargs):
        self.lock.acquire()
        value = f(self, *args, **kwargs)
        self.lock.release()
        return value
    return inner
