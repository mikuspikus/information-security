import sys, getopt
import os
from subprocess import Popen, PIPE
from client_functions import generate_OTPs

def usage(error = None):
    if error != None:
        print(error)

    print('usage:\n\tcrypt_client.py -u <username> -i <initial_number> -t <try_number> -h <help>')
    print('\tcrypt_client.py --username=<username> --init=<password> --try=<try_number> --help<help>')
    print('\nuse -t 0 or --try=0 to register in the club with your initial number')
    sys.exit(2)

def main(argv):
    username, initial_number, try_number= '', None, None
    try:
        opts, args = getopt.getopt(argv, 'u:i:t:h', ['username=', 'init=', 'try=', 'help'])
    except getopt.GetoptError as error:
        usage(error=error)

    for opt, arg in opts:
        if opt in('-h', '--help'):
            usage()
        elif opt in ('-u', '--username'):
            username = arg
        elif opt in ('-i', '--init'):
            initial_number = int(arg)
        elif opt in ('-t', '--try'):
            try_number = int(arg)
    
    pwd = generate_OTPs(initial_number)[try_number] if try_number != 0 else initial_number

    dirname = os.path.dirname
    script_path = os.path.join(os.path.join(dirname(__file__), os.pardir), os.path.join('server', 'crypt_server.py'))
    
    proc = Popen(
        'python ' + script_path + ' --username=' + str(username) + ' --pwd=' + str(pwd),
        shell=True,
        stdout=PIPE,
        stderr=PIPE
    )
    proc.wait()
    output, errors = proc.communicate()
    if proc.returncode:
        print(errors)
    
    print(output.decode(sys.stdout.encoding))

    sys.exit(0)

if __name__ == '__main__':
    main(sys.argv[1:])