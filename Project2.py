#   contacts needs name, phone mumber, and email address. contact deatils in the INNER disctionary, phone/email as OUTTER dictionary


contact ={
    'hashslinging@slasher.com': {'Name': 'Spongebob Squarepants', 'Phone': '999 111 1111'},
    'wumbology@wumbo.com': {'Name': 'Patrick Star', 'Phone': '999 222 2222'},
    'martialarts@karate.com': {'Name': 'Sandy Cheeks', 'Phone': '999 333 3333'},
    'snailmail@gary.com': {'Name': 'Gary Snail', 'Phone': '999 444 4444'}
}


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
6: Export Contacts to .txt file
7: Import Contacts from .txt file
0: Quit
-------------------- ''')
menu = (input("Enter Input: "))




# Menu Actions:
# Implement the following actions in response to menu selections:
#  1 Adding a new contact with all relevant details.
#  2 Editing an existing contact's information (name, phone number, email, etc.).
#  3 Deleting a contact by searching for their email.
#  4 Searching for a contact by their unique email and displaying their details.
#  5 Displaying a list of all contacts.
#  6 Exporting contacts to a text file in a structured format.
#  7 Importing contacts from a text file and adding them to the system.




#   1 - Adding Contacts:
while menu != 'stop adding':
    if menu == '1':
        email1 = input('Email: ')
        name1 = input('Name: ')
        phone1 = input('Phone: ')
        print('----------')
        print(name1,': Has Been Added!')
        print('----------')
        again = input('"yes" to add another, "stop adding" to end: ')
        if again == 'stop adding':
            print("Have a Nice Day!")
            break




#   2 - Editing Contact:
    while menu != 'end edit':
        if menu == '2':
            edit = input("Enter Contact Email You Would Like to Edit: ")
            if edit == 'Spongebob Squarepants':
                sponge_edit = input('What Would You Like to Change? ')
                if sponge_edit == ['Name']:
                    print()
                    break
#   dictionary[existing_key] = new_value




#   3 - Delete Contact:
        while menu != 'stop delete':
            if menu == '3':
                contact_delete = input("Enter email of contact you wish to delete: ")
                del contact[contact_delete]
                print(contact_delete,': Has Been Deleted')
                print("----------")
                print("Would You Like to Delete Another? ")
                print("----------")
                more_del = input('"yes" to proceed, "stop delete" to end: ')
                if more_del == 'stop delete':
                    print("Have a Nice Day!")
                    break
                    # doesnt break for some reason :/




#   4 - Search:
            if menu == '4':
                search = input("Enter Email to Search: ")
                if search == 'hashslinging@slasher.com':
                    print()
                elif search == 'wumbology@wumbo.com':
                    print()
                elif search == 'martialarts@karate.com':
                    print()
                elif search == 'snailmail@gary.com':
                    print()
                else:
                    print('Invald Email, Try Again')
                    break



#   5 - Display List:
            else:
                menu == '5'
                contact_list = input('Press Enter to Display All Contacts: ')
                print(contact)
                break



#   6 - Export:
#   7 - Import: