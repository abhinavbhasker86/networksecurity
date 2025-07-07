import sys
from networksecurity.logging import logger
#from networksecurity.logging.logger import logging

class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()
        
        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename 
    
    def __str__(self):
        print('------AB--EXCEPTION RAISING EXCEPTION------')
        return "ERRORRRRRRRR occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        self.file_name, self.lineno, str(self.error_message))
'''      
if __name__=='__main__':
    try:
        logger.logging.info("This is a test log message.")
        a=1/0  # This will raise a ZeroDivisionError
        logger.logging.info("This line will not be executed due to the error above.")
    except Exception as e:
        logger.logging.info('------AB--EXCEPTION RAISING EXCEPTION------')
        raise NetworkSecurityException(e, sys)  # This will raise the custom exception with the error details
'''       