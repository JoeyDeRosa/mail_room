import sys


def main():
    list_of_donors = {}
    user_prompt(list_of_donors)


def user_prompt(list_of_donors):
    """Returns user choice for actions to be taken within program."""
    while(True):
        response = input("Please enter 1 to Send a Thank You, 2 to Create a \
            report or q to Quit: ")
        if response == '1':
            donor_name = input("Enter the name of the donor or enter 'list' \
                to view donor list: ")
            if donor_name.lower() == 'q':
                sys.exit()
            elif donor_name == 'list':
                print_list(list_of_donors)
                continue
            else:
                list_of_donors = check_donor(list_of_donors, donor_name)
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
            list_of_donors = add_donation(list_of_donors, donation, donor_name)
            prepare_email(list_of_donors, donor_name)
        elif response == '2':
            create_report(list_of_donors)
        elif response.lower() == 'q':
            sys.exit()
        else:
            print('Please enter 1, 2 or q')


def print_list(list_of_donors):
    if len(list(list_of_donors.keys())) == 0:
        print('There are no names on the donor list')
    for name in list(list_of_donors.keys()):
        print(name)
    return sorted(list(list_of_donors.keys()))


def check_donor(list_of_donors, donor_name):
    if donor_name not in list_of_donors.keys():
        list_of_donors[donor_name] = []
        return list_of_donors
    else:
        return list_of_donors


def add_donation(list_of_donors, donation, donor_name):
    list_of_donors[donor_name].append(donation)
    return list_of_donors


def prepare_email(list_of_donors, donor_name):
    message = "Thank you for the donation of {} to {}".format(list_of_donors[donor_name][-1], donor_name)
    print(message)
    return message


def create_report(list_of_donors):
    new_dict = {}
    print('Donor -- Sum -- Num -- Average')
    for donor in list_of_donors:
        donor_sum = sum(list_of_donors[donor])
        num_donat = len(list_of_donors[donor])
        new_dict[donor] = [donor_sum, num_donat]
        print(donor, ' -- ', donor_sum, ' -- ', num_donat, ' -- ', \
        sum(list_of_donors[donor]) / len(list_of_donors[donor]))
    return new_dict


if __name__ == '__main__':
    main()
