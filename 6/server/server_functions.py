import os
import sys
from random import randint

def _make_joke_list(jokes_text):
    joke_list = []

    while jokes_text != '':
        joke_list.append(jokes_text[jokes_text.index('<') + 1:jokes_text.index('>')])
        jokes_text = jokes_text[jokes_text.index('>') + 1:]

    return joke_list

def generate_OTPs(initial_number, period = 100, p = 5923, m = 12619):
    def _make_pwd(old_pwd, p, m):
        return ((old_pwd % m) ** p) % m

    pwds = [initial_number]
    for i in range(0, period + 1):
        pwds.append(_make_pwd(pwds[-1], p, m)) # <- appendr

    return pwds[::-1] #<- reverse list with slice

def _get_users(file_name):
    script_dir = os.path.dirname(__file__)
    path = os.path.join(script_dir, file_name)
    users_dict = {}

    with open(path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        words = line.split()
        users_dict[words[0]] = words[1:]

    return users_dict

def _update_users(users_dict, file_name):
    script_dir = os.path.dirname(__file__)
    path = os.path.join(script_dir, file_name)
    try:
        with open(path, 'w') as f:
            for username in users_dict.keys():
                f.write(str(username) + ' ' + str(users_dict[username][0]) + ' ' + str(users_dict[username][1]) + '\n')

        return True
    except OSError:
        return False

def _get_joke(file_name):
    script_dir = os.path.dirname(__file__)
    path = os.path.join(script_dir, file_name)

    with open(path, 'r') as f:
        buffer = f.read()

    jokes = _make_joke_list(buffer)
    return jokes[randint(0, len(jokes) - 1)]



def _user_handler(username, pwd):
    users = _get_users('users.txt')
    message = ''

    try:
        pwd = int(pwd)
    except (ValueError, TypeError):
        message = 'Your password should be a number!'
        return message

    if username in users:
        # user is registered
        message = '\n\tHello, {}!\n\tGlad to meet you again.\n\tHere is you joke:'.format(username)
        # check his password
        if pwd == generate_OTPs(int(users[username][0]))[int(users[username][1])]:
            # joke
            message += _get_joke('jokes.txt')
            # next try number
            users[username][1] = str(1 + int(users[username][1]))
            message += '\tYour next password index would be {}.'.format(users[username][1])
        else:
            # access denied
            return '\n\tAccess denied!'
    else:
        message = '\n\tHello, {}!\n\tWellcome to the club!\n\tHere is your joke:'.format(username)
        # joke
        message += _get_joke('jokes.txt')
        # next try number
        message += '\tYour next password index would be {}.'.format(1)
        # register user
        users[username] = [pwd, 1]

    # update users.txt
    _update_users(users, 'users.txt')

    return message
