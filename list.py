length_of_land = 100
bricks_cost_per_price = 10.5
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s')
labour_names = ['Mahesh','Ramesh','Mahesh','Milthesh']
new_labour=["ram","mohan"]
labour_names.extend(new_labour)
labour_names.insert(0,"Sachin")

empty_list=[]
is_home = True
logging.info(f"list {labour_names[0]}")
# print(length_of_land,bricks_cost_per_price,labour_mistri,is_home)
# print(type(length_of_land),type(bricks_cost_per_price),type(labour_mistri),type(is_home))