import smtplib as s

ob =s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()
ob.login("sazidulislam223@gmail.com","app password") # Use your email and app password here
subject="test python"
body ="I love python"
massage="subject:{subject}\n\n{}".format(subject.body)
listadd=['sazidulislamrabbi@gmail.com','rabbihasan@gmail.com','king@gmail.com']
ob.sendmail("rabbiking00@gmail.com",listadd,massage)
print("Send maill")
ob.quit()