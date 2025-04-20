import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s')

def factorical(number):
    if number==0:
        return 1
    else :
       return number*factorical(number-1)
logging.info(f"factroical of {factorical(5)}")