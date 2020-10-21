class Decode:

    def decode_text(self, encoded_text: str, hash_table: dict) -> str:
        decoded_text = ""
        temp_char = ""
        for char in encoded_text:
            temp_char += char

            if decoded_char := hash_table.get(temp_char):
                decoded_text += decoded_char
                temp_char = ""
        
        return decoded_text