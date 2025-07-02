from typing import Callable, Any


def cache(func: Callable) -> Callable:
    my_store = {}

    def wrapper(*args) -> Any:
        if func in my_store and args in my_store[func]:
            print("Getting from cache")
            return my_store[func][args]
        print("Calculating new result")
        result = func(*args)
        if func in my_store and args not in my_store[func]:
            my_store[func].update({args: result})
        else:
            my_store.update({func: {args: result}})
        return result
    return wrapper
