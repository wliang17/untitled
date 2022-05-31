# 练习：返回1~10之间的偶数
for i in range(1,6,1):
    i=2*i
    print(i)

print('=================')
# 创建一个元祖
tp1=()
tp2 = (1,2,12.22,'abc',True,None)
tp3 = (1)
print(tp1)
print(tp2)
print(tp3)


print('=================')
for x in (1,2,3,4,5,6,7,8,9,10):
    print(x)


print('=================')
# 创建字典
dict0 = {}
dict1 = {'1':1,'2':2,'3':3,'4':92.22,'5':'hello','6':False,'7':None}
print(dict0)
print(dict1)

print('字典中键为1的值：',dict1['1'])

# 更新字典dict1中键为1的值
dict1['1']=12
print('字典中键为1的值：',dict1['1'])

# 返回一个新字典
dict2 = {'a':1,'b':2}
# dict0 = dict1.fromkeys('a','b')
# print('返回一个新的字典',dict0)


# 查询字典一个值,键不存在时返回空值
print('查询字典中键为1的值',dict1.get('1'))
print('查询字典中键为1的值',dict1.get('0'))

# 判断键在不在字典里
print('1' in dict1)

print('===================')
#更新字典的内容:字典d2中增加dict1中的键值对
dict2.update(dict1)
print(dict2)

# 返回字典中所有的值 d.values
print('返回字典中所有键值对的值：',dict2.values())
for i in dict2.values():
    print(i)

###删除字典中某个键对应的值 d.pop()
dict2.pop('1')
print(dict2)