```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from src.routes import *

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
```