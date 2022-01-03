import unittest
from assertpy import *
from unittest.mock import *
from zad3.src.messenger import Messenger


class TestMessage:
    def setUp(self):
        self.temp = Messenger()

    def test_receive_message(self):
        self.temp.mail_server.getMessage = Mock()
        self.temp.mail_server.getMessage.return_value = "Hello!"
        assert_that(self.temp.receiveMessage()).is_equal_to("Received message: \"Hello!\"")

    def test_receive_message_empty(self):
        self.temp.mail_server.getMessage = Mock()
        self.temp.mail_server.getMessage.side_effect = Exception("No message to be received!")
        assert_that(self.temp.receiveMessage)\
            .raises(Exception)\
            .when_called_with()\
            .contains("No message to be received!")

    def test_send_message(self):
        self.temp.template_engine.sendMessage = Mock()
        self.temp.template_engine.sendMessage.return_value = "Message \"Hello\" has been sent!"
        assert_that(self.temp.getAndSendMessage()).is_equal_to("Message \"Hello\" has been sent!")

    def test_send_message_not_succesfully(self):
        self.temp.mail_server.getMessage = Mock()
        self.temp.mail_server.getMessage.side_effect = \
            Exception("The message was not sent successfully. Please try again...")
        assert_that(self.temp.getAndSendMessage)\
            .raises(Exception)\
            .when_called_with()\
            .contains("The message was not sent successfully. Please try again...")