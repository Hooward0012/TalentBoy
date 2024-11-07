import unittest
from calc.test import add, minus, multi


class TestCalc(unittest.TestCase):

    def setUp(self) -> None:
        print("测试前的操作，例如环境的初始化，数据库连接。。。")

    def tearDown(self) -> None:
        print('测试结束的操作， 例如垃圾清理，文件关闭，数据库连接关闭')
    def test_add(self):
        a = 5
        b = 6
        self.assertEqual(add(a, b), 11)

    @unittest.skip("跳过这个测试")
    def test_minus(self):
        a = 5
        b = 6
        self.assertEqual(minus(a, b), -1)

    def test_multi(self):
        a = 5
        b = 6
        self.assertEqual(multi(a, b), 30)


if __name__ == '__main__':
    unittest.main()
