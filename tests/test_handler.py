import unittest
import index

class TestHandlerCase(unittest.TestCase):

    def test_response(self):

        event = {'pathParameters': {'topicID': 1}}
        print("testing response.")
        result = index.handler(event, None)
        print(result)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')

if __name__ == '__main__':
    unittest.main()