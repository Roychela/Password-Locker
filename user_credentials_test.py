import unittest
class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User('Js', "123abc")
    def tearDown(self):
        User.user_list = []
    def test__init__(self):
        self.assertEqual(self.new_user.username,"Js")
        self.assertEqual(self.new_user.password,"123abc")


if __name__ == "__main__":
        
    unittest.main()