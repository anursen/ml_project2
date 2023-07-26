import sys
from logger import logging


def error_message_detail(error_message):
    exc_type, exc_value, exc_traceback = sys.exc_info()
    file_name = exc_traceback.tb_frame.f_code.co_filename
    code_line = exc_traceback.tb_lineno
    error_message = f"Error occurred at python file {file_name} on line {code_line} and the error message is {error_message}"
    return error_message


class CustomException(Exception):
    def __init__(self, error_message) -> None:
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message)

    def __str__(self) -> str:
        return self.error_message


def main():
    try:
        10 / 0
    except ZeroDivisionError as e:
        logging.info("Divide by zero message")
        raise CustomException("Zero Division Error")


if __name__ == "__main__":
    main()
