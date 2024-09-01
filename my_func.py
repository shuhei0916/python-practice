import random

def get_available_seats(event_id: int) -> int:
    '''残席数を返す関数 (関数 B)
    '''
    # 残席数 (本来はデータベースに問い合わせるが、ここでは乱数)
    available_seats = random.randint(0, 100)

    return available_seats
