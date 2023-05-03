import sys
import logging
logging.basicConfig(level=logging.INFO)

task = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

if task == 1:
    result = a + b
    logging.info(f"Dodaję liczby {a} i {b}. Wynik: {result}")
    print(result)
elif task == 2:
    result = a - b
    logging.info(f"Odejmuję liczbę {b} od {a}. Wynik {result}")
    print(result)
elif task == 3:
    result = a * b
    logging.info(f"Mnożę liczby {a} i {b}. Wynik {result}")
    print(result)
elif task == 4:
    logging.info(f"Dzielę liczby {a} przez {b}")
    if b == 0:
        logging.warning("Dzielenie przez 0 jest niedozwolone")
    else:
        print(a / b)