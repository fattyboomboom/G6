# import random
# import string
# import os
# from flask import Flask, request, jsonify
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail
# from SendGridAPI import SENDGRID_API_KEY, SENDGRID_FROM_EMAIL

# app = Flask(__name__)
# # CORS(app)

# def generate_token():
#     token = string.ascii_letters + string.digits
#     return ''.join(random.choice(token) for i in range(20))

# def send_verification_email(to_email, verification_token):
#     message = Mail(
#         from_email=f"WolfCampus {SENDGRID_FROM_EMAIL}",
#         to_emails=to_email,
#         subject='Verify your email address',
#         html_content=f'Please click on this link to verify your email address: http://localhost:8080/verify_email?token={verification_token}'
#     )
#     try:
#         sg = SendGridAPIClient(SENDGRID_API_KEY)
#         response = sg.send(message)
#         return True
#     except Exception as e:
#         print(e)
#         return False

# def send_forgot_password(to_email, verification_token):
#     message = Mail(
#         from_email=f"WolfCampus {SENDGRID_FROM_EMAIL}",
#         to_emails=to_email,
#         subject='Verify your email address',
#         html_content = f'''Hello, {to_email}, a request was made to change your WolfCampus password. Please click this link to chang your password:
#         http://localhost:8080/verify_email?token={verification_token}

#         If you did not make this request, please contact our support.'''
#     )
#     try:
#         sg = SendGridAPIClient(SENDGRID_API_KEY)
#         response = sg.send(message)
#         return True
#     except Exception as e:
#         print(e)
#         return False

# # @app.route('/create_account', methods=['POST'])
# def create_account(email):
#     verification_token = generate_token()
#     send_verification_email(email, verification_token)
#     message = {'message' : 'E-mail successfully sent'}
#     return jsonify(message), 200




# @app.route('/forgot_password', methods=['POST'])
# def forgotPassword():
#     email = request.json['email']
#     verification_token = generate_token()
#     send_forgot_password(email, verification_token)
#     message = {'message' : 'E-mail successfully sent'}
#     return jsonify(message), 200
