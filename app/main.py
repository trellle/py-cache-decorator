from typing import Callable


def cache(func: Callable) -> Callable:
    my_store = {}
    def wrapper(*args):
        flag = True
        for arg in args:
            if isinstance(arg, (list, dict, set, Callable)):
                flag = False
                break
        if flag:
            if str(func) in my_store and str(args) not in my_store[str(func)]:
                print("Calculating new result")
                result = func(*args)
                my_store[str(func)].update({str(args): result})
                return result
            elif str(func) in my_store and str(args) in my_store[str(func)]:
                print("Getting from cache")
                return my_store[str(func)][str(args)]
            elif str(func) not in my_store:
                print("Calculating new result")
                result = func(*args)
                my_store.update({str(func): {str(args): result}})
                return result
    return wrapper
