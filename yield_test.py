def h():
    print("test")
    yield  5
    print('if')
    yield 6
    yield 7
c = h()
print(c.next()) # just like c.send(None) method to ask next value
print(c.send("mm"))
print(c.next())

try:
    print(c.next())
except StopIteration:
    print('no more')
    pass
