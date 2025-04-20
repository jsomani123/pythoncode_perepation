import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s')

def seventable(number,i):
    if i>10:
        return
    logging.info(f"table of seven {number} * {i}={number*i}") 
    return seventable(number,i+1)


logging.info(f"table of seven{seventable(7,1)}")