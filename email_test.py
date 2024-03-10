#Jackie Massaya 11 feb 2024

### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email():
    # Declare the class variable, with default value, for emails. 
 has_been_read = False
    # Initialise the instance variables for emails.
 def __init__(self, email_address, subject_line, email_content):
    self.email_address= email_address
    self.subject_line = subject_line
    self.email_content = email_content

    # Create the method to change 'has_been_read' emails from False to True.
 def mark_as_read(email):
    email.has_been_read==True

 def __str__(self):
    return self.subject_line
# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox =[]
# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
    
    # Create 3 sample emails and add it to the Inbox list. 
 email_1 = Email('fun@fun.com', 'hey', 'hey there')
 email_2 = Email('me@me.com', 'hello', 'hello stranger, how goes it??')
 email_3 = Email('you@you.com', 'hihihi', 'hi, how have you been?')
 emails= (email_1, email_2, email_3)
 inbox.extend(emails)

 
def list_emails(inbox):
    
    # Create a function which prints the email’s subject_line, along with a corresponding number.

 for email_number, email in enumerate(inbox):
   print(email_number, email.subject_line)
   

def read_email(index):
 email = inbox[index]  
    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.

 print("Email address: " + email.email_address + 
       '\n' + "Subject: " + email.subject_line  +
        '\n' + "Message: " + email.email_content)

 email.has_been_read = True
 print(f"\nEmail from {email.email_address} marked as read.\n")
# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.
populate_inbox()
# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # add logic here to read an email
     list_emails(inbox)

     #defensive check
     while True:
       try:
           index = int(input("Select the index of the email you would like to read"))
           break
       except (ValueError, IndexError):
           print("Oops - incorrect input.")

         
     read_email(index)

    elif user_choice == 2:
        # add logic here to view unread emails
     unread = []
     for email in inbox: 
       if email.has_been_read==False:
         unread.append(email.subject_line)
     print("The following emails are unread:" + '\n' + "\n".join(unread))
       
    
    elif user_choice == 3:
        # add logic here to quit appplication
      break
    else:
        print("Oops - incorrect input.")

