# 列表list是Python内置的一种数据类型
# list是一种有序的集合,可以随时添加和删除其中的元素

my_list = ['a','b','c']
print(my_list)

my_list.append('d')
print(my_list)

my_list.insert(0, 'start')
print(my_list)

my_list.pop(1)
print(my_list)

# list元素可以包含另一个list
s = ['a','b',['tom','jack'],'c']
# s[2]又是一个list,但是在s中,他只是一个元素
print(len(s))

# =========================================

# tuple,元组,Python中的另一种有序列表.
# tuple一旦初始化后,就无法修改,使代码更安全.
my_tuple = ('a','b','c')
print(my_tuple)

# 定义只含一个数字元素的tuple时,后面加上逗号,避免歧义.
# 如果没有逗号,解释器会认为这是数值变量的定义
t = (9,)

# 当tuple中含有list的时候,这个tuple是 [可变] 的
t = ('a','b',['A','B'])
print(t)
t[2][0] = 'X'
print(t)

# tuple所谓的[不变],是指tuple每个元素的指向永远不变.
# 上面的 t[2] 指向一个list,就不能改变为指向其他的元素.
# 但是那个list本身是可以变的.