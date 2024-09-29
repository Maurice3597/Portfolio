import smtplib, ssl
import pandas
def send_mail(message):
    username = "datascienceandaienegneer@gmail.com"
    password = 'ecri eafn hsxa wgqy'

    host = 'smtp.gmail.com'
    port = 465
    receiver = "gobackenddevelopment@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context= context)as  server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

def topic():
    topics = pandas.read_csv("topics.csv")
    for index, topic in topics.iterrows():
        return topics["topic"]
topic()