import smtplib
import os.path, time
import re


def alert_message():

    s = smtplib.SMTP('smtp.gmail.com', 587)		
    s.starttls()
    s.login("aarthikaf@gmail.com", "aarthikafff")
    #f=open("/home/gokul/Documents/test/conpot.log","r")
    message="gokul"
    with open("/var/log/conpot/conpot.log") as file:
        for line in (file.readlines() [-1:]):
            print(line, end ='')
            if re.search("Modbus", line):
                message="\nTime-- "+str(line.split(',')[0])
                message+="\nservice --Modbus"
                p=re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\:\d{1,6})')                
                message+="\nIP address --"+str(p.search(line)[0])
                
                print(message)
            
    '''for x in f:
        x=json.loads(x);
    try:
    
    except:
        pass'''

        

    s.sendmail("aarthikaf@gmail.com", "gokulr7071@gmail.com", message)
    s.quit() 
    return

if __name__=="__main__":
    
    v=time.ctime(os.path.getmtime("/var/log/conpot/conpot.log"))
    print(v)
    while(1):
        if v!=time.ctime(os.path.getmtime("/var/log/conpot/conpot.log")):
            alert_message()
            v=time.ctime(os.path.getmtime("/var/log/conpot/conpot.log"))
            
        
        
        
    


