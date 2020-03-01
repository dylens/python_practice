import math

print(list(filter(lambda x: math.sqrt(x) % 1 == 0, [x for x in range(1, 101)])))

b = [4, 5, 6]
c = [7, 9, 3, 1, 8]
zi = zip(b, c)
lb, lc = zip(*zip(b, c))
print(lb)
print(lc)

print(ord('a'))
print(chr(ord('a')))
print(ord('♠'))
print(chr(ord('♠')))

# bytes 函数返回一个新的 bytes 对象，该对象是一个 0 <= x < 256 区间内的整数不可变序列。它是 bytearray 的不可变版本。
# b'hello'
print(bytes('hello', 'ascii'))

print("{:.2f}".format(3.1415926))
print("{:+.5f}".format(-3.1415926))
print("{:*>+15d}".format(-3))
print("{:>+15d}".format(-3))
print("{:.4%}".format(0.36259861))
print("{:.1e}".format(0.000000000036259861))

print("{:d}".format(20))
print("{:b}".format(20))
print("{:o}".format(20))
print("{:x}".format(20))
print("{:#x}".format(20))
print("{:#X}".format(20))

# 先按照score降序，再按照名字升序
d1 = [{'name': 'alice', 'score': 38}, {'name': 'bob', 'score': 18}, {'name': 'darl', 'score': 28},
      {'name': 'christ', 'score': 28}]
print(sorted(d1, key=lambda x: (-x['score'], x['name'])))

x = set('81080')
y = set('037')
print(x, y)
print(x & y)  # 交集
print(x | y)  # 并集
print(x - y)  # 差集
