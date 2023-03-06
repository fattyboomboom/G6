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

@app.route('/posts', methods=['GET'])
def get_posts():
    posts = [
        {
            "name": "John Smith",
            "date": "1/1/23",
            "time": "9:00 PM",
            "category": "Gaming",
            "likes": 256,
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        },
        {
            "name": "Jenny Jones",
            "date": "1/1/23",
            "time": "6:00 PM",
            "category": "Coding",
            "likes": 98,
            "content": "Dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        },
        {
            "name": "Sam Smith",
            "date": "1/1/23",
            "time": "2:45 PM",
            "category": "Cooking",
            "likes": 325,
            "content": "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        },
        {
            "name": "Alice Smith",
            "date": "1/1/23",
            "time": "12:00 PM",
            "category": "Movies",
            "likes": 500,
            "content": "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."
        },
        {
            "name": "Bob Smith",
            "date": "1/1/23",
            "time": "11:15 AM",
            "category": "Music",
            "likes": 150,
            "content": "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        },
    ]
    return jsonify(posts)

# @app.route('/friends', methods=['GET', 'POST'])
# def get_posts():
#     post = [
#         { "id": "1",'name': "Tessa", "avatar": "https://www.minneapolisheadshots.com/gallery/main/professional-woman1.jpg", "content": "I need sleep!"},
#         { "id": "2",'name': "Fra", "avatar": "https://www.shutterstock.com/image-photo/young-serious-indian-professional-business-260nw-1941541432.jpg", "content": "Class is cancelled. Yay!"},
#         { "id": "3",'name': "Rylie", "avatar": "https://riverviewphotography.com/wp-content/uploads/2020/05/Professional-Headshots6-scaled.jpg", "content": "Panda express has the longest lines."},
#         { "id": "4",'name': "Drake", "avatar": "https://www.rashidahdevore.com/uploads/9/0/0/6/90067921/ssp-64544-fs-web.jpg", "content": "Im not that Drake."},
#         { "id": "5",'name': "Brittany", "avatar": "https://images.squarespace-cdn.com/content/v1/53b599ebe4b08a2784696956/1495767786612-YF1JF6XGTDRMS920068H/professional-photographer-08.jpg", "content": "It's cold."},
#         { "id": "6",'name': "Jeramiah", "avatar": "https://images.squarespace-cdn.com/content/v1/55b029d3e4b022c52efdde18/1553193307362-G0ZWC3V4XFZTZ8DTR5VY/bowling+green+ohio+headshots-9.jpg", "content": "Anyone know any good barbershops?"},
#         { "id": "7",'name': "Emilie", "avatar": "https://www.mayo.edu/-/media/kcms/employees/2019/10/11/17/15/isabel-santana-16194357.jpg", "content": "I need sleep!"},
#         { "id": "8",'name': "Eric", "avatar": "https://thumbs.dreamstime.com/b/businessman-wearing-suit-opening-door-leaving-home-work-144597437.jpg", "content": "Kings are the best team in the NBA!"},
#         { "id": "9",'name': "Laci", "avatar": "https://www.unomaha.edu/news/2019/04/img/20190326_deena_keilany.jpg", "content": "Found an internship."},
#         { "id": "10",'name': "Deon", "avatar": "https://www.wonderwall.com/photos/2014/03/28/104-135619_Actual.jpg?x=576&y=800&icq=74&sig=8473cf9ce8a4ca14516d7ce2b00c49de", "content": "This app is cool."},
#         { "id": "11",'name': "Neveah", "avatar": "https://i.pinimg.com/736x/c8/1a/8b/c81a8b6bcee899a76686672e8832863e--professional-headshots-corporate-headshots.jpg", "content": "Mamba Mentality."},
#         { "id": "12",'name': "Donavan", "avatar": "https://d1vwxdpzbgdqj.cloudfront.net/assets/professional-courses/professional-banner-e0c1ba5a4c2d6b53708b17d8c1fc6b79d59e7328e42f6490832acf7511c2a3e3.jpg", "content": "Has anyone read the Biography of Leonardo DaVinci?"},
#         { "id": "13",'name': "Selena", "avatar": "https://www.weinstocklaw.com/wp-content/uploads/attorney_sukhija.jpg", "content": "Yes!"},
#         { "id": "14",'name': "Harrison", "avatar": "https://th.bing.com/th/id/OIP.BjoFdhjoR3-IRBrt-bjnSgHaHa?pid=ImgDet&rs=1", "content": "Should I do a minor?"},
#         { "id": "15",'name': "Cali", "avatar": "https://images.squarespace-cdn.com/content/v1/572e050c4d088ea3a8f0ac9d/1652567766499-UNBUKR33P595WUKRYBO5/Nall_Miller-10-6-21-2834-PRINT.jpg?format=1000w", "content": "Will NFT's make a comeback?"},
#         { "id": "16",'name': "Rowan", "avatar": "https://th.bing.com/th/id/OIP.K9xDLlPZCudB_Kl1guvy8QHaLH?pid=ImgDet&w=1200&h=1800&rs=1", "content": "How does population decline affect real estate prices?"},
#         { "id": "17",'name': "Cheyenne", "avatar": "https://jcpportraits.com/wp-content/uploads/2021/11/224-081-JCP-1080x1080-Gallery-Business-1.jpg", "content": "Kevin Durant is taking the suns to a championship."},
#         { "id": "18",'name': "Guillermo", "avatar": "https://www.boredart.com/wp-content/uploads/2019/04/Top-Examples-of-Professional-Headshots4.jpg", "content": "I will be moonwalking across campus today at 3pm."},
#         { "id": "19",'name': "Jazlyn", "avatar": "https://content.latest-hairstyles.com/wp-content/uploads/professional-short-and-textured-pixie-hairstyle.jpg", "content": "I need to get my cap and gown."},
#         { "id": "20",'name': "Dan", "avatar": "https://cdn.lifehack.org/wp-content/uploads/2015/04/photo-3.png", "content": "Bruh!"},
#     ]
#     return jsonify(post)

# def get_friends():
#     friends =  [
#             {
#                 "id": "0",
#                 "image": "https://randomuser.me/api/portraits/men/58.jpg",
#                 "name": "Jerry",
#             },
#             {
#                 "id": "1",
#                 "image": "https://randomuser.me/api/portraits/women/3.jpg",
#                 "name": "Olivia",
#             },
#             {
#                 "id": "2",
#                 "image": "https://randomuser.me/api/portraits/men/86.jpg",
#                 "name": "Ben",
#             },
#             {
#                 "id": "3",
#                 "image": "https://randomuser.me/api/portraits/women/18.jpg",
#                 "name": "Amelia",
#             },
#             {
#                 "id": "4",
#                 "image": "https://randomuser.me/api/portraits/men/4.jpg",
#                 "name": "Liam",
#             },
#             {
#                 "id": "5",
#                 "image": "https://randomuser.me/api/portraits/women/90.jpg",
#                 "name": "Sophia",
#             },
#             ]
#     return jsonify(friends)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
