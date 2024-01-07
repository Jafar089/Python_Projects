# THis is for checking correct email

from verify_email import verify_email

 email_id = input("Enter your email id ")
 if(verify_email(email_id)):
    print("This is a valid email address")
 else:
    print("This is an invalid email address")