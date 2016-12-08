'''Test file for mail_room.py.'''


def test_print_list():
    '''Test that print_list returns the donors names.'''
    donor_list = {'Bob': [1, 2], 'Ted': [3, 4], 'Jim': [5, 6]}
    from mail_room import print_list
    assert print_list(donor_list) == ['Bob', 'Jim', 'Ted']


def test_check_donor():
    '''Test that check_donor returns if the donor is already in list or not'''
    donor_list = {}
    from mail_room import check_donor
    assert check_donor(donor_list, donar_name) == []

