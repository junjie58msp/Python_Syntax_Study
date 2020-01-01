# #coding:utf-8
# import HtmlTestRunner
# import unittest
# start_dir = './testCases'
# discover = unittest.defaultTestLoader.discover(start_dir=start_dir, pattern=r'test*.py')
# if __name__ == '__main__':
#     # 创建测试runner，执行测试用例集
#     with open('html_result1.html', 'w+') as f:
#         runner = HtmlTestRunner.HTMLTestRunner(output='./', stream=f, report_title='TestReport', descriptions='TestDetails')
#         runner.run(discover)


# import unittest,HtmlTestRunner
# suite = unittest.TestSuite()#创建测试套件
# start_dir = './testCases'
# all_cases = unittest.defaultTestLoader.discover(start_dir=start_dir, pattern=r'test_*.py')
# #找到某个目录下所有的以test开头的Python文件里面的测试用例
# for case in all_cases:
#     suite.addTests(case)#把所有的测试用例添加进来
# fp = open('res.html','wb')
# runner = HtmlTestRunner.HTMLTestRunner(stream=fp,report_title='all_tests',descriptions='Details')
# runner.run(suite)
# #运行测试



#https://www.cnblogs.com/NancyRM/p/8385850.html
#关于HTMLTestRunner 的说明
#coding:utf-8
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
start_dir = './testCases'
all_cases = unittest.defaultTestLoader.discover(start_dir=start_dir, pattern=r'test_*.py')

if __name__ == '__main__':
    # 存放报告的文件夹
    report_dir = './test_report'
    # 报告命名时间格式化
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # 报告文件完整路径
    report_name = report_dir+'/'+now+"_result.html"

    # 打开文件再报告文件写入测试结果
    with open(report_name, "wb") as f:
        runner = HTMLTestRunner(stream=f, title='TestReport', description='TestDetails')
        # 运行测试用例
        runner.run(all_cases)
        # 关闭报告文件
        f.close()