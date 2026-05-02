from decimal import Decimal, getcontext
import time
import sys

def chudnovsky(digits):
    getcontext().prec = digits + 10

    C = 426880 * Decimal(10005).sqrt()

    M = 1
    L = 13591409
    X = 1
    K = 6
    S = L

    steps = digits // 14 + 1

    for i in range(1, steps + 1):
        M = (M * (K**3 - 16*K)) // (i**3)
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12

        percent = int((i / steps) * 100)
        print(f"Calculating... {percent}%", end="\r")
        time.sleep(0)  # usuwa jitter, możesz usunąć

    print("Calculating... 100%")

    return str(C / S)

while True:
    n = input("Digits of pi (or 'exit'): ")

    if n.lower() == "exit":
        break

    if n.isdigit():
        print("Starting calculation...")
        print(chudnovsky(int(n)))