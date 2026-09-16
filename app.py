import pandas
from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import resend
from resend.exceptions import ResendError
from typing import Final


PRODUCTS_INFO: Final = pandas.read_excel("products.xlsx").to_dict(orient="records")
GALLERY_INFO: Final = pandas.read_excel("gallery.xlsx").to_dict(orient="records")


app = Flask(__name__)
@app.route("/", methods = ["GET", "POST"])
def main_page():
    if request.method == "POST" and request.form.get('username'):
        username = request.form.get("username")
        phone = request.form.get("phone")
        user_email = request.form.get("email")
        params: resend.Emails.SendParams = {
            "from": "Sweetchest <onboarding@resend.dev>",
            "to": [user_email],
            "subject": "Thanks",
            "html": f"Hello {username}. Thanks for your order!",
        }
        try:
            email = resend.Emails.send(params)
        except ResendError as error:
            print(error)
    return render_template(
        "template.html", 
        products_info=PRODUCTS_INFO,
        gallery_info=GALLERY_INFO
    )


if __name__ == "__main__":
    load_dotenv()
    resend.api_key = os.environ["RESEND_API_KEY"]
    app.run(debug=True)