import sys
import logging
from src.logger import logging
 
def get_message_detail(error,error_detail = sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "An error occured in the python script [{0}] at line no. [{1}] and the error is [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail=sys) -> None:
        super().__init__(error_message)
        self.error_message_detail = get_message_detail(error_message,error_detail)
    def __str__(self) -> str:
        return self.error_message_detail