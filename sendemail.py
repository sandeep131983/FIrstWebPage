import smtplib
import ssl
def email(message):
    host1="smtp.gmail.com"
    port1=465
    receiver="sandeep13feb1983@gmail.com"
    username="sandeep13feb1983@gmail.com"
    password="wqcggapymyjrpzen"

    context=ssl.create_default_context()

    with smtplib.SMTP_SSL(host=host1,port=port1,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)