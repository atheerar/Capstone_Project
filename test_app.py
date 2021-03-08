import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie, db_insert_all

class CastingAgencyTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = "postgres://qmuctnxsjzynmq:caaa92f73f104bc8eaf93ab5b71a13adec2d14616f4eac78575a109a0a6e4896@ec2-52-70-67-123.compute-1.amazonaws.com:5432/d5o744grfo2435"
        setup_db(self.app, self.database_path)
        db_insert_all()

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()
            self.casting_assistant_auth = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InpVaGxYSUlkZGttRFJ3bjFvMWFMdCJ9.eyJpc3MiOiJodHRwczovL2EtdGhlZXIudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwNDQ4N2I5NTc5N2RjMDA2ODhhMjhhMSIsImF1ZCI6ImNhcHN0b25lLWF0aGVlciIsImlhdCI6MTYxNTE5MjMyMywiZXhwIjoxNjE1Mjc4NzIzLCJhenAiOiJERlAxSjRCblQwdDNQR3U5SWo3d1NUdGlXa1h5Z2FZUCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.0wVZRroMir_nxNM4oEDAayeKm3EDXXbOI5E1y1nYFK42sWsLaJxw97udTe9QheoO6CVmjBQvDC4sdpaGh1K_ZrU-QPyjZxn5fwXoCpkZf9XewzNaRGAG8OIc9vGrbZ7Fux-hcrmLzWZ4Kuk-hNdxKiesxbB98upyPzFhE7uKfyj52Q1lb4mKcGQGmyIUi7-PKqedMkGlj4jwZ6sjkh-TaC2kfEWSNm8ns34NoEe1HuoMSbDq4H_ZLwCWAG1Izek2DdBp6CePh27Gr1laFRaKBfpuRtaqFUE8PWNv-Wx5C77-oz28YhUF7mKEBLSNlKWnyYAJW4as9v_EDWZCTDn0TQ '
            self.casting_director_auth = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InpVaGxYSUlkZGttRFJ3bjFvMWFMdCJ9.eyJpc3MiOiJodHRwczovL2EtdGhlZXIudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwNDQ4N2YxMGQ5ZjcxMDA3MGVlNjkzMCIsImF1ZCI6ImNhcHN0b25lLWF0aGVlciIsImlhdCI6MTYxNTE5MjE3MywiZXhwIjoxNjE1Mjc4NTczLCJhenAiOiJERlAxSjRCblQwdDNQR3U5SWo3d1NUdGlXa1h5Z2FZUCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiY3JlYXRlOmFjdG9ycyIsImNyZWF0ZTptb3ZpZXMiLCJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInVwZGF0ZTphY3RvcnMiLCJ1cGRhdGU6bW92aWVzIl19.PDFgf66vgq0Mzw-PvQJvYRHyCsqcNsfoKbp_GFiQRac2sXmNZhqxkDQYMPkYIa_3-9wrEEhUv_9Ij354wLiY2KGZjqWDjE94IDyscqqk0EDGR0l7JZOjg0SAc0Hy9-b713C_wHGnWvM6dSY0LXCjT6TC9fPSZ2tI4b_YQNkU1HNzqBbDhDl2io9I9_48HlbGa3wQcKWlh34EAJLwQRAgyszI97Q-mHuufFw05CowX7PEohopWW4AUbrArxCFh62WWtF6thsEG3zlk2vV0xxrIQW397UjSnqJ0wcQDzQCxe3L1odEbCNojCwy2jH8Zf8Ed1ZropK9yz1v8LifoSlsWg'
            self.producer_auth = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InpVaGxYSUlkZGttRFJ3bjFvMWFMdCJ9.eyJpc3MiOiJodHRwczovL2EtdGhlZXIudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwNDQ4ODEwM2Y4NDczMDA2ZjU2NGQ1YyIsImF1ZCI6Ik1ZX0ZTTkQiLCJpYXQiOjE2MTUxOTIwOTAsImV4cCI6MTYxNTI3ODQ5MCwiYXpwIjoiWW1wa2QwQ3Vaemk0bUUzRFJmSDI2U0h0dHFTbVNMSDMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.EMxUlgjZSCyij6GuokM50zYbKLjvC6IKrqzqYdba9q_Gx2nPYt2GvhgeC3Qja8PcdLB7ORhDd--cSSajL0Gzo3CTaxde-L9HUd4zUN-SrMFQ0wkKJDPgBxuO928gHCDA5qlKhvSdr6pv_eSZgMqeIcUKIHFc22Q9X9GgfKjqfgYIhNgrUCAZSZtzgWLL4T8JXTYVOveyazu-5hyEUlE6uU-NFhmpu6e_d-qHi3y8yM0VFwCCiww1h8QV1t5glqxpFjsJ4OoPF6zrM7rmbjCzWvLuw8zfR5C-80x04nizoZqu80qZIeSL_FfsQd15APqWHsan7n5IaVE9ZezD8BvvKw'
               
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
