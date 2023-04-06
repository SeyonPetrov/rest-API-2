from data import db_session
from flask import Flask, make_response, jsonify
import cool, dubble_cool
from flask_restful import Api


app = Flask(__name__)
api = Api(app)


def main():
    db_session.global_init("db/blogs.db")
    api.add_resource(cool.UsersResource, '/api/v2/users/<int:user_id>')
    api.add_resource(cool.UsersListRes, '/api/v2/users')
    api.add_resource(dubble_cool.JobsResource, '/api/v2/jobs/<int:job_id>')
    api.add_resource(dubble_cool.JobsListRes, '/api/v2/jobs/')
    app.run(debug=True)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


if __name__ == '__main__':
    main()
