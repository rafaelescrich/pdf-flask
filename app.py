#!flask/bin/python
from flask import Flask
from flask import jsonify
from flask import abort
from flask import make_response
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

users = [
    {
        'id': 1,
        'username': u'rafaelescrich',
        'email': u'rafaelescrich@gmail.com', 
        'name': u'Rafael Escrich',
	'cpf': u'32742438840',
	'rg': u'274851647',
	'phone': u'+554899926942',

    },
    {
        'id': 2,
        'username': u'rafaelescrich',
        'email': u'rafaelescrich@gmail.com', 
        'name': u'Rafael Escrich',
	'cpf': u'32742438840',
	'rg': u'274851647',
	'phone': u'+554800000000',
    }
]

@app.route('/api/v1/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})

@app.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    return jsonify({'user': user[0]})

@app.route('/api/v1/users', methods=['POST'])
def create_user():
    if not request.json or not 'username' in request.json:
        abort(400)
    user = {
        'id': users[-1]['id'] + 1,
        'username': request.json['username'],
	'email': request.json['email'],
	'name': request.json['name'],
	'cpf': request.json['cpf'],
	'rg': request.json['rg'],
	'phone': request.json['phone']
    }
    users.append(user)
    return jsonify({'user': user}), 201

@app.route('/api/v1/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'username' in request.json and type(request.json['username']) != unicode:
        abort(400)
    if 'email' in request.json and type(request.json['email']) is not unicode:
        abort(400)
    if 'name' in request.json and type(request.json['name']) is not unicode:
        abort(400)
    if 'cpf' in request.json and type(request.json['cpf']) is not unicode:
        abort(400)
    if 'rg' in request.json and type(request.json['rg']) is not unicode:
        abort(400)
    if 'phone' in request.json and type(request.json['phone']) is not unicode:
        abort(400)
    user[0]['username'] = request.json.get('username', user[0]['username'])
    user[0]['email'] = request.json.get('email', user[0]['email'])
    user[0]['name'] = request.json.get('name', user[0]['name'])
    user[0]['cpf'] = request.json.get('cpf', user[0]['cpf'])
    user[0]['rg'] = request.json.get('rg', user[0]['rg'])
    user[0]['phone'] = request.json.get('phone', user[0]['phone'])
    return jsonify({'user': user[0]})

@app.route('/api/v1/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    user.remove(user[0])
    return jsonify({'result': True})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
