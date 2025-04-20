
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s')
for i in range(5):
    logging.info(f"{(i+1)*'*'}")

