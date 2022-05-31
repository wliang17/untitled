

#实例: 创建学生类，要求有属性：姓名和年级 ; 方法有：学习的方法，打印学生的上课情况
class Student():  #定义一个Student类
    name=''  #属性
    grade=''    #属性

    def study(self):   #定义方法（函数）
        print('学生{}在{}年级上课'.format(self.name,self.grade))

    def statu(self):
        print('{}年级学生{}正在上课睡觉'.format(self.grade,self.name))

s1=Student()
s1.name='张三'
s1.grade='4'
print(s1.study())
print(s1.statu())

s2=Student()
s2.name='刘备'
s2.grade='9'
print(s2.study())
print(s2.statu())

print('='*100)

# python类的构造方法使用 __init__() 方法来表示，每次调用类的时候会自动被调用 ，主要用来初始化数据。
class Student1():


    def __init__(self,name,grade):
        self.name=name
        self.grade=grade


    def study(self):
        x='{}年级的学生{}正在上课'.format(self.grade,self.name)

        return x

s3 = Student1('张飞',9)
print(s3.study())

print('='*150)


# # 14. 题目：打印出如下图案（菱形）:
# str1='*'
# alst1=[x for x in range(1,8,2)]
# alst1.extend(y for y in range(5,0,-2))
# for i in alst1:
#     print((str1*i).center(7))





