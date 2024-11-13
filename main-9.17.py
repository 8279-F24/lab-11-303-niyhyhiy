contact_list = input().split()

name = input()

for contact in contact_list:
    if name in contact:
        Frank_number = contact.split(',')[1]
    
print(Frank_number)