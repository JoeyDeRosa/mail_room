import sys

LIST_OF_DONORS = {}


def main():
    user_prompt()


def user_prompt():
    """Returns user choice for actions to be taken within program"""
    while(True):
        response = input("Please enter 1 to Send a Thank You, 2 to Create a report or q to Quit: ")
        if response == '1':
            send_thank_you_prompt()
        elif response == '2':
            create_report()
        if response.lower() == 'q':
            sys.exit()
        else:
            print('Please enter 1, 2 or q')


def send_thank_you_prompt():
    send_thank_you(input("Enter the name of the donor or enter 'list' to view donor list: "))


def send_thank_you(donor_name):
    if donor_name.lower == 'q':
        sys.exit()
    elif donor_name.lower == 'list':
        for name in list(LIST_OF_DONORS.keys()):
            print(name)
        send_thank_you_prompt()
    elif donor_name not in LIST_OF_DONORS.keys():
        LIST_OF_DONORS[donor_name] = []
    add_donation(donor_name)


def create_report():
    print(LIST_OF_DONORS)


def add_donation(donor_name):
    while(True):
        donation = input("What is the amount of the donation?: ")
        if donation.lower == 'q':
            sys.exit()
        elif type(donation) == 'int' or 'float':
            LIST_OF_DONORS[donor_name].append(donation)
            prepare_email(donor_name)
        else:
            print('Please enter a dollar amount')


def prepare_email(donor_name):
    message = "Thank you for the donation of {} to {}".format(LIST_OF_DONORS[donor_name][-1], donor_name)
    print(message)
    user_prompt()


if __name__ == '__main__':
    main()
