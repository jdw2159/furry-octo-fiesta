import routes
import unittest 

class MyUnitTests(unittest.TestCase): 

    @classmethod
    def setUpClass(cls):
        pass 

    @classmethod
    def tearDownClass(cls):
        pass 

    @classmethod
    def tearDownClass(cls):
        pass 

    def setUp(self):
        self.app = routes.app.test_client()
        self.app.testing = True 

    def tearDown(self):
        pass

    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_users_in_database(self):
        result = self.app.get('/')
        assert 'Jake' in result.data
        assert 'Don' not in result.data
        assert 'kldjlksa' not in result.data

    def test_add(self):
        self.assertEqual(2,2)


if __name__ == '__main__':
      unittest.main()
