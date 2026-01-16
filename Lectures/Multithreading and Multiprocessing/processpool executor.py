import time
from concurrent.futures import ProcessPoolExecutor
def compute_squares(i):
    time.sleep(2)
    return f"The square of {i}: {i*i}"

numbers = [1,3,45,6,8,9,54,2,2]
if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=3) as executor:
        result = executor.map(compute_squares,numbers)
    
    for i in result:
        print(i)