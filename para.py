import functools
import yaml

def decorator(func):
    @functools.wraps(func)
    def wrapped(*args):
        list = [*func(*args)]
        with open('list.yaml', 'w') as f:
            yaml.dump(list)
            print(yaml.dump(list))
        return list
    return wrapped

