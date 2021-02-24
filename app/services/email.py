import sendgrid
from sendgrid.helpers.mail import Mail
from app.constants import SENDGRID_API_KEY, FROM_EMAIL


def send_invitation_email(emails: [str], inviter, link):
    sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=emails,
        subject="{} invited you to join an Heirloom page".format(inviter),
        html_content=link)
    sg.send(message)
