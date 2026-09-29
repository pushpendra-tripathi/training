def cache(fn):
    '''
    cache function
    '''
    results = {}

    def wrapper_func(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key not in results:
            results[key] = fn(*args, **kwargs)
        return results[key]

    return wrapper_func