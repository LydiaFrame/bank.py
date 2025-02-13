#!/usr/bin/env python3

"""A program to compute the balance of a bank account."""

__author__ = "Lydia Frame"
__date__ = "02/13/2025"

import transaction

def main():
    while True:
        print("Balance: $", transaction.balance)
        type = input("Type? ").lower()
        print()
        
        if type == "x":
            break
        elif type == "d":
            value = float(input("Value? "))
            transaction.deposit(value)
            print()
        elif type == "w":
            value = float(input("Value? "))
            transaction.withdraw(value)
            print()
        elif type == "i":
            rate = float(input("Value? "))
            transaction.apply_interest(rate)
            print()
        else:
            print("Invalid option. Try again.")
            
if __name__ == "__main__":
    main()