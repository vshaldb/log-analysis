import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

class email:
    def __init__(self, msg):
        self.msg = msg

    def sendEmail(self):
        message = Mail(
            from_email='from_email@example.com',
            to_emails='to_email@example.com',
            subject='Error - We Found an error in your application',
            html_content=self.msg
        try:
            #set your api key as a value for SENDGRID_API_KEY environment variable
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            sg.send(message)
        except Exception as e:
            print(e.message)
