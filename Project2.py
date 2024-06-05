contacts = {
    'hashslinging@slasher.com': {'Name': 'Spongebob Squarepants', 'Phone': '999 111 1111'},
    'wumbology@wumbo.com': {'Name': 'Patrick Star', 'Phone': '999 222 2222'},
    'martialarts@karate.com': {'Name': 'Sandy Cheeks', 'Phone': '999 333 3333'},
    'snailmail@gary.com': {'Name': 'Gary Snail', 'Phone': '999 444 4444'}
}


def add_contact():
    email = input('Email: ')
    name = input('Name: ')
    phone = input('Phone # ')
    contacts[email] = {'Name': name, 'Phone': phone}
    print(name, 'Added Successfully!')


def edit_contact():
    email = input("Enter Contact's Email to Edit: ")
    if email in contacts:
        field = input('Enter Edit (Name/Phone): ')
        new_value = input(f'Enter new {field}: ')
        contacts[email][field] = new_value
        print('Contact Updated. ')
    else:
        print('Contact Not Found, Please Try Again. ')


def delete_contact():
    email = input('Enter email of contact you wish to delete: ')
    if email in contacts:
        del contacts[email]
        print('Contact deleted successfully!')
    else:
        print('Contact not found.')


def search_contact():
    email = input('Enter Email to Search: ')
    if email in contacts:
        print('- - - - - - - - - -')
        print('Contact Details:')
        print('Name:', contacts[email]['Name'])
        print('Phone:', contacts[email]['Phone'])
    else:
        print('Contact Not Found, Please Try Again. ')


def display_contacts():
    print('Roladex Info:')
    for email, details in contacts.items():
        print('- - - - - - - - - -')
        print('Email:', email)
        print('Name:', details['Name'])
        print('Phone:', details['Phone'])


while True:
    print('''
    Welcome to the Contact Management System!
    --------------------
           Menu:
    --------------------
    1: Add New Contact
    2: Edit Existing Contact
    3: Delete a Contact
    4: Search Contacts
    5: Display all Contacts
    0: Quit
    -------------------- ''')
    choice = input("Enter Input: ")

    if choice == '1':
        add_contact()
        
    elif choice == '2':
        edit_contact()

    elif choice == '3':
        delete_contact()

    elif choice == '4':
        search_contact()

    elif choice == '5':
        display_contacts()

    elif choice == '0':
        print('Good Bye, Have a Good Day. ')
        break
    else:
        print('Invalid Input. Please Try Again. ')







#   6 - Export:
#   7 - Import: