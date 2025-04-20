length_of_land = 100
bricks_cost_per_price = 10.5
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s')

labour_names = ['Mahesh','Ramesh','Mahesh','Milthesh',200]
#method1
# for i in labour_names:
#   logging.info(f"labour 1  name is {i}")  
#method 2
for i in range(len(labour_names)):
    logging.info(f"labour {i+1}  name is {labour_names[i]}")


empty_list=[]
is_home = True
# logging.info(f"list {labour_names}")
# print(length_of_land,bricks_cost_per_price,labour_mistri,is_home)
# print(type(length_of_land),type(bricks_cost_per_price),type(labour_mistri),type(is_home))