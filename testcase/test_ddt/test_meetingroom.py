from ddt import ddt, data, unpack
from core.basecase import BaseCase


@ddt
class TestMeetingRoom(BaseCase):
    @data(["1234563432156789345222987543391", 40058], ["", 40058])
    @unpack
    def test_add_meetingroom(self, name, expect_errcode):
        """
        测试异常场景
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/oa/meetingroom/add?access_token={self.token}"
        adddata = {
            "name": name,
            "capacity": 10,
            "city": "深圳",
            "building": "腾讯大厦",
            "floor": "18F",
            "equipment": [1, 2, 3]
            "coordinate":
                {
                    "latitude": "22.540503",
                    "longitude": "113.934528"
                }
        }
        r = self.requests(method='post', url=url, json=adddata)
        # 添加断言
        self.assertEqual(r.json()["errcode"], expect_errcode)
        # self.assertEqual(r.json()["errmsg"], "ok")
