import datetime
import sqlalchemy
from sqlalchemy import orm
from data.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Jobs(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, autoincrement=True, primary_key=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Float, nullable=True)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now())
    end_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now())
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    user = orm.relationship('User')

    def __repr__(self):
        return f'<Job> {self.job}'
