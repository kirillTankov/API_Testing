import unittest
import requests

class Test_users(unittest.TestCase):
    def setUp(self):
        self.url = 'https://reqres.in/'

    def test_list_users(self):
        self.response = requests.get(self.url + 'api/users?page=2')
        self.assertEqual(self.response.status_code, 200)

        expected_response_body = {"page":2,"per_page":6,"total":12,"total_pages":2,"data":[{"id":7,"email":"michael.lawson@reqres.in","first_name":"Michael","last_name":"Lawson","avatar":"https://reqres.in/img/faces/7-image.jpg"},{"id":8,"email":"lindsay.ferguson@reqres.in","first_name":"Lindsay","last_name":"Ferguson","avatar":"https://reqres.in/img/faces/8-image.jpg"},{"id":9,"email":"tobias.funke@reqres.in","first_name":"Tobias","last_name":"Funke","avatar":"https://reqres.in/img/faces/9-image.jpg"},{"id":10,"email":"byron.fields@reqres.in","first_name":"Byron","last_name":"Fields","avatar":"https://reqres.in/img/faces/10-image.jpg"},{"id":11,"email":"george.edwards@reqres.in","first_name":"George","last_name":"Edwards","avatar":"https://reqres.in/img/faces/11-image.jpg"},{"id":12,"email":"rachel.howell@reqres.in","first_name":"Rachel","last_name":"Howell","avatar":"https://reqres.in/img/faces/12-image.jpg"}],"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}

        self.assertDictEqual(self.response.json(), expected_response_body)

    def test_single_user(self):
        self.response = requests.get(self.url + 'api/users/2')
        self.assertEqual(self.response.status_code, 200)

        expected_response_body = {"data":{"id":2,"email":"janet.weaver@reqres.in","first_name":"Janet","last_name":"Weaver","avatar":"https://reqres.in/img/faces/2-image.jpg"},"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}
        self.assertDictEqual(self.response.json(), expected_response_body)

    def test_single_user_not_found(self):
        self.response = requests.get(self.url + 'api/users/23')
        self.assertEqual(self.response.status_code, 404)

        expected_response_body = {}
        self.assertDictEqual(self.response.json(), expected_response_body)
