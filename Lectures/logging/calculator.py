import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt= '%d-%m-%Y %H-%M-%S',
    force = True,
    handlers=[
        logging.FileHandler('calculator.log'),
        logging.StreamHandler()
    ]
)

logger1 = logging.getLogger("calculator")

def add(a,b):
    logger1.info(f"Adding {a} and {b} i.e {a} + {b} = {a+b}")
    return a+b
def subtract(a,b):
    logger1.info(f"Subtracting {a} and {b} i.e {a} - {b} = {a-b}")
    return a-b
def divide(a,b):
    logger1.info(f"Dividing {a} and {b} i.e {a} / {b} = {a/b}")
    return a/b
def multiply(a,b):
    logger1.info(f"Multiply {a} and {b} i.e {a} * {b} = {a*b}")
    return a*b

add(3,4)
subtract(3,2)
divide(4,2)
multiply(4,5)