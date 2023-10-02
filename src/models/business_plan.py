```python
from datetime import datetime
from main import db

class BusinessPlan(db.Model):
    __tablename__ = 'business_plans'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=False, default='Draft')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('business_plans', lazy=True))

    def __init__(self, user_id, title, content, status='Draft'):
        self.user_id = user_id
        self.title = title
        self.content = content
        self.status = status

    def __repr__(self):
        return f'<BusinessPlan {self.title}>'
```