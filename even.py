import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s')
for i in range(101):
    if(i%2==0):
            logging.info(f"all even no {i}")

