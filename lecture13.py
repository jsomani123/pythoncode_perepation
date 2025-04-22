#List comphersion
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s')
list=[1,2,3,4,5,6,7,8,9,10]
sub_list=[2,4,6,8,10]
new_list=["Even" if number%2==0 else "Odd" for number in list]
logging.info(f"{new_list}")