import re


name = input("What is your name? ").strip()

# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"
# print(f"Hello, {name}")

matches = re.search(r"^(.+), (.+)$", name)
if matches:
    # last = matches.groups(1)
    # first = matches.groups(2)
    name = matches.group(2) + " " + matches.group(1)
    # name = f"{first} {last}"
print(f"Hello, {name}")


