from view.terminal.menu import Menu
from view.terminal.encode.encode_view import EncodeView
from view.terminal.decode.decode_view import DecodeView


class ViewMenu(EncodeView, DecodeView):
    def __init__(self):
        super(ViewMenu, self).__init__()
        self.menu = Menu()
        self.handler_options = {
            1: self.encode_handler,
            2: self.decode_handler
        }


    def handle_menu_option(self, option: int):
        self.handler_options[option]()

    def encode_handler(self):
        self.menu.encode.get_options()
        option = self.menu.get_option([1,2,3])
        super().get_encode_handler(option)

    def decode_handler(self):
        self.menu.decode.get_options()
        option = self.menu.get_option([1,2])
        super().get_decode_handler(option)

    def return_to_menu(self):
        self.menu.get_header()
        self.handle_menu_option(self.menu.get_option([1,2]))



class Decode:
    pass