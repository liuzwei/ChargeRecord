import requests
import json

mainUrl = "http://batteryzuul.w-oasis.com/"
loginUrl = "ebd/api/login"
getByBsuUrl = "ebd/api/getBatteryNoByFollowBMS"

class HttpUtil():

    def __init__(self):
        self.url = mainUrl
    # 登陆
    def login(self, **kargs):
        params = {"username":kargs['username'], "passwd":kargs['passwd']}
        headers = {"Content-Type":"application/json"}
        response = requests.post(self.url+loginUrl, data=json.dumps(params), headers=headers)
        result = {"code":response.status_code}
        if response.content != None:
            result['data'] = response.json()
        return result
    #根据从板获取电池组编号
    def getByBsucode(self, **kargs):
        params = {"followbmsno":kargs["followbmsno"]}
        headers = {"Content-Type": "application/json"}
        response = requests.get("http://10.0.0.170:8004/data/getBatteryNoByFollowBMS", data=json.dumps(params), headers=headers)
        result = {"data": response.json(), "code": response.status_code}
        return result

if __name__ == '__main__':
    httpUtil = HttpUtil()
    # result = httpUtil.login(username='15001101535', passwd='123456')
    result = httpUtil.getByBsucode(followbmsno='0B2224690118')
    if result['code']==200:
        print("请求成功\n")
        print(result)
    elif result['code']==404:
        print("地址无效404",result['data'])