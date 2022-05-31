## 需求-迭代1：登录功能
# 1. 定义两条用户数据 ，要求用户数据的属性包括用户角色，用户账号，密码，部门

# 2. 要求返回的格式是字典形式 ，包含两个字段，code和message ,code为0代表成功，为1代表失败 ；
# message给出相应的提示 ，格式如 ：{'code':0,'message':'登录成功'}
# 3. 用户通过控制台输入用户名和密码，判断用户名和密码是否和定义数据中的用户名密码相匹配，
# 若匹配返回成功登录消息体，并把用户列表也追加到返回结果中,{'code':0,'message':'登录成功',user_list:[]}
# 4. 若用户名输入为空或密码输入为空，都给出对应的提示，如用户名不能为空
# 5. 若用户名或密码不匹配，都给出登录失败，请检查您的用户名或密码是否填写正确。提示


# ## 需求-迭代2：用户查询功能:
# 1. 用户查询功能必须是在登录以后才能调用 ，否则给出权限不足提示
# 2. 若输入的用户名正确，返回登录用户的信息，password字段不显示  。
# 3. 若输入的用户名不正确 ，给出无查询结果的提示
# 4. 查询支持模糊查询。

"""
## 需求-迭代3：用户新增功能:
1. 将默认用户数据放在文件中保存，以上迭代功能查询数据都要从文件查询 。
2. 需要对文件的读写进行异常捕获
3. 用户可以输入关键字add进行新增用户 ，新增的用户信息可以保存到文件中 。
4. 同时进行查询时，也能查询出该用户 。
5. 当用户添加成功时，在返回的结果中要创建时间。
"""

from datetime import datetime
from loguru import logger


# 方法 ：从文件中读取数据，返回的是列表形式的数据
def from_file_read_data(file_name):
    f=None
    try:
        f=open(file_name,'r')
        line=f.readline()
        user_data=eval(line)
        return user_data

    except Exception as e:
        print(e)

    finally:
        if not f:
            f.close()

# 方法 ：向文件中写入内容，用户添加的信息是在原来的基础上添加的。
def save_data(file_name,file_content):
    f=None
    try:
        f=open(file_name,'w')
        f.write(str(file_content))

    except Exception as e:
        print(e)

    finally:
        if not f:
            f.close()


# user_list = [{'role':'admin','account':'admin','password':'admin','dept':'teacher'},
#              {'role':'user','account':'user','password':'123456','dept':'student'}]
user_list=[]
user_list = user_list if user_list else from_file_read_data(r'D:\untitled\data.txt')
result={'code':'','message':''}

def login(user_name,user_password):


#实现用户名为空时的情况
    if user_name == '' or user_name is None:
        result.update({'code':1,'message':'用户名或密码不能为空,请重新输入'})
        return result

    if user_password == '' or user_password is None:
        result.update({'code': 1, 'message': '用户名或密码不能为空,请重新输入'})
        return result

    #实现用户名输入正确的情况
    for x in user_list:
        if user_name==x.get('account') and user_password==x.get('password'):
            result.update({'code': 0, 'message': '登录成功','user_list':user_list})
            return result

    #用户名或者密码输入错误的情况

    result.update({'code': 1, 'message': '登录失败，请检查您的用户名或密码是否填写正确'})
    return result


# 创建一个类 ，包括新增用户，修改用户，删除用例，查询用户
class User():

#用户查询功能
    def select(self,select_name):


    #判断用户是否登录，若登录成功可以进行查询 ；若登录失败，返回权限不足
        if result.get('code') !=0:

            result.update({'code':11,'message':'权限不足，请先登录。'})
            logger.info('日志信息{}'.format(result))
            return result

    # 输入正确用户名进行查询 ，返回结果 (支持模糊查询)

        else:
            # result.clear()
            lst=[] #定义一个空值用来存储查询到的信息
            for y in user_list:
                account=y.get('account')#用列表account来存储从user_list遍历的账户信息
                if select_name in account: #如果输入的用户名在account列表里，则可以表明搜索成功，实现模糊查询
                    y.pop('password')
                    lst.append(y)
            if lst:#如果lst不为空，则表明搜索不为空，输出搜索的内容
                result.update({'code':0,'message':'搜索成功','user_list':lst})
                return result

            result.update({'code':12,'message':'查询失败，该用户不存在,请重新输入'})
            return result

    def add(self,role,user_name,user_password,dept):
        user_dict={}
        user_dict={'role':role,'account':user_name,'password':user_password,'dept':dept}
        user_list.append(user_dict)
        save_data('data.txt',user_list)
        result.update({'message':'添加成功','add_time':datetime.now()})
        return result




if __name__ == '__main__':
    #进入循环，供用户操作
    flag=True
    while flag:

    #给用户选择接下来操作哪一步
        key=input(('请选择您的操作：'
              '\n 1) 进行登录'
              '\n 2) 进行查询用户'
              '\n 3) 进行新增用户'
              '\n q）退出操作'
              '\n 5) 未知操作，请重新输入\n'))
    #当用户输入其他字符时，返回上一步继续操作
        if key not in ('1','2','3','q','quit','exit'):
            print('='*100)
            continue

        if key == '1':
            user_name=input('请输入用户名:')
            user_password = input('请输入密码:')
            login_result=login(user_name,user_password)
            print(login_result)
            continue
        #
        if key == '2':
            user=User()#实例化对象
            select_name=input('请输入查询的用户名：')
            select_result=user.select(select_name)
            print(select_result)
            continue

        if key =='3':
            print(result)  # 测试专用，可以注销
            add_username = input('请输入您想添加的用户名：')
            user1=User()
            add_result=user1.select(add_username)

            # print(add_result) #调试时，看看返回的值是什么(可以注释注销)
            if add_result.get('code')==12:
                add_role=input('请输入您想添加的用户角色类别：')
                add_password = input('请输入添加的用户密码：')
                add_dept = input('请输入用户部门：')
                print('测试专用',user1.add(add_role,add_username,add_password,add_dept))#测试专用
                continue
            if add_result.get('code')==0:
                result.update({'code':0,'message':'用户名已存在，无法添加'})#原先代码为code是13，调试时发现，若添加用户失败后，继续选择3添加则显示权限不足，现在改为0试试
                print(result)
                print('*'*100)
                continue


        if key == 'q' or 'quit' or 'exit':
            flag=False
            print('退出成功')

#BUG说明：1、进入系统后，若直接按3进行新增用户，输入不存在的用户名，则会直接退出。若先登录再执行后面的就没问题。

















