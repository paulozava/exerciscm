shoes = int(input())
shoes_size = input().split()

cashier = 0
for _ in range(int(input())):
    size, value = tuple(input().split())
    if size in shoes_size:
        shoes_size.remove(size)
        cashier += int(value)

print(cashier)


# default dict

from collections import defaultdict

d = defaultdict(list)

a_group, b_group = tuple(map(int, input().split()))
for i in range(a_group):
    letter = input()
    d[letter].append(i+1)

for item in [input() for _ in range(b_group)]:
    print(d[item])

# named tuple

from collections import namedtuple

class_number = int(input())
tags = input()
Students = namedtuple('Students', tags)
marks_sum = 0
for _ in range(class_number):
    temp = Students(*input().split())
    marks_sum += int(temp.MARKS)
print(marks_sum / class_number)

# order dict

from collections import OrderedDict

number = int(input())
dic = OrderedDict()

for _ in range(number):
    stdin = input().split()
    price = int(stdin.pop())
    key = ' '.join(stdin)
    if key not in dic:
        dic[key] = 0
    dic[key] += price

for key, value in dic.items():
    print(f'{key} {value}')

# deque

from collections import deque

deq = deque()
for _ in range(int(input())):
    action = input()
    if 'append' in action :
        target = action.split()
        deq.append(target[-1])
    elif 'appendleft' in action:
        target = action.split()
        deq.appendleft(target[-1])
    elif 'pop' in action:
        deq.pop()
    elif 'popleft' in action:
        deq.popleft()
print(' '.join(deq))

# calendar

from datetime import datetime
from calendar import day_name

strdate = input()
dt = datetime.strptime(strdate, '%m %d %Y')
print(day_name[dt.weekday()])


# exception

for _ in range(int(input())):
    try:
        a, b = tuple(map(int, input().split()))
        print(a / b)
    except Exception as e:
        print(f'Error Code: {e}')


# re exception
from re import compile

try:
    compile('')
    print(True)
except:
    print(False)


# any all
evaluate = input().split()
test = all(map(lambda x: int(x)>0, evaluate)) and any(map(lambda x: x == x[::-1], evaluate))
print(test)

# angle
hyp = (AB**2 +BC**2)**0.5/2
heightSin = AB/2
angle = math.asin(heightSin/hyp)
print("degrees",round(math.degrees(angle)))

# float
isinstance(eval('+4.54'), float)

# re group
import re

pat = r'(\w+)\1'
a = '..12345678910111213141516171820212223'
res = re.findall(pat, a)

pat = r'([^+\-, ])([aeiouAEIOU]{2,})([^+\-, ])'

# find span
import re

seek = input()
pattern = r'(?=({}))'.format(input())

if re.search(pattern, seek):
    for found in re.finditer(pattern, seek):
        s, e = found.span(1)
        print((s, e-1))
else:
    print((-1, -1))

# validate number
# 2
# 9587456281
# 1252478965
import re

for _ in range(int(input())):
    if re.search('[789]\d{9}', input()):
        print('YES')
    else:
        print('NO')


import re

pattern = r'<[a-z][\w\-\.]*@[\w]+\.[\w]{1,3}>'

for _ in range(int(input())):
    email = input()
    if re.search(pattern, email):
        print(email)

# re uid

# It must contain at least 2 uppercase English alphabet characters.
quint = len([s for s in seek if s.isupper()]) >= 2
# It must contain at least 3 digits ( - ).
quart = len([s for s in seek if s.isdigit()]) >= 3
# It should only contain alphanumeric characters ( - ,  -  &  - ).
third = seek.isalnum()
# No character should repeat.
second = len(set(seek)) == len(seek)
# There must be exactly  characters in a valid UID.
first = len(seek) == 10
if first and second and third and quart and quint:
    print('Valid')
else:
    print('Invalid')


import re

seek = input()
pattern = r'( )(#([0-9a-fA-F]{6}|[0-9a-fA-F]{3}))'
if re.search(pattern, seek):
    for found in re.finditer(pattern, seek):
        print(found.group(2))



A = set([1, 2, 3])
A.update(action)
A.intersection_update(action)
A.symmetric_difference_update(action)
A.difference_update(action)

A.remove()