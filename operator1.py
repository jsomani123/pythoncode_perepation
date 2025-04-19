length_of_land = 100
bricks_cost_per_price = 10.5
breath_of_land=2044
labour_mistri = 'Jagmohan'
is_home = True

import math
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s')

                    

#calculate the area of land 

#total_area_of_land=length_of_land*breath_of_land


# 3logging.info(f"total area of my land is {total_area_of_land} sq ft")

#PERMETER OF LAND  2*(length_of_land+breath_of_land)
#bomas

#Module operator 
#print(15%6) #amstrong number need to use module 
#floor division
#print(math.floor(15//6))
#print(math.ceil(15//7))

permeter_of_land= 2* (length_of_land+breath_of_land)

#logging.info(f"permeter of my land is {permeter_of_land} sq ft")
# a="25"
# b=56
#print(a+str(b))

# a=1.5
# b=7
#print(int(a)+b)

length_of_land = float(input("please enter the lenght of your land"))
breath_of_land = (input("please enter the breath of land "))
#logging.INFO(f"{type(length_of_land)}")
total_area_of_your_land = abs(length_of_land * float(breath_of_land))
logging.info(f"total area of your land is {(total_area_of_your_land)}")