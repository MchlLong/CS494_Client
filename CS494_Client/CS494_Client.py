# Michael Long, Gennadii Sytov -- CS494 -- Client Main -- May 2019

import client

def main():

    print("Booting Application. . .")
    user = client.client_handler(host = '71.193.235.33', port = 1080)
    user.main_loop()

if __name__ == '__main__':
    main()
