###
# Kim Kaufman
# This program checks a password from user input to see if it meets the password requirements


def check_password(password):
    """Takes a password to check it against each password requirement to determine if it meets the requirements

    Param:
        password (string): takes a password to check against password requirements in for loop

    Returns:
        password_check (string): only returns if every password requirement is met
        incorrect_password (list): returns with a list that contains the appropriate password problem messages 
    """
    
    check_upper = False
    check_lower = False
    check_digit = False
    for char in password: 
        if char.isupper():
            check_upper = True
        elif char.islower():
            check_lower = True
        elif char.isdigit():
            check_digit = True
            
    if len(password) >= 8 and check_upper and check_lower and check_digit:
        password_check = "correct"
        return password_check
    
    else:
        incorrect_password = []
        if len(password) < 8:
            incorrect_password.append("incorrect length") 
        if not check_upper:
            incorrect_password.append("missing uppercase letter")
        if not check_lower:
            incorrect_password.append("missing lowercase letter")
        if not check_digit:
            incorrect_password.append("missing digit")
        return incorrect_password
        
                  
    
def main():
    
    
    done = False
    while not done: 
    
        print("\nYour password must be a least 8 characters long,\n have at least one uppercase & one lowercase letter,\n and must have at least one digit.\n")
   
        password = input("Please enter a password:\t\t")
        
        password2 = input("Please enter your password again:\t")
        # password and password2 must match
        
        if password == password2 :
            print("The password entries match \n")
            
        else:
            print("\nThe password entries do not match. Please try again")
            continue
        
        password_status = check_password(password2)
        #calls check_password and sets password_status to the value returned from check_password
        
        if password_status == "correct":
            print("The password meets all requirements")
            done = True
            
        else:
            password_message = " "
            password_message = ", ".join(password_status)
            print("Password problem(s): ", password_message)
            #converts password_status from a list to a string to format for printing
            continue    
                
    
    
    
    
       
main()    
    
