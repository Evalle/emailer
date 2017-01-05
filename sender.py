import smtplib


def send_emails(emails, forecast, username, password):
    # Connect to smtp server
    server = smtplib.SMTP('smtp.gmail.com', '587')
    # Start encryption
    server.starttls()
    # Login
    server.login(username, password)

    # Send to whole mail list
    for to_email, name in emails.items():
        message = 'Subject: Weather forecast for today\n'
        message += 'Hi ' + name + '!\n\n'
        message += forecast + '\n\n'
        message += 'Cheers, your email forecast app'
        server.sendmail('emailer.app11@gmail.com', to_email, message)
    server.quit()
