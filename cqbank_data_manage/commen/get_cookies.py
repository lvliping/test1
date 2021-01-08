# coding=utf-8

import requests
from commen import config

DTL_SESSION_ID = None
def get_session():
    global DTL_SESSION_ID
    if DTL_SESSION_ID:
        return DTL_SESSION_ID
    else:
        login_url = config.url + "dam_cqcbank/login"
        login_data = {"userID": config.username,
                      "pwd": config.password
                      }
        login_res = requests.post(login_url, data=login_data)

        # print(login_res.status_code)
        # print(login_res.cookies.get_dict())
        DTL_SESSION_ID = login_res.cookies.get_dict().get("DTL_SESSION_ID")
        return DTL_SESSION_ID
if __name__ == '__main__':
    get_session()
    print(DTL_SESSION_ID)
