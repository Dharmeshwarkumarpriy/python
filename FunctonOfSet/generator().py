def mycard():
    yield 'f'
    yield 'cdsd'
    yield 'b'

g=mycard()
print(next(g))
print(next(g))
print(next(g))