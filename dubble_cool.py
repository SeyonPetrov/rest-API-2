from flask_restful import reqparse, abort, Resource
from flask import Flask, jsonify
from data import db_session
from data.jobs import Jobs
from datetime import datetime

app = Flask(__name__)
db_session.global_init('db/blogs.db')


par = reqparse.RequestParser()
par.add_argument('team_leader', required=True, type=int)
par.add_argument('job', required=True)
par.add_argument('work_size', required=True, type=int)
par.add_argument('collaborators', required=True)
par.add_argument('is_finished', required=True, type=bool)


def abort_if_not_found(job_id):
    sess = db_session.create_session()
    job = sess.query(Jobs).get(job_id)
    if not job:
        abort(404, message=f'User {job_id} not found')


class JobsResource(Resource):
    def get(self, job_id):
        abort_if_not_found(job_id)
        job = db_session.create_session().query(Jobs).get(job_id)
        return jsonify({'user': job.to_dict(only=('job', 'team_leader', 'work_size'))})

    def delete(self, job_id):
        abort_if_not_found(job_id)
        sess = db_session.create_session()
        user = sess.query(Jobs).get(job_id)
        sess.delete(user)
        sess.commit()
        return jsonify({'ALL': 'GOOD'})


class JobsListRes(Resource):
    def get(self):
        jobs = db_session.create_session().query(Jobs).all()
        return jsonify({'all_users': [
            x.to_dict(only=('job', 'team_leader', 'work_size')) for x in jobs
        ]})

    def post(self):
        args = par.parse_args()
        sess = db_session.create_session()

        job = Jobs(
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            start_date=datetime.now(),
            is_finished=args['is_finished'],
            end_date=datetime.now()
        )
        sess.add(job)
        sess.commit()
        return jsonify({'ALL': 'GOOD'})





