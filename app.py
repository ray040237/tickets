from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def api():
    name = request.args.get('name')
    age = request.args.get('age')
    if name and age:
        response = {
            'status': 'success',
            'message': f'Hello, {name}! You are {int(age)+2} years old.'
        }
    else:
        response = {
            'status': 'error',
            'message': 'Please provide both name and age.'
        }
    return jsonify(response)

if __name__ == '__main__':
    app.run()
