from my_class import Event

# Event を作る
event = Event(id=1)

# 空席状況を取得する
availability = event.check_availability()

print(availability)
