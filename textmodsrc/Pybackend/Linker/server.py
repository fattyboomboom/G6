import json

from flask import Flask, request, jsonify, abort, Response, flash, redirect, url_for
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename

#helper function imports
from posts import write_json
from filterProfanity import CheckProfanity

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/')
def hello():
    return ''

# posts route which loads the posts.json file and returns to front-end
@app.route('/posts', methods=['GET'])
def getPosts():
    with open('post.json','r+') as file:
            file_data = json.load(file)
    return file_data

@app.route('/images', methods=['POST', 'GET'])
def imageUpload():
  if request.method == 'POST':
    file = request.files['uploadblobby']
    print(file)
  return 'hi'

# endpoint responsible for handling post moderation and post submission
@app.route('/process', methods=['POST', 'GET'])
def FilterProfanity():
    submission = request.get_json()
    print(submission)
    process = submission['post']

    if request.method == 'POST':
        #checks that post is not empty
        if len(process) > 0:
            #processes post for profanity
            output = CheckProfanity(process)
            #if output is true, denoting that profanity was found, return error status code
            #otherwise we write the json to a file and return success code
            if output:
                return jsonify({ 
                    'status' : 'failed', 
                    'profanity' : output}), 403
            
            write_json(submission)
            return jsonify({
                'status' : 'success',
                'profanity' : output,
                })
        return abort(406,  description="Please return a submission!")
    return '??? what happen'