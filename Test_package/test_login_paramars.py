from demologin2 import login
import unittest
import sys
from parameterized import parameterized
#导用参数化包


lst_data=[(0,'admin','admin'),(0,'user','123456'),(1,'admin','123456')]
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        print('开始运行方法',sys._getframe().f_code.co_name)

    def tearDown(self) -> None:
        print('结束运行方法', sys._getframe().f_code.co_name)


    #测试用例1：输入正确的用户和正确密码进行登录
    @parameterized.expand(lst_data) #先加装饰器
    def test_login(self,except_values,username,password):

        actual_values=login(username,password).get('code')
        self.assertEqual(except_values,actual_values)

if __name__ == '__main__':
    unittest.main()

