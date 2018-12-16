from collections import namedtuple
City = namedtuple('City', 'name country population coordinate')
tokyo = City('Tokyo' ,'JP', 36.933, (35.689722, 139.691667))

print(tokyo)
print(tokyo.name)
print(tokyo.coordinate)
print(tokyo[1])

