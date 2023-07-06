import smtplib
import ssl


def send_email(subject, message):
    host = "smtp.gmail.com"
    port = 465

    username = "curtis4ridaz@gmail.com"
    password = "efeikwoyofwhhzzs"

    receiver = "chyka9632@gmail.com"
    email_message = f"Subject: {subject}\n\n{message}"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, email_message)


if __name__ == "__main__":
    print("Successfully sent")
