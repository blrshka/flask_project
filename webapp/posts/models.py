from datetime import datetime
from sqlalchemy.orm import relationship

from webapp.db import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    text = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id', ondelete='CASCADE'),
        index=True)
    
    user = relationship('User', backref='posts')

    def __repr__(self):
        return '<Post {} {}>'.format(self.title, self.created)