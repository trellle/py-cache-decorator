from typing import Callable, Any


def cache(func: Callable) -> Callable:
    my_store = {}

    def wrapper(*args) -> Any:
        if str(func) in my_store and str(args) in my_store[str(func)]:
            print("Getting from cache")
            return my_store[str(func)][str(args)]
        print("Calculating new result")
        result = func(*args)
        if str(func) in my_store and str(args) not in my_store[str(func)]:
            my_store[str(func)].update({str(args): result})
        else:
            my_store.update({str(func): {str(args): result}})
        return result
    return wrapper
