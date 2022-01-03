
class MailServer:
    def getMessage(self):
        pass


class TemplateEngine:
    def sendMessage(self, message):
        pass


class Messenger:
    def __init__(self):
        self.template_engine = TemplateEngine()
        self.mail_server = MailServer()

    def receiveMessage(self):
        message = self.mail_server.getMessage()
        return f"Received message: \"{message}\""

    def getAndSendMessage(self):
        message = self.mail_server.getMessage()
        return self.template_engine.sendMessage(message)



