def add(x,y):
    z=x+y
    return z
print(add(4,7))
print('='*100)

def lesson(a,b):
    c='在{}年级，上{}课'.format(a,b)
    return c
print(lesson(2,'语文'))
print(lesson(b='数学',a=2))

print('='*100)


#默认参数
def study_language(name,language='python'):
    info = ("{}要学习{}语言".format(name,language))
    return info
print(study_language('张三','java'))
print(study_language('李四','python'))
print(study_language('王五'))

#可变化参数
def sum1(a,b,*c):
    # print(c)
    z=a+b+sum(c)
    return z
print(sum1(1,2))
print(sum1(1,2,3))
print(sum1(1,2,3,4,5,6))


def sum2(**d):
    print(d)
    return d
print(sum2(a='x',b='y',c='z'))