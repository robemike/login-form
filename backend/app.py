from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, create_access_token
from datetime import timedelta
from flask_cors import CORS
from flask_restful import Resource, Api
from flask_bcrypt import Bcrypt
import random

from models import db, Member

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///members.db'
app.config['SQLALCHEMT_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = "fsbdgfnhgvjnvhmvh"+str(random.randint(1,1000000000000)) 
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)
app.config["SECRET_KEY"] = "JKSRVHJVFBSRDFV"+str(random.randint(1,1000000000000))

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

migrate = Migrate(app=app, db=db)
db.init_app(app)
api = Api(app)

class SignUp(Resource):
    def post(self):
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        existing_member = Member.query.filter_by(email=email).first()
        if existing_member:
            return {"message": "Email address already exists."}, 400
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
            new_member = Member(username=username, email=email, password=hashed_password)
            db.session.add(new_member)
            db.session.commit()
            return {"message": "Member registered successfully."}
        
class Login(Resource):
    def post(self):
        username = request.form.get('username', None)
        email = request.form.get("email", None)
        password = request.form.get("password", None)

        member_username = Member.query.filter_by(username = username).first()
        member_email = Member.query.filter(Member.email == email).first()

        if member_email and member_username and bcrypt.check_password_hash(member_email.password, password):
            access_token = create_access_token(identity=member_email.id)
            return jsonify({"access_token":access_token})
        else:
            return {"message": "Invalid login credentials."}, 401

api.add_resource(SignUp, '/signup')
api.add_resource(Login, '/login')

if __name__ == "__main__":
    app.run(port=5555, debug=True)