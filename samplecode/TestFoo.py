import unittest
from unittest import mock

def foo(user):
    return {'name': user.name, 'fullname': user.get_fullname()}

class TestFoo(unittest.TestCase):
    def test_call(self):
        dummy = mock.Mock()
        dummy.name = 'John' # 属性のセット
        dummy.get_fullname.return_value = 'John Smith' # 関数返り値のセット
        
        self.assertEqual(foo(dummy), {'name': 'John', 'fullname': 'John Smith'})
        dummy.get_fullname.assert_called_once()
