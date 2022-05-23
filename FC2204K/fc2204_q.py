a = 0.0
b = 0
c = True
d = 12345
e = "False"
print(type(a), type(b), type(c), type(d), type(e))


a = "Kyobo Life helps people not to despair with their hardships in their lives."
print(a.count("L"))
print(a.count("l"))

a, b = 30, 30
if a < b:
    print("a < b")
elif a == b:
    print("a == b")


data1, data2 = "hello"
print(data1, data2)

b = [1, 2, [3, 4]]
b

data1 = "fast campus"
data2 = "kyobo"
data = data1 + ' X ' + data2
print(data)


ls = ["kyobo", "life", "best", "programing", "language"]
string = " ".join(ls)
string

a, b = 10, 30
if a > b:
    print("가")
elif a == b:
    print("나")
elif a < 20 and b < 10:
    print("다")
else:
    print("라")


QUERY = """
    INSERT INTO user(name, age)
    VALUES ('peter', 23), ('andy', 42);
"""
curs.execute(QUERY)


text = "Life is short, You need Python"
if "life"in text:
    print("A")
elif "short"in text:
    print("B")
elif "you" not in text:
    print("C")
elif "Python" in text:
    print("D")


data1, data2, data3, data4 = -2, 2.9, True, "True"
type(data1), type(data2), type(data3), type(data4)

for i in range(2, 10):
    for j in range(1, 10):
        print("%d X %d = %d" % (i, j, i * j))

list(range(0, 12, 2))

# 답확인
for number in range(0, 13, 2):
    if number % 3:
        continue
    print(number)
    if number >= 11:
        print(number)
        break

bool(1), bool(0), bool(2)

# 답확인
a = list(range(2, 7, 2))
b = [number for number in range(7) if number % 2]
c = [2, 4, 6]
d = list(set([4, 2, 6, 4, 6, 6, 4]))

a, type(a)
b, type(b)
c, type(c)
d, type(d)


print("True")

# 답확인
bool([])

years = list(range(2000, 2022))
2022 in years

not (2, 3) != (3, 2)

9 not in [num for num in range(9)]

bool([])
years = list(range(2000, 2022))
2022 in years
not (2, 3) != (3, 2)
9 not in [num for num in range(9)]
