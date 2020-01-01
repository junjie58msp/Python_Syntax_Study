#coding:utf-8
#执行当面目录下所有用例：python -m unittest discover -s ./
import unittest
class TestCaseThree(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print "3setUpClass_method"
    @classmethod
    def tearDownClass(cls):
        print "3tearDownClass_method"
    def setUp(self):
        print "3setUp_method"
    def tearDown(self):
        print "3tearDown_method"
    def test_one(self):
        self.assertTrue(False)
        print "3test_one"
    def test_two(self):
        print "3test_two"
    def test_three(self):
        print "3test_three"

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
    with open('txt_result1','w+') as f:
        suit = unittest.TestSuite()
        suit.addTest(TestCaseThree('test_two'))
        suit.addTest(TestCaseThree('test_one'))
        suit.addTest(TestCaseThree('test_three'))
        # # 运行测试
        runner = unittest.TextTestRunner(stream=f,verbosity=2)
        runner.run(suit)
