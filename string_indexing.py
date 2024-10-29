# enter your email id
email=input("please enter your email address: ")
# email = email.index("@")
# print(email)
username= email[:email.index('@')]
domain=email[email.index('@') + 1:]
print(username)
print(domain)
