import unittest
from assertpy import *
from unittest.mock import *
from zad2.src.subscriber import Subscriber


class SubscriberTest(unittest.TestCase):
    def setUp(self):
        self.temp = Subscriber()

    def test_add_person(self):
        self.temp.add_person = Mock()
        self.temp.add_person.return_value = "Person Julia added to list!"
        assert_that(self.temp.add_person("Julia")).is_equal_to("Person Julia added to list!")

    def test_add_person_that_exists(self):
        self.temp.add_person = Mock()
        self.temp.add_person.side_effect = Exception("This person already exist!")
        assert_that(self.temp.add_person).raises(Exception).when_called_with("Jan")

    def test_delete_person(self):
        self.temp.delete_person = Mock()
        self.temp.delete_person.return_value = "Person Julia deleted from list!"
        assert_that(self.temp.delete_person("Julia")).is_equal_to("Person Julia deleted from list!")

    def test_add_delete_that_doesnt_exist(self):
        self.temp.delete_person = Mock()
        self.temp.delete_person.side_effect = Exception("This person doesn't exist!")
        assert_that(self.temp.delete_person).raises(Exception).when_called_with("Jan")

    def test_send_message(self):
        self.temp.send_message = Mock()
        self.temp.send_message.return_value = "Message \"Hello!\" sent to Julia"
        assert_that(self.temp.send_message("Julia", "Hello!")).is_equal_to("Message \"Hello!\" sent to Julia")

    def test_send_message_to_person_that_doesnt_exist(self):
        self.temp.send_message = Mock()
        self.temp.send_message.side_effect = Exception("This person doesn't exist!")
        assert_that(self.temp.send_message).raises(Exception).when_called_with("Jan", "Hello!")