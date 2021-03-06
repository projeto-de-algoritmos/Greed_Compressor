from view.terminal.menu import Menu
from view.terminal.view_menu import ViewMenu
import signal

menu = Menu()
view_menu = ViewMenu()


def main():
    menu.get_header()
    view_menu.handle_menu_option(menu.get_option([1,2]))

if __name__ == "__main__":
    signal.signal(signal.SIGINT, menu.exit_terminal)
    main()