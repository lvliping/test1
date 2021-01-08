# coding=utf-8
from commen import config
import requests


class QueryTopic:
    parent_name = []
    topic_code = []
    def __init__(self, relateType=None, topicKey=None, cookies=None):
        query_url = config.url + "dam_cqcbank/api/dev/dptopic/top"
        self.relateType = relateType
        self.topicKey = topicKey
        if relateType and topicKey:
            query_data = {
                "relateType": self.relateType,
                "topicKey": self.topicKey
            }
            self.query_res = requests.get(query_url, params=query_data)
        if not relateType and topicKey:
            if relateType is None:
                query_data = {
                    "topicKey": topicKey
                }
                self.query_res = requests.get(query_url, params=query_data)
            else:
                query_data = {
                    "relateType": relateType,
                    "topicKey": topicKey
                }
                self.query_res = requests.get(query_url, params=query_data)
        if relateType and not topicKey:
            if topicKey is None:
                query_data = {
                    "relateType": relateType,
                }
                self.query_res = requests.get(query_url, params=query_data)
            else:
                query_data = {
                    "relateType": relateType,
                    "topicKey": topicKey
                }
                self.query_res = requests.get(query_url, params=query_data)
        self.code = self.query_res.status_code
        self.content = self.query_res.json()
        for name in content:
            self.parent_name = name.get("parent_name")
            self.topic_code = name.get("topic_code")
    def query_Succeed(self):
        if (self.code == 200 and self.topicKey in self.parent_name) or \
                (self.code == 200 and self.topicKey in self.topic_code):
            return True
        else:
            print("没有符合条件的数据", "状态码", self.code, "查询结果", self.content)
            return False

    def query_failed(self, msg):
        code = self.query_res.status_code
        content = self.query_res.json()
        if code == 200 and content == msg:
            return True
        else:
            print("查询失败", self.code, self.content)
            return False


if __name__ == '__main__':
    query = QueryTopic(relateType=" ", topicKey="ceshi")
    query.query_Succeed()
