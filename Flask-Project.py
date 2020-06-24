from flask import Flask
from flask import render_template
#from processing import send_email
#import smtplib, ssl


app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')
if __name__ == '__main__':
   app.run()


#def send_email(message, email, name):
    #port = 465  # For SSL
    #smtp_server = "smtp.gmail.com"
    #sender_email = "matthewtlharvey@gmail.com"
    #receiver_email = "matthewtlharvey@gmail.com"
    #password = "Password"
    #message = message + email + name
    #context = ssl.create_default_context()
    #with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        #server.login(sender_email, password)
        #server.sendmail(sender_email, receiver_email, message)

#@app.route('/foo', methods=["POST"])
#def foo_page():
    #req_data = request.get_json()
    #message = req_data['message']
    #email = req_data['email']
    #name = req_data['name']
    #send_email(message, email, name)
    #return
