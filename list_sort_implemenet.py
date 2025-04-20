import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s')
list=[5,18,77,108,930]
index=0
no_to_intersted=100
for num in list:
    if num > no_to_intersted:
        index=index
        break
    else:
        index=index+1
list.append(None)
for i in (range(len(list)-1,index,-1)):
    list[i]=list[i-1]
list[index]=no_to_intersted
logging.info(f"soreted and added the element{list}")
    

