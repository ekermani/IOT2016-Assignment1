a = sunSign, risingSign, moonSign

    def yourChart(sunSign, risingSign, moonSign): 
    
        print ("Your Horoscope for " + sunSign + "/" +  risingSign + "/" + moonSign + " is: You are screwed. Mercury is in Retrograde")

    def horoscope():
    sign1 = raw_input("Enter your sun sign ")
    sign2 = raw_input("Enter your rising sign ")
    sign3 = raw_input("Enter your moon sign ")
    yourChart(sign1, sign2, sign3)

    horoscope()

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
# b = email.message_from_string(a)


fromaddr = "tests4iot@gmail.com"
toaddr = "tests4iot@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg ['Subject'] = "Your Horoscope for This Week"

body = "horoscope"  
msg.attach(MIMEText(body,'plain'))

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(fromaddr,'LVva@0#b1x5g')
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

# if b.is_multipart():
#     for payload in b.get_payload():
#         # if payload.is_multipart(): ...
#         print payload.get_payload()
# else:
#     print b.get_payload()