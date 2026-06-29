class NotificationSystem:
    def notification(self,messages):
        print("notification is send hello pavan")
class EmailNotification(NotificationSystem):
    def notification(self,messages):
        print("notification is send by email your money wii be credited")
class SMSNotification(NotificationSystem):
    def notification(seelf,messages):
        print("notification is send by sms your balance is over")
class googleNotification(NotificationSystem):
    def notification(self,messages):
        print("notification is send by google new movie will be released")
class whatsappNotification(NotificationSystem):
    def notification(self,messages):
        print("notification is send by whatsapp your lover is send a message")
class facebookNotification(NotificationSystem):
    def notification(self,massages):
        print("notification is send by new information is available")
class twitterNotification(NotificationSystem):
    def notification(slef,masseges):
        print("notification is send by upgrade in twitter")
notification=[EmailNotification(),SMSNotification(),googleNotification(),whatsappNotification(),facebookNotification(),twitterNotification()]
messages=input("enter the messages:")
print("you have chosen",messages)
print("\n------notification methods---\n")
for notifications in notification:
    notifications.notification(messages)        
