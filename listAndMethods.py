l1 = [1113, 3,5,234,234,24, 'kashf']

print(type(l1))
print(l1)

#Methods
l1.remove('kashf')
print(l1.count(234))
l1.sort()
l1.pop()
l1.append(78)
# l1.clear()
l1.extend([89, 73])
print(l1)
print(l1[0:4])
l1[0] = 'Kashaf'
print(l1)