import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import pytz

class emailContact:
    smpt_host = ""
    smpt_port = int("")
    def showDatetime():
        format = "Inquiry Date: %d/%m/%y | %I:%M%p EST"
        converted_tz = pytz.timezone('US/Eastern')
        datetime_object = datetime.datetime.now(converted_tz)
        retTime = f"{datetime_object.strftime(format)}"

        return retTime





    def SendEmail_user(name,userEmail, userSubject):
        sender_email = 'your_email'
        sender_password = 'your_password'

        recipient_email = userEmail

        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email

        message['Subject'] = 'Contact - Your Company'
        text_body = f'Dear {name},'

        html_body = f"""
        <html>
            <body>
                <p>We trust this message finds you well.</p>

                <p>This email is in response to your recent inquiry about: <strong>{userSubject}</strong>. </p>

                <p>We appreciate your interest and would like to assure you that your request has been received, and you will receive a follow-up as soon as possible.</p>

                <p>Should you have any further questions or require additional assistance, please do not hesitate to reach out to us.</p>
                <br>
            
                <p>Thank you for considering us.</p>
                <br>
                <p>Kind Regards,</p>
                <p>Your Company.</p>
                <p>{emailContact.showDatetime()}</p>


                <p style="font-size: 80%; color: #888;">This email address is a do not reply address. Please do not reply to this email as replies will not be monitored.</p>
            </body>
        </html>
        """


        message.attach(MIMEText(text_body, 'plain'))
        message.attach(MIMEText(html_body, 'html'))


                 # Enter you SMPT information to send emails  

        with smtplib.SMTP(smpt_host, smpt_port) as server:
            server.starttls()

            server.login(sender_email, sender_password)

            server.sendmail(sender_email, recipient_email, message.as_string())

        return('Email sent successfully to user!')

    def SendEmail_admin(name,userEmail, userSubject, userPhoneNumber, userMessage):
        sender_email = 'your_email'
        sender_password = 'your_password'

        recipient_email = "admin_email/s"

        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email

        
        message['Subject'] = 'New contact from user'
        text_body = f'Dear Admin,'

        html_body = f"""
        <html>
            <body>
                <p>New Request.</p>
                <br>
                
                <p>Contactors Name: <strong>{name}</strong> </p>
                <p>Contactors Email: <strong>{userEmail}</strong> </p>
                <p>Contactors Subject: <strong>{userSubject}</strong> </p>
                <p>Contactors Phone Number: <strong>{userPhoneNumber}</strong> </p>
                <p>Contactors Message: <strong>{userMessage}</strong> </p>
                <p>Contactors Datetime: {emailContact.showDatetime()}</p>

                <br>
                <p>Kind Regards,</p>
                <p>Your Company.</p>

                <p style="font-size: 80%; color: #888;">This email address is a do not reply address. Please do not reply to this email as replies will not be monitored.</p>
            </body>
        </html>
        """


        message.attach(MIMEText(text_body, 'plain'))
        message.attach(MIMEText(html_body, 'html'))

         # Enter you SMPT information to send emails 
        with smtplib.SMTP(smpt_host, smpt_port) as server:
            server.starttls()

            server.login(sender_email, sender_password)

            server.sendmail(sender_email, recipient_email, message.as_string())

        return('Email sent successfully to Admin!')


