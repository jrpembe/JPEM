# Calling Methods on Strings

string = "Hello, HOW are you TODAY?"
print(string)

string.upper()
string.lower()
string.title()
string.capitalize()

string.find("you")

string.replace("you", "ya")

string2 = "    How's it going?  "
string2.strip()
# lstrip and rstrip are options as well to remove left or right white spaces

# parsing and extrracting text

email = "jason.pemberton@gmail.com   "
atpos = email.find("@")
print(atpos)

host = email[atpos+1:]
print(len(host))
print(host.strip())