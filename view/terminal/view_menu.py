from view.terminal.menu import Menu
from view.terminal.encode.encode_view import EncodeView
from view.terminal.decode.decode_view import DecodeView


class ViewMenu(EncodeView, DecodeView):
    def __init__(self, *args, **kwargs):
        self.menu = Menu()
        self.handler_options = {
            1: self.encode_handler,
            2: self.decode_handler
        }
        super().__init__(*args, **kwargs)


    def handle_menu_option(self, option: int):
        self.handler_options[option]()

    def encode_handler(self):
        self.menu.encode.get_encode_options()
        option = self.menu.get_option([1,2,3])
        super().get_encode_handler(option)

    def decode_handler(self):
        print("Deu ruim")

    def return_to_menu(self):
        self.menu.get_header()
        self.handle_menu_option(self.menu.get_option([1,2]))



class Decode:
    pass