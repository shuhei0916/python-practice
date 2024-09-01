from my_func import get_available_seats

class Event:
    '''イベント
    '''
    def __init__(self, id: int):
        self.id = id

    def check_availability(self):
        '''空席状況を返す関数 (関数 A)
        '''
        # 残席数と座席数を取得する
        available_seats = get_available_seats(self.id)

        if available_seats == 0:
            return '完売'
        elif available_seats < 20:
            return '残り僅か'
        else:
            return '余裕あり'
