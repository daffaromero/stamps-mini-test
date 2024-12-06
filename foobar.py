list = []
for i in range(100, 0, -1):
    if i % 3 == 0 and i % 5 == 0:
        list.append("FooBar")
    elif i % 3 == 0:
        list.append("Foo")
    elif i % 5 == 0:
        list.append("Bar")
    else:
        list.append(i)

print(", ".join(map(str, list)))
