import unittest
import requests

<<<<<<< HEAD
class TestUsers(unittest.TestCase):
=======
class Test_users(unittest.TestCase):
>>>>>>> fb34b3aabdfcb8b2e5cf23cf51d1c2cee40506c8
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
<<<<<<< HEAD


class TestPages(unittest.TestCase):
    def setUp(self):
        self.url = 'https://reqres.in/'

    def test_list_resource(self):
        self.response = requests.get(self.url + 'api/unknown')
        self.assertEqual(self.response.status_code, 200)

        expected_response_body = {"page":1,"per_page":6,"total":12,"total_pages":2,"data":[{"id":1,"name":"cerulean","year":2000,"color":"#98B2D1","pantone_value":"15-4020"},{"id":2,"name":"fuchsia rose","year":2001,"color":"#C74375","pantone_value":"17-2031"},{"id":3,"name":"true red","year":2002,"color":"#BF1932","pantone_value":"19-1664"},{"id":4,"name":"aqua sky","year":2003,"color":"#7BC4C4","pantone_value":"14-4811"},{"id":5,"name":"tigerlily","year":2004,"color":"#E2583E","pantone_value":"17-1456"},{"id":6,"name":"blue turquoise","year":2005,"color":"#53B0AE","pantone_value":"15-5217"}],"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}
        self.assertDictEqual(self.response.json(), expected_response_body)

    def test_single_resource(self):
        self.response = requests.get(self.url + 'api/unknown/2')
        self.assertEqual(self.response.status_code, 200)

        expected_response_body = {"data":{"id":2,"name":"fuchsia rose","year":2001,"color":"#C74375","pantone_value":"17-2031"},"support":{"url":"https://reqres.in/#support-heading","text":"To keep ReqRes free, contributions towards server costs are appreciated!"}}
        self.assertDictEqual(self.response.json(), expected_response_body)

    def test_single_resource_not_found(self):
        self.response = requests.get(self.url + 'api/unknown/23')
        self.assertEqual(self.response.status_code, 404)

        expected_response_body = {}
        self.assertDictEqual(self.response.json(), expected_response_body)


class TestUserCRUD(unittest.TestCase):
    def setUp(self):
        self.url = 'https://reqres.in/'

    def test_create(self):
        user_data = {
            "name": "testir",
            "job": "tester"
        }

        self.response = requests.post(self.url + 'api/users', json=user_data)
        self.assertEqual(self.response.status_code, 201)

        expected_user_data = self.response.json()
        self.assertEqual(expected_user_data["name"], user_data["name"])
        self.assertEqual(expected_user_data["job"], user_data["job"])

    def test_update_put(self):
        user_data = {
            "name": "test",
            "job": "tester"
        }

        self.response = requests.put(self.url + 'api/users/2', json=user_data)
        self.assertEqual(self.response.status_code, 200)

        expected_user_data = self.response.json()
        self.assertEqual(expected_user_data["name"], user_data["name"])
        self.assertEqual(expected_user_data["job"], user_data["job"])

    def test_update_patch(self):
        user_data = {
            "name": "test",
            "job": "tester"
        }

        self.response = requests.put(self.url + 'api/users/2', json=user_data)
        self.assertEqual(self.response.status_code, 200)

        expected_user_data = self.response.json()
        self.assertEqual(expected_user_data["name"], user_data["name"])
        self.assertEqual(expected_user_data["job"], user_data["job"])

    def test_delete(self):
        self.response = requests.delete(self.url + 'api/users/2')
        self.assertEqual(self.response.status_code, 204)


class TestRegLog(unittest.TestCase):
    def setUp(self):
        self.url = 'https://reqres.in/'
    def test_register_suc(self):
        user_data = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }

        self.response = requests.post(self.url + 'api/register', json=user_data)
        self.assertEqual(self.response.status_code, 200)

        expected_response_data = {
            "id": 4,
            "token": "QpwL5tke4Pnpja7X4"
        }

        self.assertDictEqual(self.response.json(), expected_response_data)

    def test_register_unsuc(self):
        user_data = {
            "email": "sydney@fife"
        }

        self.response = requests.post(self.url + 'api/register', json=user_data)
        self.assertEqual(self.response.status_code, 400)

        expected_response_data = {
            "error": "Missing password"
        }

        self.assertDictEqual(self.response.json(), expected_response_data)

    def test_login_suc(self):
        user_data = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }

        self.response = requests.post(self.url + 'api/login', json=user_data)
        self.assertEqual(self.response.status_code, 200)

        expected_response_data = {
            "token": "QpwL5tke4Pnpja7X4"
        }

        self.assertDictEqual(self.response.json(), expected_response_data)

    def test_login_unsuc(self):
        user_data = {
            "email": "peter@klaven"
        }

        self.response = requests.post(self.url + 'api/login', json=user_data)
        self.assertEqual(self.response.status_code, 400)

        expected_response_data = {
            "error": "Missing password"
        }

        self.assertDictEqual(self.response.json(), expected_response_data)
=======
>>>>>>> fb34b3aabdfcb8b2e5cf23cf51d1c2cee40506c8
