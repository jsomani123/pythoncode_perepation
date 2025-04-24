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
total_cost=0
susbract_cost=0
for key,value in labour_with_cost.items():
    total_cost+=value*50
    if key=='Mahesh':
        susbract_cost+=labour_with_cost[key]*3
    if key=='Jagmohan':
         susbract_cost+=labour_with_cost[key]*7
logging.info({total_cost-susbract_cost})
