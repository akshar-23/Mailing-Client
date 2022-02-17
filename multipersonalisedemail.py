import smtplib, ssl, csv


message = """Subject: Your Result Grade

Hello {name}, Your grade is {grade}"""

from_address = "my@gmail.com" #gmail id of the email through which you want to send personalised mail
password = input('Enter your password: ')

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
    server.login(from_address,password)
    with open("contacts.csv") as file:
        reader = csv.reader(file)
        next(reader) #skip header
        for name,email,grade in reader:
            server.sendmail(from_address,email,message.format(name=name, grade=grade))