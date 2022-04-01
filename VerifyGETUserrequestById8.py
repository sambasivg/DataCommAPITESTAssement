
from collections import Counter
from urllib import response
import requests
import unittest


API_URL = "https://jsonplaceholder.typicode.com/users"
           

class VerifyGetUserReqById(unittest.TestCase):
    #parametarise 'id'
    IdParams = {'id': '8'}

    Expecteduser = "Nicholas Runolfsdottir V"
    # Get API Response
    response = requests.get(API_URL, params=IdParams)
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
    def test_Verify_GET_User_request_by_Id8(self):
        print ("Request text for Id=8",self.response.text)     
        for getId in self.response_body:
            name = getId.get("name",0)
            print("username: "+name)

        if(name ==self.Expecteduser):
            self.assertEqual(name, "Nicholas Runolfsdottir V", "The Id 8 username is :  " + name + "Users Found in the request")
            print("The Id=8 username is :" +name)  
        else:
            raise Exception("User name 'Nicholas Runolfsdottir V' not found for given Id")    
    
if __name__ == '__main__':
    unittest.main()

