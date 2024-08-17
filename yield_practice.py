def simple_generator():
    yield 1
    yield 2
    yield 3
    
def main():
    gen = simple_generator()
    
    print(next(gen))
    print(next(gen))
    print(next(gen))
    
if __name__ == "__main__":
    main()
    