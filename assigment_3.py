#method 1 to resolve it 
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s')
list=[202,165,89,65,12]
index=0
no_to_instered=15
for num in list:
    if num<no_to_instered:
        index=index
        break
    else:
        index=index+1
list.append(None)
for i in range(len(list)-1,index,-1):
    list[i]=list[i-1]
list[index]=no_to_instered
logging.info(f"soreted and added the element{list}")


