# calc.py
import logging
logging.basicConfig(level=logging.INFO)

def add(a, b):
    logging.info(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    logging.info(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    logging.info(f"Multiplying {a} * {b}")
    return a * b

def power(a, b):
    logging.info(f"Power calculation: {a} ** {b}")
    return a ** b

def divide(a, b):
    if b == 0:
        logging.error("Attempted to divide by zero.")
        raise ValueError("Cannot divide by zero")
    logging.info(f"Dividing {a} / {b}")
    return a / b
