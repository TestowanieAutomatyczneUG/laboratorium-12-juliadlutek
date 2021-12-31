import unittest
import requests
from assertpy import *


class RandomUserTest(unittest.TestCase):
    def setUp(self):
        self.temp = requests.get("https://randomuser.me/api/").json()

    def test_correct_format(self):
        assert_that(self.temp).contains_key("results", "info")

    def test_results_amount(self):
        assert_that(self.temp["results"]).is_length(1)

    def test_results_correct_format(self):
        assert_that(self.temp["results"][0]).contains_key("gender", "name", "location", "email", "login", "dob",
                                                          "registered", "phone", "cell", "id", "picture", "nat")

    def test_info_correct_format(self):
        assert_that(self.temp["info"]).contains_key("seed", "results", "page", "version")

    def test_name_type(self):
        assert_that(self.temp["results"][0]["name"]["first"]).is_type_of(str)

    def test_age_type(self):
        assert_that(self.temp["results"][0]["dob"]["age"]).is_type_of(int)
