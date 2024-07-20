import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "tt.test.159753159753@gmail.com"
    password = "dumj kllh cpvc pnnd"
    receiver = "tt.test.159753159753@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)



