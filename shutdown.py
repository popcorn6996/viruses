import os


def shut_down():
    try:
         if os.name == 'nt':
             os.system("shutdown /s /f /t 0") 
         elif os.name == "posfix":
             os.system("sudo shutdown now")    
         else:
             print('Unsupported Operating System')
    except Exception as e:
        print(f"Error as  {e}")       
        


if __name__ == "__main__":
    shut_down()          
                 
             
    
