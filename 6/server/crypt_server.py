import sys, getopt
from server_functions import _user_handler, generate_OTPs

def usage(error = None):
    if error != None:
        print(error)
    print('usage: crypt_server.py -u <username> -p <password>')
    print('usage: crypt_server.py --username=<username> --pwd=<password>')
    sys.exit(2)

def main(argv):
    username, pwd = '', None
    try:
        opts, args = getopt.getopt(argv, 'u:p:', ['username=', 'pwd='])

    except getopt.GetoptError as error:
        usage(error)
        
    
    for opt, arg in opts:
        if opt in ('-u', '--username'):
            username = arg
        elif opt in ('-p', '--pwd'):
            pwd = arg
    
    print(_user_handler(username, pwd))
    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv[1:])