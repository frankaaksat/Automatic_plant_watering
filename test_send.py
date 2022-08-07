import smtplib, ssl

port = 465  # For SSL
password = "_B@rcelona44443424"

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("frank.dev22@gmail.com", password)
    sender_email = "frank.dev22@gmail.com"
    receiver_email = "frank_a94@hotmail.com"
    message = """\
    Subject: Hi there

    This message is sent from Python."""
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    print("the email was succesfully sent")
    