from abc import ABC, abstractmethod

# Step 1: Define an Interface
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

# Step 2: Concrete Implementations
class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending Email with message: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS with message: {message}")

class PushNotification(Notification):
    def send(self, message):
        print(f"Sending Push Notification with message: {message}")

# Step 3: Factory Class
class NotificationFactory:
    def create_notification(self, notification_type):
        if notification_type == 'email':
            return EmailNotification()
        elif notification_type == 'sms':
            return SMSNotification()
        elif notification_type == 'push':
            return PushNotification()
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")

# Client Code
def send_notification(notification_type, message):
    factory = NotificationFactory()
    notification = factory.create_notification(notification_type)
    notification.send(message)

# Usage
send_notification('email', 'Hello via Email!')
send_notification('sms', 'Hello via SMS!')
send_notification('push', 'Hello via Push Notification!')
