import unittest

# dataclassを使わない場合
class Person:
    def __init__(self, number, name='XXX') -> None:
        self.number = number
        self.name = name
        
from dataclasses import dataclass
# dataclassを使う場合　
@dataclass 
class DataclassPerson:
    number: int
    name: str = 'XXX'
    
def main():
    person1 = Person(0, 'Alice')
    print(person1) # __repr__(そのオブジェクトを表現representationするための文字列を返すメソッド)が生成されないため、<__main__.Person object at 0x7f135a7afbb0>が返る
    print(person1.number)
    print(person1.name)
    
    print("-----")
    dataclass_person1 = DataclassPerson(0, 'Alice')
    print(dataclass_person1) # @dataclassを使うと、自動的にわかりやすい__repr__が生成されるため、DataclassPerson(number=0, name='Alice')が表示される
    print(dataclass_person1.number)
    print(dataclass_person1.name)
    

class TestDataClassPerson(unittest.TestCase):
    def test_person_name(self):
        dataclass_person1 = DataclassPerson(0, 'Alice')
        self.assertEqual(dataclass_person1.name, 'Alice')

    def test_person_number(self):
        dataclass_person1 = DataclassPerson(0, 'Alice')
        self.assertEqual(dataclass_person1.number, 0)
        
    def test_person_name_equality(self):
        person1 = Person(0, 'Alice') 
        dataclass_person1 = DataclassPerson(0, 'Alice')
        
        self.assertEqual(person1.name, dataclass_person1.name)
        
    def test_person_equality(self):
        person1 = Person(0, 'Alice') 
        dataclass_person1 = DataclassPerson(0, 'Alice')
        
        self.assertEqual(person1, dataclass_person1) # このテストは失敗する

if __name__ == "__main__":
    TEST_MODE = False
    
    if TEST_MODE:
        unittest.main()
    else:  
        main()
    