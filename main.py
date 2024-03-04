import ui.menu as m

def main():
    m.menuMain()

if __name__ == '__main__':
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print('No rompa el codigo')
            m.sc.pause_screen()
        else:
            main()
            break