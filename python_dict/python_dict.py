#!Anaconda/anaconda/python
#coding: utf-8

# 字典，dictionary，在其他语言中多称为map。使用【键-值】对存储
# dictionary内部存放顺序和key的放入顺序没有关系
# 优点：查找速度快。不会因为key的增加变慢
# 缺点：浪费内存较多，字典是一种用空间换时间的方法

dict = {'tom':95, 'bob':60, 'jack':50}
print(dict['tom'])

# 通过key增加字典的内容
dict['andrew'] = 10
print(dict)

# 一个key只能对应一个value
dict['andrew'] = 90
print(dict)

# 判断key是否在字典中，两种方法
print('andrew' in dict)
print(dict.get('marry', -1))

# 删除一对键值
dict.pop('andrew')
print(dict)

# 注意：dictionary的key必须是不可变对象
# 因为dictionary使用哈希算法，利用key来计算value的存储位置
# truple是不可变对象，可以作为key
t = ('a', 'b')
dict[t] = 'test'
print(dict)

# ---dictionary和list比较---
# list查找和插入的速度随元素的增加而增加
# list占用空间少，浪费内存小

print('='*40)
# ===========================================
# 集合，set，和dictionary类似，是一组key的集合，但是不存储value
# key不能重复，重复元素会被自动过滤
# 需要提供一个list作为输入集合
mySet = set([1, 2, 3])
print(mySet)

mySet.add(5)
print(mySet)

mySet.remove(5)
print(mySet)

# set可以看成数学上无序和无重复元素的集合
# 两个set可以做集合的【交集】，【并集】
s1 = set([1, 2, 3])
s2 = set([1, 2, 5])
print('s1 & s2:', s1 & s2)
print('s1 | s2:', s1 | s2)