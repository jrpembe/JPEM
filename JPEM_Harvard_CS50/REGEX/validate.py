email = input('What is your email address? ').strip()

# Basic

# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")

# Intermediate

# username, domain = email.split("@")

# if (username) and ("." in domain) and domain.endswith(".com"):
#     print("Valid")
# else:
#     print("Invalid")
    
    
# Advanced   
# re 
# re.search(pattern, string, flags=0)

"""
. any character except a newline
* 0 or more repetitions
+ 1 or more repetitions
? 0 or 1 repetition
{m} m repetitions
{m, n} m-n repetitions
^ matches the start of a string
$ matches the end of a string (just before the newline)
"""


import re

# if re.search(".+@.+", email):
#     print("Valid")
# else:
#     print("Invalid")
    
# or
if re.search(r"^.+@.+\.com$", email):
    print("Valid")
else:
    print("Invalid")
