import yagmail
reciever = "your@gmail.com" #email id of the reciever
body = "Hello there from Yagmail"
filename = "ironman.jpg" #file path of the attachment

yag = yagmail.SMTP("my@gmail.com", "yourpassword") # the password and the gmail id should be of the one you want to send email from
#though the above method is not recommended 
#instead you can add your Gmail validations to the keyring of your OS.
yag.send(
    to = reciever,
    subject = "yagmail email with attachment",
    contents = body,
    attachments = filename
)
