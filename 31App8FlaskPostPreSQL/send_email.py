import smtplib
import ssl

def send_email(to_email, height, average_height, heights_count):
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    response =smtp_obj.ehlo()
    print(response)
    print(smtp_obj.starttls())

    # can be app password
    # password = "z1kOut4r1"
    password = "jmbpezjnxckwajpq"

    from_address = "sekator6666@gmail.com"
    smtp_obj.login(from_address, password)

    # from_address = "unknowntest@gmail.com"
    # to_address ="tritseratops@gmail.com"
    from_address = "sekator6666@gmail.com"
    to_address =to_email

    subject = "Your height statistics"
    message = "Your height "+height+"written to statistics \n Average height is:"+str(average_height) + "\n Calaulated out of people: "+str(heights_count)
    msg = 'Subject: ' + subject +'\n'+message
    smtp_obj.sendmail(from_address, to_address, msg)
    smtp_obj.close()