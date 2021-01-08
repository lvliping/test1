# coding=utf-8
from api.standard_topic import QueryTopic
import unittest
from unittest import TestCase, TestSuite, TextTestRunner

class QueryTopicCase(TestCase):
    def test_query_succeed(self):
        query_topic = QueryTopic(relateType=" ", topicKey=" ")
        self.assertTrue(query_topic)
if __name__ == '__main__':
    case = QueryTopicCase("test_query_succeed")
    suite = TestSuite()
    suite.addTest(case)
    TextTestRunner().run(suite)
    # unittest.main()