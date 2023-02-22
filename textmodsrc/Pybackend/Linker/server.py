from flask import Flask, request, jsonify, abort, make_response
from flask_cors import CORS, cross_origin
from filterProfanity import CheckProfanity

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/')
def hello():
    return "hi"

@app.route('/process', methods=['POST', 'GET'])
def FilterProfanity():
    submission = request.get_data()
    process = str(submission, 'utf-8')

    if request.method == 'POST':
        if len(submission) > 0:
            output = CheckProfanity(process)
            return jsonify({
                'status' : 'success',
                'profanity' : output })
        return abort(406, f'Must return a submission')
    return 'get'
