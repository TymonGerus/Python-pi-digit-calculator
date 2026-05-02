from decimal import Decimal, getcontext
import threading
import time

def chudnovsky(digits):
    getcontext().prec = digits + 10

    C = 426880 * Decimal(10005).sqrt()
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = L

    for i in range(1, digits):
        M = (M * (K**3 - 16*K)) // (i**3)
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12

    return str(+ (C / S))

def loading(stop_event):
    while not stop_event.is_set():
        print("Calculating ...", end="\r")
        time.sleep(0.4)

while True:
    user_input = input("Enter number of digits of pi (or 'exit'): ")

    if user_input.lower() == "exit":
        break

    if user_input.isdigit():
        stop_event = threading.Event()
        t = threading.Thread(target=loading, args=(stop_event,))
        t.start()

        result = chudnovsky(int(user_input))

        stop_event.set()
        t.join()

        print(" " * 50, end="\r")
        print(result)