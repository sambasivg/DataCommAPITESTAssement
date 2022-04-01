
from collections import Counter
from urllib import response
import requests
import unittest


API_URL = "https://jsonplaceholder.typicode.com/users"
           

class APIAutomationtest(unittest.TestCase):
    # Get API Response
    response = requests.get(API_URL)
    # Read API Data
    response_body = response.json()


# validate API status code and Content types
    def test_Verify_GET_Users_request_check_status_code_equals_200(self):
        # validate whether API status code is equal to 200 or not
        self.assertEqual(self.response.status_code,200, \
            "Response status code Expected : 200, but found : " + str(self.response.status_code))
        # validate whether API response headers 'Content-Type'  is "application/json" or not
        self.assertEqual(self.response.headers['Content-Type'], "application/json; charset=utf-8", \
            "Response content type Expected:application json, but found :  " + str(self.response.headers['Content-Type']))

#  Verify that there are 10 users in the results
    def test_Verify_that_there_are_10_users(self):
        total=0
        for getId in self.response_body:
            user = getId.get("username",0)
            total += 1

        
        print(f"Total Users Found in the Request {total}")
        
        if(total==10):
            self.assertEqual(total, 10, "There are total :  " + str(total) + "Users Found in the given API")
        else:
            raise Exception("No of users are More than 10")  

    
if __name__ == '__main__':
    unittest.main()

