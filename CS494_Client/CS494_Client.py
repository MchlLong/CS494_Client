# Michael Long, Gennadii Sytov -- CS494 -- Client Main -- May 2019

import client_gui as gui
import client

def main():
    #screen = gui.gui_controller()
    a = client.client_handler(host = '71.193.235.33', port = 1080)
    a.main_loop()

if __name__ == '__main__':
    main()
