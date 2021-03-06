from flask.ext.mail import Message 
from app import mail
from flask import current_app
from flask import  render_template
def send_email(to, subject, template, **kwargs): 
    msg = Message(current_app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject, 
                  sender=current_app.config['FLASKY_MAIL_SENDER'], recipients=[to]) 
    msg.body = render_template(template, **kwargs) 
    msg.html = render_template(template, **kwargs) 
    mail.send(msg)