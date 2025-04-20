
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s')
# labour_names = ['Mahah','Rameh','Maheh','Miltheh',500,400,300,400]
# logging.info(f"cotsly labour chagre {(labour_names)}") 
# labour_names[0:4]=['Mahesh']
# # wage=labour_names.pop(2)
# # del labour_names
# logging.info(f"cotsly labour chagre {(labour_names)}") 
# # logging.info(f"cotsly labour chagre {(labour_names.remove(1000))}") 
# # new_labour=["ram","mohan"]
# # labour_names=labour_names + (new_labour)
# #revers a list90
# # if wage >500 :
# #    logging.info(f"cotsly labour chagre {(labour_names)}") 

# logging.info(f"lenght of list {(labour_names)}")
# #logging.info(f"first element {labour_names[::-1]}")
# #get list of columns 

api_endpoint='https://portal.azure.com/#home'
new_api_list=api_endpoint.split("/")
logging.info(f"first element {new_api_list[-2]}")