def foo(**kwargs):
    print(kwargs)
    return kwargs

foo(c=1, b="a", a=4)