# pip install Flask-cors
# pip install sendgrid

import random
import string
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from SendGridAPI import SENDGRID_API_KEY, SENDGRID_FROM_EMAIL

app = Flask(__name__)
CORS(app)

def generate_verification_token():
    token = string.ascii_letters + string.digits
    return ''.join(random.choice(token) for i in range(20))

def send_verification_email(to_email, verification_token):
    message = Mail(
        from_email=f"WolfCampus {SENDGRID_FROM_EMAIL}",
        to_emails=to_email,
        subject='Verify your email address',
        html_content=f'Please click on this link to verify your email address: http://localhost:8080/verify_email?token={verification_token}'
    )
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        return True
    except Exception as e:
        print(e)
        return False

@app.route('/create_account', methods=['POST'])
def create_account():
    email = request.json['email']
    verification_token = generate_verification_token()
    send_verification_email(email, verification_token)
    message = {'message' : 'E-mail successfully sent'}
    return jsonify(message), 200


 #********To do**************
# @app.route('/verify_email')
# def verify_email():
    # Get token from link
    # Look up token for corresponding account
    # When token is found, mark account as verified
    # If token/link doesnt exist, notify user.

if __name__ == '__main__':
    app.run(debug=True, port=3000)