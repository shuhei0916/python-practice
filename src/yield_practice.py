import unittest

def simple_generator():
    yield 1
    yield 2
    yield 3
    
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def main():
    gen = simple_generator()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    
    fib_gen = fibonacci()
    for _ in range(10):
        print(next(fib_gen))
    
    
class TestYieldFunctions(unittest.TestCase):
    def test_simple_generator(self):
        gen = simple_generator()
        self.assertEqual(next(gen), 1)
        self.assertEqual(next(gen), 2)
        self.assertEqual(next(gen), 3)
        
    def test_fibonacci_generator(self):
        gen = fibonacci()
        expected_values = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] 
        for expected in expected_values:
            self.assertEqual(next(gen), expected)
        

if __name__ == "__main__":
    TEST_MODE = True
    
    if TEST_MODE:
        unittest.main()
    else:  
        main()
    