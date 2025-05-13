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
    return a * b
