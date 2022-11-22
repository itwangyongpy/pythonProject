from core.basecase import BaseCase
import random
from pojo import MeetingRoom


class TestMeetingRoom(BaseCase):

    def test1_add_meetingroom(self):
        """
        添加会议室
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/oa/meetingroom/add?access_token={self.token}"
        adddata = {
            "name": f"{random.random()}F-会议室",
            "capacity": 10,
            "city": "深圳",
            "building": "腾讯大厦",
            "floor": "18F",
            "equipment": [1, 2, 3],
            "coordinate":
                {
                    "latitude": "22.540503",
                    "longitude": "113.934528"
                }
        }
        r = self.requests(method='post', url=url, json=adddata)
        # 添加断言
        self.assertEqual(r.json()["errcode"], 0)
        self.assertEqual(r.json()["errmsg"], "ok")

        # 设置上下游传参
        MeetingRoom.meetingroom_id = r.json()["meetingroom_id"]

    def test2_query_meetingroom(self):
        """
        查询会议室
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/oa/meetingroom/list?access_token={self.token}"
        query_data = {
            "city": "深圳",
            "building": "腾讯大厦",
            "floor": "18F",
            "equipment": [1, 2, 3]
        }
        r = self.requests(method="post", url=url, json=query_data)
        meetingroom_list = r.json()["meetingroom_list"]
        tmplist = []
        for meetingroom in meetingroom_list:
            tmplist.append(meetingroom["meetingroom_id"])
        # print(tmplist)
        # 添加断言
        # 上面添加的meetingroom_id应该在 templist中
        self.assertTrue(MeetingRoom.meetingroom_id in tmplist)

    def test3_delete_meetingroom(self):
        """
        删除会议室（用到添加会议室接口返回数据中的meetingroom_id 字段）
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/oa/meetingroom/del?access_token={self.token}"
        deletedata = {
            "meetingroom_id": MeetingRoom.meetingroom_id,
        }
        r = self.requests(method="post", url=url, json=deletedata)
        # 添加断言
        self.assertEqual(r.json()["errcode"], 0)
        self.assertEqual(r.json()["errmsg"], "ok")
