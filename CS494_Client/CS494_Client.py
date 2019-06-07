# Michael Long, Gennadii Sytov -- CS494 -- Client Main -- May 2019

import client

def main():

    user = client.client_handler(host = '127.0.0.1', port = 1234)
    user.main_loop()

if __name__ == '__main__':
    main()
