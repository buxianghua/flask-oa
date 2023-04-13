from flask import Flask
import config
from models import UserModel
from exts import db, mail
from blueprints.auth import bp as auth_bp
from blueprints.qa import bp as qa_bp
from flask_migrate import Migrate

app = Flask(__name__)
# 加载绑定配置文件
app.config.from_object(config)

db.init_app(app)
mail.init_app(app)
migrate = Migrate(app,db)
# flask db init
# flask db migrate
# flask db upgrade

# 绑定蓝图
app.register_blueprint(auth_bp)
app.register_blueprint(qa_bp)


if __name__ == '__main__':
    app.run()
