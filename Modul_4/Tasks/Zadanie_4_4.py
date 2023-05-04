import sys
import logging
logging.basicConfig(level=logging.INFO)

def add(*args):
    result = sum(args)
    logging.info(f"Dodaję liczby {args}. Wynik {result}")
    
def subs(a, b):
    result = a - b
    logging.info(f"Odejmuję liczbę {b} od {a}. Wynik {result}")
    
def multi(*args):
    result = 1
    for x in args:
        result *= x
    logging.info(f"Mnożę liczby {args}. Wynik {result}")
    
def divide(a, b):
    if b == 0:
        logging.warning("Dzielenie przez 0 jest niedozwolone")
    else:
        result = a / b
        logging.info(f"Dzielę liczbę {a} przez {b}. Wynik {result}")

def wrong_task():
    logging.warning("Wybierz poprawne działanie")
    sys.exit()

if __name__ == "__main__":
    task = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    
    if task in [1, 3]:
        nums = input("Podaj liczby oddzielone spacjami: ")
        nums_list = [int(num.strip()) for num in nums.split(" ")]
    elif task in [2, 4]:
        a = int(input("Podaj pierwszą liczbę: "))
        b = int(input("Podaj drugą liczbę: "))
    
    if task == 1:
        result = add(*nums_list)
    elif task == 2:
        result = subs(a, b)
    elif task == 3:
        result = multi(*nums_list)
    elif task == 4:
        result = divide(a, b)
    else:
        wrong_task()