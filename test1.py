# # 从文件中读取数据，返回的是列表数据
# def from_file_get_data(file_name):
#     f=None
#     try:
#         f=open(file_name,'r')
#         line=f.readline()
#         user_data=eval(line)
#         return user_data
#
#     except Exception as e:
#         print(e)
#
#     finally:
#         if not f:
#             f.close()
#
#
# if __name__ == '__main__':
#     print(from_file_get_data('data.txt'))
#     print(type(from_file_get_data('data.txt')))
#
import unittest
from demologin2 import login

class TestLogin(unittest.TestCase):
    def test_login_success(self):
        except_values=0
        actually_values=login('admin','admin').get('code')
        self.assertEqual(except_values,actually_values)
# case1 : 输入正确的用户和正确的密码进行登录

# case2 : 输入错误的用户名或密码登录

# case3 : 输入空的用户或密码登录

if __name__ == '__main__':
    unittest.main()





