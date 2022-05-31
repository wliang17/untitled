from demologin2 import login
import unittest
import sys
from Test_package.HTMLTestRunner import HTMLTestRunner #导入HTMLTESTRUNNER包

class TestLogin(unittest.TestCase):



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

    #创建一个测试报告文件，是html格式的
    test_report='./test_report.html'


    with open(test_report,'wb') as f: #用with方法打开文件，并自动关闭文件,其中wb为显示二进制，否则乱码报错


        # runner = unittest.TextTestRunner()   #原先的runner运行器
        runner = HTMLTestRunner(f,title='测试报告',description='测试报告描述')

        runner.run(suite_a)