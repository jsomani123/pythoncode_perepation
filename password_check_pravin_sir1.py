import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(message)s')
def passwordCheck(password):

    if(len(password)<8):
        return False
    char=list(password)
    if  not any (i1[0].isupper() or i1[0].isdigit() for i1 in char):
           print("1")
           return False
    elif not any(i.isupper() for i in char):
            print("2")
            return False
    elif not any(i.islower() for i in char):
            print("3")
            return False
    elif not any(i1 in('!@#$%^&*')for i1 in char):
           print("4")
           return False
    else:
            print("5")
            return True
string='Password@123'
check=passwordCheck(string)
logging.info(f"password check is correct or not{check}")
    



    
    