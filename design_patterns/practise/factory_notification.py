from abc import abstractmethod,ABC

class AbstractNotification(ABC):
    @abstractmethod
    def send():
        """
        Whichever classes inherit from AbstractNotification must implement send method. 
        """
        pass
    def confirm_message(self):
        print("sending notification from AbstractNotification")

class NotificiationClass(ABC):
    @abstractmethod
    def send():
        """
        Whichever classes inherit from AbstractNotification must implement send method. 
        """
        pass

    def confirm_message(self):
        print("sending notification from Notification class")

class EmailNotification(AbstractNotification,NotificiationClass):
    def send(self):
        print("I was sent from Email class")

class SMSNotification(AbstractNotification,NotificiationClass):
    def send(self):
        print("I was sent from SMS class")    

class Factory:
    def __init__(self,type):
       self.type=type
    def create_notification(self):
        if self.type=='email':
            return EmailNotification()

        elif self.type=='sms':
            return SMSNotification()
        else:
            return None

obj=Factory('sms')
notification_obj=obj.create_notification()
notification_obj.send()
notification_obj.confirm_message()


        

