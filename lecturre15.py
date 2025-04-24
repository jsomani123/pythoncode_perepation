#create a dictionary 
#into key and value
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s')
# labour_with_cost={"Mahesh":400,"Yogesh":500,"Akash":560,"Ramesh":900}
# labour_with_cost["Mahesh"]=1000
# # logging.info(f"{labour_with_cost.keys()}")
# # logging.info(f"{labour_with_cost.items()}")
# for name in labour_with_cost:
#     logging.info(f"{name,labour_with_cost[name]}")
# for key,value in labour_with_cost.items():
#     print(key,value)

    #total cost of employee who working days 5 days
    #out of which mahesh 3 days was abesent in class jaghmon for 7 days abesment 
    #total labour labour_with_cost
labour_with_cost = {"Mahesh":500,"Ramesh":400,"Mithilesh":400,"Sumesh":300,"Jagmohan":1000,"Rampyare":800}
#labour_with_cost=labour_with_cost.get("Mahesh1")

#logging.info(f"{labour_with_cost}")

#KEY AND VALUE METHOD
#logging.info(f"{labour_with_cost.key()}")

#logging.info(f"{labour_with_cost.values()}")
#item method
#logging.info(f"{labour_with_cost.items()}")
# labour_with_cost.update({"manish":700,"Ram":800})
# logging.info(f"{labour_with_cost}")
#new_dict={"manish":700,"Ram":800}
#final_dict={**labour_with_cost, **new_dict}
#ogging.info(f"{final_dict.items()}")

#pop
# logging.info(f"{labour_with_cost.pop("Mahesh")}")
# logging.info(f"{labour_with_cost.popitem()}")
# logging.info(f"{labour_with_cost.popitem()}")
# logging.info(f"{labour_with_cost.keys()}")


#copy 
# new_labour_cost=labour_with_cost.copy()
# logging.info(f"{id(labour_with_cost)}")
# logging.info(f"{id(new_labour_cost)}")

#clear 
#new_labour_cost=labour_with_cost.clear()
#logging.info(f"{id(labour_with_cost)}")
#logging.info(f"{id(new_labour_cost)}")

#dictionary comphresion

# labour_with_cost ={key:labour_with_cost[key]+100 for key in labour_with_cost }
# logging.info(f"{(labour_with_cost)}")
# labour_with_cost ={ key:labour_with_cost.get(key)+100 if key!='Jaghmohan' else labour_with_cost for key in labour_with_cost }
# logging.info(f"{(labour_with_cost)}")

name="manish kumar"
letter_count = {} # Initialize as a dictionary
text = "example text"

for char in name:
    if char in letter_count:
        letter_count[char] += 1
    else:
        letter_count[char] = 1
    print(letter_count)