import os
import sys


def error_function():
    try:
        return 10 / 0
    except ZeroDivisionError as e:  # You need to specify the exception to catch
        print("Error: Division by zero occurred.")
        print(f"Error message: {e}")


if __name__ == "__main__":  # Double underscores should surround "main"
    error_function()
