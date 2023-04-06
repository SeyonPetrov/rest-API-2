from flask_restful import reqparse, abort, Resource
from flask import Flask, jsonify
from data import db_session
from data.users import User
from datetime import datetime
from werkzeug.security import generate_password_hash

app = Flask(__name__)
db_session.global_init('db/blogs.db')


par = reqparse.RequestParser()
par.add_argument('surname', required=True)
par.add_argument('name', required=True)
par.add_argument('age', required=True, type=int)
par.add_argument('position', required=True)
par.add_argument('speciality', required=True)
par.add_argument('address', required=True)
par.add_argument('email', required=True)
par.add_argument('hashed_password', required=True)


def abort_if_not_found(user_id):
    sess = db_session.create_session()
    user = sess.query(User).get(user_id)
    if not user:
        abort(404, message=f'User {user_id} not found')


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_not_found(user_id)
        user = db_session.create_session().query(User).get(user_id)
        return jsonify({'user': user.to_dict(only=('name', 'surname', 'position', 'address'))})

    def delete(self, user_id):
        abort_if_not_found(user_id)
        sess = db_session.create_session()
        user = sess.query(User).get(user_id)
        sess.delete(user)
        sess.commit()
        return jsonify({'ALL': 'GOOD'})


class UsersListRes(Resource):
    def get(self):
        users = db_session.create_session().query(User).all()
        return jsonify({'all_users': [
            x.to_dict(only=('name', 'surname', 'position', 'address')) for x in users
        ]})

    def post(self):
        args = par.parse_args()
        sess = db_session.create_session()

        user = User(
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email'],
            hashed_password=generate_password_hash(args['hashed_password']),
            modified_date=datetime.now()
        )
        sess.add(user)
        sess.commit()
        return jsonify({'ALL': 'GOOD'})





