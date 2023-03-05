from flask import render_template
import config
from domain.models import Account
from domain.models import Users
from domain.models import Posts
# from flask_cors import CORS

app = config.connex_app
app.add_api("swagger.yml")
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/")
def home():
    account = Account.query.all()
    user = Users.query.all()
    post = Posts.query.all()
    return render_template("home.html", account=account, user=user, post=post)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
