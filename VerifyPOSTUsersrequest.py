
from collections import Counter
from urllib import response
import requests
import unittest


API_URL = "https://jsonplaceholder.typicode.com/users"
           

class VerifyPOSTUsersrequest(unittest.TestCase):
    #parameterise ''
    Newuserparams = {
            
                "id": 11,
                "name": "Test Leanne Graham",
                "username": "Test Bret",
                "email": "TestSincere@april.biz",
                "address": {
                    "street": "TestKulas Light",
                    "suite": "TesrApt. 556",
                    "city": "TestGwenborough",
                    "zipcode": "92788-3874",
                    "geo": {
                    "lat": "-32.3159",
                    "lng": "88.1496"
                    }
                  },
                        "phone": "1-160-736-8021 x56442",
                        "website": "testhildegard.org",
                        "company": {
                        "name": "testRomaguera-Crona",
                        "catchPhrase": "testMulti-layered client-server neural-net",
                        "bs": "testharness real-time e-markets"
                        }
            }
         
    # Get API Response
   # response = requests.get(API_URL, params=params)
    # Read API Data
  #  response_body = response.json()
    

    headers = {"Accept": "application/json"}
    endpoint = "https://jsonplaceholder.typicode.com/users"
    response = requests.post(endpoint, params=Newuserparams, headers=headers)
    print("respose Code",response.status_code)
    print("respose Code"+ response.text)
    print("respose Code", response.json())

    response_body = response.json()


# validate API status code and Content types
    def test_Verify_Created_message_is_returned_201(self):
        # validate whether API status code is equal to 200 or not
        self.assertEqual(self.response.status_code,201, \
            "Response status code Expected : 201, but found : " + str(self.response.status_code))
        # validate whether API response headers 'Content-Type'  is "application/json" or not
        self.assertEqual(self.response.headers['Content-Type'], "application/json; charset=utf-8", \
            "Response content type Expected:application json, but found :  " + str(self.response.headers['Content-Type']))

#  Verify that the posted data are showing up in the result
    def test_Verify_that_the_posted_data_Is_Created (self):
        print ("Request text ",self.response.text)  
        Total=0   
        for getId in self.response_body:
           # username = getId.get("id",0)
           # print("username: "+username)
            Total+=1

        if(Total == 1):
            self.assertEqual(Total, 1, "Total No.of users Users Found in the request")
            print("The Total no.of users :" ,Total)  
        else:
            raise Exception("User name 'Nicholas Runolfsdottir V' not found when Id=8",Total)    
    


if __name__ == '__main__':
    unittest.main()

