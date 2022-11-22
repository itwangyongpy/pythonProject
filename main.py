"""
运行整个testcase下所有的文件

"""
import unittest
from testcase.test_meetingroom import TestMeetingRoom
from BeautifulReport import  BeautifulReport
def allTests():
    """
    执行所有的用例
    :return:
    """
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    alltests = loader.discover(start_dir='testcase')
    suite.addTest(alltests)
    return alltests


# def smokeTests():
#         suite = unittest.TestSuite()
#         loader = unittest.TestLoader()
#         suite.addTest(TestMeetingRoom("test1_add_meetingroom"))
#         suite.addTest


if __name__ == '__main__':
    # runner = unittest.TextTestRunner(verbosity=2)
    runner = BeautifulReport(allTests())
    runner.report(description='企业微信api测试',report_dir='reports')
