import sys

LIST_OF_DONORS = {}


def main():
    user_prompt()


def user_prompt():
    """Returns user choice for actions to be taken within program"""
    while(True):
        response = input("Please enter 1 to Send a Thank You, 2 to Create a \
            report or q to Quit: ")
        if response == '1':
            donor_name = input("Enter the name of the donor or enter 'list' \
                to view donor list: ")
            if donor_name.lower() == 'q':
                sys.exit()
            elif donor_name == 'list':
                print_list()
                continue
            else:
                check_donor(donor_name)
            valid_value = False
            while valid_value is not True:
                donation = input("What is the amount of the donation?: ")
                if donation.lower() == 'q':
                    sys.exit()
                try:
                    donation = int(donation)
                except ValueError:
                    print("That's not a valid dollar value")
                else:
                    valid_value = True
            add_donation(donation, donor_name)
            prepare_email(donor_name)
        elif response == '2':
            create_report()
        if response.lower() == 'q':
            sys.exit()
        else:
            print('Please enter 1, 2 or q')


def print_list():
    if len(list(LIST_OF_DONORS.keys())) == 0:
        print('There are no names on the donor list')
    for name in list(LIST_OF_DONORS.keys()):
        print(name)
    return list(LIST_OF_DONORS.keys())


def check_donor(donor_name):
    if donor_name not in LIST_OF_DONORS.keys():
        LIST_OF_DONORS[donor_name] = []
        return 1
    else:
        return 2


def add_donation(donation, donor_name):
    LIST_OF_DONORS[donor_name].append(donation)
    return LIST_OF_DONORS


def prepare_email(donor_name):
    message = "Thank you for the donation of {} to {}".format(LIST_OF_DONORS[donor_name][-1], donor_name)
    print(message)
    return message


def create_report():
    print(LIST_OF_DONORS)


if __name__ == '__main__':
    main()
