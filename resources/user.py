from flask_restful import Resource, reqparse

from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."

    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank."

    )

    def post(self):
        data = __class__.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': "A user with the name '{}' already exists.".format(data['username'])}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {'message': "User '{}' successfully registered.".format(data['username'])}, 201
