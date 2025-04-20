import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s')
count=0
paragraph = """ Ralph Kimball founded the Kimball Group. Since the mid-1980s, he has been the 
data warehouse and business intelligence industry’s thought leader on the dimen
sional approach. He has educated tens of thousands of IT professionals. The Toolkit 
books written by Ralph and his colleagues have been the industry’s best sellers 
since 1996. Prior to working at Metaphor and founding Red Brick Systems, Ralph 
coinvented the Star workstation, the fi rst commercial product with windows, icons, 
and a mouse, at Xerox’s Palo Alto Research Center (PARC). Ralph has a PhD in 
electrical engineering from Stanford University """
paragraph=paragraph.split(" ")
for letter in paragraph:
    if letter =='the':
        count=count+1
    else:
        continue
logging.info(f"the word count of the is {count}")
    