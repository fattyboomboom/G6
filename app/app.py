from flask import render_template
import config
from domain.modelDemo import Account

app = config.connex_app
app.add_api("swagger.yml")


@app.route("/")
def home():
    account = Account.query.all()
    return render_template("home.html", account=account)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
