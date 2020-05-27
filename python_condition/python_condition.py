# Python条件判断
# if 语句从上往下执行,如果有一个条件成立,其他自动忽略.
# 注意input()函数返回的数据类型是 str
# 在做条件判断时,需要进行数据转换
age = 0
# s = input('input your age: ')
# age = int(s)

if age >= 18:
    print('adult')
elif age >= 6:
    print('teen')
elif age >= 2:
    print('kid')
else:
    print('baby')

# 条件判断的简写
# 只要 x 是非零数值/非空字符串/非空列表,就为True
x = ['andrew']
if x:
    print('True')

# =================================
# Python循环

# 第一种: for x in y: 循环
# 依次把y中的每个元素取出代入变量x中,然后执行后面的语句
y = list(range(1, 11))
print(y)

sum = 0
for x in y:
    sum += x
print(sum)

# 第二种: white: 循环
n = 10
sum = 0
while n > 0:
    sum += n
    n -= 1
print(sum)

# break 可以在while中直接退出整个循环
n = 1
while n < 10:
    print(n)
    n += 1
    if n > 5:
        break
print('END')

# continue 直接跳过当前循环,开始下一次循环
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print(n)
print('END')
