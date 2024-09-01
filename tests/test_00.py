from unittest import TestCase
from my_class import Event

class EventTest(TestCase):
    def test_availability(self):
        # Event を作る
        event = Event(id=1)

        # 空席状況を取得する
        availability = event.check_availability()

        # いずれかの空席状況が返ってきたことを確認する
        self.assertIn(availability, ['完売', '残り僅か', '余裕あり'])
