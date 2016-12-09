'''Test file for mail_room.py.'''


def test_print_list():
    '''Test that print_list returns the donors names.'''
    donor_list = {'Bob': [1, 2], 'Ted': [3, 4], 'Jim': [5, 6]}
    from mail_room import print_list
    assert print_list(donor_list) == ['Bob', 'Jim', 'Ted']


def test_check_donor_present():
    '''Test that check_donor returns if the donor is already in the list.'''
    donor_list = {'Bob': [1, 2], 'Ted': [3, 4], 'Jim': [5, 6]}
    donar_name = 'Jim'
    from mail_room import check_donor
    assert check_donor(donor_list, donar_name) == donor_list


def test_check_donor_not_present():
    '''Test that check_donor returns if the donor is not already in the list.'''
    donor_list = {'Bob': [1, 2], 'Ted': [3, 4]}
    donar_name = 'Jim'
    from mail_room import check_donor
    assert 'Jim' in check_donor(donor_list, donar_name)


def test_add_donation():
    '''Test that add_donation updates to donors donation array.'''
    donor_list = {'Jim': [5, 6]}
    donation = 20
    donor_name = 'Jim'
    from mail_room import add_donation
    assert add_donation(donor_list, donation, donor_name) == {'Jim': [5, 6, 20]}


def test_prepare_email():
    '''Test that prepare_email creates a message.'''
    donor_list = {'Bob': [1, 2], 'Ted': [3, 4]}
    donor_name = 'Bob'
    from mail_room import prepare_email
    assert prepare_email(donor_list, donor_name) == "Thank you for the donation of 2 to Bob"


def test_create_report():
    '''Tests that create report calcualates the proper figures'''
    donor_list = {'Bob': [10, 5]}
    from mail_room import create_report
    assert create_report(donor_list) == {'Bob': [15, 2]}
