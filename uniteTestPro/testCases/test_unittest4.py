#coding:utf-8
#执行当面目录下所有用例：python -m unittest discover -s ./
#http://blog.itpub.net/69908432/viewspace-2647512/
import unittest
import HtmlTestRunner  #pip install html-testRunner

class TestCaseFour(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print "4setUpClass_method"
    @classmethod
    def tearDownClass(cls):
        print "4tearDownClass_method"
    def setUp(self):
        print "4setUp_method"
    def tearDown(self):
        print "4tearDown_method"
    def test_one(self):
        self.assertTrue(False)
        print "4test_one"
    def test_two(self):
        print "4test_two"
    def test_three(self):
        print "4test_three"

if __name__ == '__main__':
    # # 方法一： 把 TestCaseOne 里面所有的 test* 都添加并执行
    # loader = unittest.TestLoader()
    # suit_test_case = loader.loadTestsFromTestCase(TestCaseOne)
    # suit_all = unittest.TestSuite(suit_test_case)
    #
    # # 运行测试
    # runner = unittest.TextTestRunner()
    # runner.run(suit_all)

    # # 方法二：添加 TestCaseOne 中特定的用例并执行
    with open('html_result1','w+') as f:
        suit = unittest.TestSuite()
        suit.addTest(TestCaseFour('test_two'))
        suit.addTest(TestCaseFour('test_one'))
        suit.addTest(TestCaseFour('test_three'))
        # # 运行测试
        runner = HtmlTestRunner.HTMLTestRunner(output='./', stream=f, report_title=u'TestReport', descriptions=u'TestDetails')
        runner.run(suit)
