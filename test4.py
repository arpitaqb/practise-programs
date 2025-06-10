#extract valid email using regx
import re

pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

def extractemail(emails):
    matches = re.search(pattern, emails)
    if matches:
        print(f"Your email is valid : {emails}")
    else:
        print("no match")


emails = [ "john.doe@example.com",
    "user123@sub.domain.org",
    "name+alias@gmail.com",
    "first.last@company.co.uk",
    "user_name@domain.io",
    "user-name@domain.travel",
    "email@123.123.123.123",
    "email@[123.123.123.123]",
       "plainaddress",
    "@missingusername.com",
    "username@.com",
    "username@com",
    "username@domain.c",
    "user name@domain.com",
    "user@domain..com",
    "user@.domain.com",
]
for i in emails:
    extractemail(i)
