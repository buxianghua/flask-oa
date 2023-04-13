# 存在的目的就是为了解决循环引用的问题
# flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

mail = Mail()
db = SQLAlchemy()