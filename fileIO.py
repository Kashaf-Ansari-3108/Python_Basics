s = 'Kashaf is a good girl'

#Writing
# with open('test.txt', 'w') as f:
#     f.write(s)

# fp = open('test.txt', 'w')
# fp.write(s)
# fp.close()

#Reading
# with open('test.txt', 'r') as f:
#     s = f.read()
#     print(s)

# fp = open('test.txt', 'r')
# s = fp.read()
# print(s)
# fp.close()

#Appending
with open('test.txt', 'a') as f:
    f.write(' also nice girl')

