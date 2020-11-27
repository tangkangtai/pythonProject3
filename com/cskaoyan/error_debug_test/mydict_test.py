import unittest

from com.cskaoyan.error_debug_test.mydict import Dict

#编写单元测试 测试类  从unittest.TestCase继承
#以test开头的方法就是测试方法
class TestDict(unittest.TestCase):

    def test_init(self):

        d = Dict(a=1,b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'],'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            # print(d.empty)
            value = d.empty


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # unittest.main()


#setUp()  和 tearDown()
#这两个方法分别在每调用一个测试方法的前后分别被执行
#比如在测试 连接数据库时
class TestDict(unittest.TestCase):
    def setUp(self):
        print('setUp....')

    def tearDown(self):
        print('tearDown...')


