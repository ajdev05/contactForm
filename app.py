from flask import *
import emailActions

app = Flask(__name__)

# Edit emailActions.py to send emails and messages




@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        phone = request.form['phone']
        message = request.form['message']

        # Mailing
        cMail = emailActions.emailContact.SendEmail_user(name, email, subject)
        print(cMail)
        adminMail = emailActions.emailContact.SendEmail_admin(name,email,subject,phone,message)
        print(adminMail)
        # End mailing

    return render_template("html/contactForm.html")




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
