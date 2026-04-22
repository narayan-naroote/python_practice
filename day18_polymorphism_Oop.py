#POLYMORPHISM
class Notification:
    def send(self):
        print("Sending notification...")

class SMSNotification(Notification): #Inherits
    def send(self):
        print("SMS sent....")

class EmailNotification(Notification):
    def send(self):
        print("Email sent....")

# Polymorphism
notifications = [SMSNotification(), EmailNotification()]

for n in notifications:
    n.send()