import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie, db_insert_all
# from config import auth0_tokens

class CastingAgencyTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = "postgresql:///movie_db"
        setup_db(self.app, self.database_path)
        db_insert_all()

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

            self.casting_assistant_auth = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InpVaGxYSUlkZGttRFJ3bjFvMWFMdCJ9.eyJpc3MiOiJodHRwczovL2EtdGhlZXIudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwNDQ4N2I5NTc5N2RjMDA2ODhhMjhhMSIsImF1ZCI6Ik1ZX0ZTTkQiLCJpYXQiOjE2MTUxMjU5OTUsImV4cCI6MTYxNTEzMzE5NSwiYXpwIjoiWW1wa2QwQ3Vaemk0bUUzRFJmSDI2U0h0dHFTbVNMSDMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.WXPzzIRIlj7sB53uvqeqkuj0CAHhyK1w2uXSa69EAZ3EQVhF_pCVLMtsVWNMiDkQaMCeBOf9_3QvX6M-RRIEUSCTR7wpN5NEr_SCab9ocMtU-oJfwuTHJg16i0DR__kt0pHjTJm6VI2nyQCqXBgPyQKPUhXeUkJZwQ0fZqrE5_xCS59qYV0uv6qcKu4M7bjQxnL_6kfYTiy_pFNjEArZ3wkwnomvchm93mj1UXAYWNsgvuCp2j4qbwONsooQucdSAwEoHCDd-on872xfH6QrlV6UOufz-4bDHIPq0UHhLxFYW9QIH2WwgK5IHmXkjQKrgbWMNtmB-T7HQGX2i6CQ9A'
            self.casting_director_auth = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InpVaGxYSUlkZGttRFJ3bjFvMWFMdCJ9.eyJpc3MiOiJodHRwczovL2EtdGhlZXIudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwNDQ4N2YxMGQ5ZjcxMDA3MGVlNjkzMCIsImF1ZCI6Ik1ZX0ZTTkQiLCJpYXQiOjE2MTUxMjYwNzAsImV4cCI6MTYxNTEzMzI3MCwiYXpwIjoiWW1wa2QwQ3Vaemk0bUUzRFJmSDI2U0h0dHFTbVNMSDMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImNyZWF0ZTphY3RvcnMiLCJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJ1cGRhdGU6YWN0b3JzIiwidXBkYXRlOm1vdmllcyJdfQ.A5XRHZfYRJa7Ag0x_mWLI1VK5O_XLpmrjk4M7jh2Xo7qVnf9HOLfuoJYsqXRuLfo4gl4xCW4BlmR7kWhxspjabNG-YKIbksjeIb5z_27mJVKsVtFicp_XqPXtHEBJkNpoCWsVJHBZFyj4cT5lmbZfQid47vuQr4hBpX-iYD4uHJAD3CJujHhCBfQma5Gq9ip-pyA27fcEl7LAyZWEnj0pUNtEDhwLQvVZ7T9jmpBZs2yOQJW7vsmZZSK6XtCkiyH1o6XQIRkBMZ9KIqocJmXr8ct-khexQe5RgZ8hqzjmpD2K0XTIPki-2WjnIJGrYvWVCbPEJw_svC9Nty9XuneZA'
            self.producer_auth = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InpVaGxYSUlkZGttRFJ3bjFvMWFMdCJ9.eyJpc3MiOiJodHRwczovL2EtdGhlZXIudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwNDQ4ODEwM2Y4NDczMDA2ZjU2NGQ1YyIsImF1ZCI6Ik1ZX0ZTTkQiLCJpYXQiOjE2MTUxMjk2MzksImV4cCI6MTYxNTEzNjgzOSwiYXpwIjoiWW1wa2QwQ3Vaemk0bUUzRFJmSDI2U0h0dHFTbVNMSDMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.LikOSkhTajzbpv8xjWtM4P2HXTJa6MkbVKcOtY6XkGm5MJOT379tQOIufvMx2D1UKzUfyTaA_VQgn0Z1O0nMZHdKuMiVFi_HMgwJPCthMj6qeLKvpzKfeyxPf3i2AeQPtCtGC1GQOBZVmmqJlYeRtKXFtsx0kl-BwJum3Ct_Y2pUz50RB2Myp7QOSX5Pc55u8-IkhlyrIGvgalr50vd6AOySdAd_okGi7rmWRAn9YEJjKgKOoFn1t5M15XiNNLXimf5m0FdxXrUDJUUeQbyUu0H4KClyYW6Cb04TlLGEb7DP5L8vEMQNFOJzL2SzbN6PviL-vyTpvyHjuZtyenDVug'
                        
            self.new_actor = {
                'name': 'Test Nmae', 
                'age': '27',
                'gender': 'Female'
            }
            self.new_movie = {
                'title': 'Test Movie',
                'release_date': '21/06/1993'
            }
            self.emty_actor = {}
            self.emty_movie = {}

    def tearDown(self):
        pass

    def test_first(self):
        res = self.client().get('/')
        self.assertEqual(res.status_code, 200)

    def test_retrieve_actors_valid(self):
        res = self.client().get('/actors', headers={"Authorization": "Bearer {}".format(self.producer_auth)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_retrieve_movies_valid(self):
        res = self.client().get('/movies', headers={"Authorization": "Bearer {}".format(self.producer_auth)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_create_actor_valid(self):
        res = self.client().post('/actors', json=self.new_actor, headers={"Authorization": "Bearer {}".format(self.producer_auth)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_actor_unvalid(self):        
        res = self.client().post('/actors', json=self.emty_actor, headers={"Authorization": "Bearer {}".format(self.producer_auth)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
    

    def test_create_movie_valid(self):
        res = self.client().post('/movies', json=self.new_movie, headers={"Authorization": "Bearer {}".format(self.producer_auth)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_movie_unvalid(self):
        res = self.client().post('/movies', json=self.emty_movie, headers={"Authorization": "Bearer {}".format(self.producer_auth)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)


    def test_update_actor_valid(self):
        res = self.client().patch('/actors/1', json=self.new_actor, headers={"Authorization": "Bearer {}".format(self.producer_auth)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_actor_unvalid(self):
        res = self.client().patch('/actors/1', json=self.emty_actor, headers={"Authorization": "Bearer {}".format(self.producer_auth)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_update_movie_valid(self):
        res = self.client().patch('/movies/1', json=self.new_movie, headers={"Authorization": "Bearer {}".format(self.producer_auth)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_movie_unvalid(self):
        res = self.client().patch('/movies/1', json=self.emty_movie, headers={"Authorization": "Bearer {}".format(self.producer_auth)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)


    def test_delete_actor_valid(self):
        res = self.client().delete('/actors/1',  headers={"Authorization": "Bearer {}".format(self.producer_auth)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 1)

    def test_delete_actor_unvalid(self):
        res = self.client().delete('/actors/400',  headers={"Authorization": "Bearer {}".format(self.producer_auth)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_delete_movie_valid(self):
        res = self.client().delete('/movies/1',  headers={"Authorization": "Bearer {}".format(self.producer_auth)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['delete'], 1)

    def test_delete_movie_unvalid(self):
        res = self.client().delete('/movies/123', headers={"Authorization": "Bearer {}".format(self.producer_auth)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)

    def test_casting_assistant_auth_valid(self):
        res = self.client().get('/actors', headers={"Authorization": "Bearer {}".format(self.casting_assistant_auth)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_casting_assistant_auth_unvalid(self): 
        res = self.client().patch('/movies/1', json= self.new_movie,  headers={"Authorization": "Bearer {}".format(self.casting_assistant_auth)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "unauthorized")


    def test_casting_director_auth_valid(self):
        res = self.client().get('/actors', headers={"Authorization": "Bearer {}".format(self.casting_director_auth)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_casting_director_auth_unvalid(self):
        res = self.client().delete('/movies/1', headers={"Authorization": "Bearer {}".format(self.casting_director_auth)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "unauthorized")

if __name__ == "__main__":
    unittest.main()
