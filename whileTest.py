import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s')
import time 
labour_names = ['Mahah','Rameh','Maheh','Miltheh']
iterataorable_value=3
while(iterataorable_value>0 ):
    print(labour_names[iterataorable_value])
    time.sleep(5)
    iterataorable_value-=1
