#name
#bases
#dict
std = type('Student', (object,), dict(name='John', age=12))
print(std.name)
print(std.age)

print(type(std))
print(std.__name__)
print(std.__bases__)
print(std.__dict__)
