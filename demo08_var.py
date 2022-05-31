# 封装、变量

# class Student():
#     name='曹操'
#     __score='80'
#
#     def __study(self,name,__score):
#         self.name=name
#         self.score=__score
#
#     def statu(self):
#         print('学生考试成绩为{}分'.format(self.__score))
#
# s1=Student()
#
# print(s1.statu())
#

#继承：父类，子类

class People():
    age=0

    def eat(self,people_type):
        print('{}在吃饭'.format(people_type))

class Student(People):
    pass

class Teacher(People):
    pass

s1=Student()

print(s1.eat('学生'))

s2=Teacher()

print(s2.eat('老师'))
