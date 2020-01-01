#coding:utf-8
import unittest
class TestCaseOne(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print "setUpClass_method"
    @classmethod
    def tearDownClass(cls):
        print "tearDownClass_method"
    def setUp(self):
        print "setUp_method"
    def tearDown(self):
        print "tearDown_method"
    def test_one(self):
        self.assertTrue(False)
        print "test_one"
    def test_two(self):
        print "test_two"
    def test_three(self):
        print "test_three"

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
    suit = unittest.TestSuite()
    suit.addTest(TestCaseOne('test_two'))
    suit.addTest(TestCaseOne('test_one'))
    suit.addTest(TestCaseOne('test_three'))
    # # 运行测试
    runner = unittest.TextTestRunner()
    runner.run(suit)
