
# 连接字符串
astr='+'
bstr=astr.join('java')
print(bstr)

#分割字符串 split
cstr='java+python+php+sql'
dstr=cstr.split('+')
print(dstr)

#查找字符串str.find('x')，若查找到，返回最小索引值，否则返回-1
estr='hello world '
fstr=estr.find('l')
print(fstr)

gstr='hello world '
hstr=estr.index('l')
print(hstr)


#查找以xx结尾的字符串:str.endwith('xxx')
istr='hello world.doc'
if istr.endswith('.doc'):
    print('该文件是word文件')

#替换字符串：str.replace(new,old)
kstr='hello world'
lstr=kstr.replace('world','python')
print(lstr)
print('===============')
# 12. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

alpha=0
space=0
number=0
other=0
a=input('请输入一行字符：')
for i in a:
    if i.isalpha():
        alpha+=1
    elif i.isspace():
        space+=1
    elif i.isdigit():
        number+=1
    else:
        other+=1
print('其中字母个数为：',alpha)
print('其中空格个数为：',space)
print('其中数字个数为：',number)
print('其中其他字符个数为：',other)
