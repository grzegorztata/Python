import sys
import logging
logging.basicConfig(level=logging.INFO)

def add(a, b):
    result = a + b
    logging.info(f"Dodaję liczby {a} i {b}. Wynik: {result}")
    print(result)
    
def minus(a, b):
    result = a - b
    logging.info(f"Odejmuję liczbę {b} od {a}. Wynik {result}")
    print(result)
    
def x_times(a, b):
    result = a * b
    logging.info(f"Mnożę liczby {a} i {b}. Wynik {result}")
    print(result)
    
def divide(a, b):
    logging.info(f"Dzielę liczby {a} przez {b}")
    if b == 0:
        logging.warning("Dzielenie przez 0 jest niedozwolone")
        return
    else:
        return a / b

def wrong_task():  # na spotkanie
    logging.warning("Wybierz poprawne działanie")
    sys.exit()

if __name__ == "__main__":
    task = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    
    if task == 1:
        result = add(a, b)
        print(result)
    elif task == 2:
        result = minus(a, b)
        print(result)
    elif task == 3:
        result = x_times(a, b)
        print(result)
    elif task == 4:
        result = divide(a, b)
        print(result)
    else:
        wrong_task()  # na spotkanie