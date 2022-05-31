from demologin2 import login
import unittest
import sys
from Test_package.HTMLTestRunner import HTMLTestRunner #导入HTMLTESTRUNNER包

class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        print('开始运行方法',sys._getframe().f_code.co_name)

    def tearDown(self) -> None:
        print('结束运行方法', sys._getframe().f_code.co_name)


    #测试用例1：输入正确的用户和正确密码进行登录
    def test_login_success(self):
        except_values=0
        actual_values=login('admin','admin').get('code')
        self.assertEqual(except_values,actual_values)

    # 测试用例2：输入错误的用户和或密码进行登录
    def test_login_wrong(self):
        except_values = 1
        actual_values = login('22admin', 'admin').get('code')
        self.assertEqual(except_values, actual_values)


    # 测试用例3：输入空的用户或密码进行登录
    def test_login_password_isnull(self):
        except_values = 1
        actual_values = login('0', 'admin').get('code')
        self.assertEqual(except_values, actual_values)

if __name__ == '__main__':
    # 创建一个套件a
    suite_a = unittest.TestSuite()
    suite_a.addTest(TestLogin('test_login_success'))
    suite_a.addTest(TestLogin('test_login_wrong'))
    suite_a.addTest(TestLogin('test_login_password_isnull'))
    print(suite_a)

    runner = unittest.TextTestRunner()
    runner.run(suite_a)