import pandas
from flask import Flask, render_template, request
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
import resend


load_dotenv()
app = Flask(__name__)
email = os.environ["EMAIL"]
resend.api_key = os.environ["RESEND_API_KEY"]
app.config["MAIL_SERVER"]="smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = email
app.config["MAIL_PASSWORD"] = os.environ["EMAIL_PASSWORD"]
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
mail = Mail(app)
products_info = pandas.read_excel("products.xlsx").to_dict(orient="records")
gallery_info = pandas.read_excel("gallery.xlsx").to_dict(orient="records")


@app.route("/", methods = ["GET", "POST"])
def main_page():
    if request.method == "POST" and request.form.get('username'):
        username = request.form.get("username")
        phone = request.form.get("phone")
        user_email = request.form.get("email")
        msg = Message("Thanks", sender = email, recipients = [user_email])
        msg.body = f"Hello {username}. Thanks for your order!"
        mail.send(msg)
        print("Sended")
    return render_template(
        "template.html", 
        products_info=products_info,
        gallery_info=gallery_info
    )


if __name__ == "__main__":
    app.run(debug=True)