import smtplib, ssl
import pandas, os
from dotenv import load_dotenv

load_dotenv(".env")
passkey = os.environ.get("PASSKEY")
user_mail = os.environ.get("EMAIL")
PORT= os.environ.get("PORT")
HOST = os.environ.get("HOST")


def send_mail(message, password =passkey, mail = user_mail):
    password = passkey
    user_email= mail

    host = HOST
    port = PORT
    receiver = "gobackenddevelopment@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context= context)as  server:
        server.login(user_email, password)
        server.sendmail(user_email, receiver, message)

def topic():
    topics = pandas.read_csv("topics.csv")
    for index, topic in topics.iterrows():
        return topics["topic"]
topic()


print(f"{user_mail}\n{passkey}\n{HOST}\n{PORT}")