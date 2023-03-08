from flask import render_template
import config
from domain.models import Account
from domain.models import Users
from domain.models import Posts
from domain.models import UserToken


# from flask_cors import CORS

app = config.connex_app
app.add_api("swagger.yml")
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/")
def home():
    account = Account.query.all()
    user = Users.query.all()
    post = Posts.query.all()
    userToken = UserToken.query.all()
    return render_template("home.html", account=account, user=user, post=post, userToken=userToken)

# @app.route('/process', methods=['POST', 'GET'])
# def FilterProfanity():
#     submission = request.get_data()
#     process = str(submission, 'utf-8')

#     if request.method == 'POST':
#         if len(process) > 12:
#             output = CheckProfanity(process)
#             if output:
#                 return jsonify({ 'status' : 'failed', 'profanity' : output}), 403
#             return jsonify({
#                 'status' : 'success',
#                 'profanity' : output,
#                 # 'test' : process
#                 })
#         return abort(406,  description="Please return a submission!")
#     return 'get'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
