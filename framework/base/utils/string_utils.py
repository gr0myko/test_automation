import string
import random
import re


class RandomString:
    UPPERCASE = string.ascii_uppercase
    LOWERCASE = string.ascii_lowercase
    DIGITS = string.digits
    ALL_CHAR = LOWERCASE + UPPERCASE + DIGITS

    @staticmethod
    def get_random_password(login: str, number=3):
        pw_list = ([''.join(random.choices(RandomString.DIGITS, k=number)),
                    ''.join(random.choices(RandomString.LOWERCASE, k=number)),
                    ''.join(random.choices(RandomString.UPPERCASE, k=number)),
                    ]
                   + [login])
        random.shuffle(pw_list)
        random_password = ''.join(pw_list)

        return random_password

    @staticmethod
    def get_random_string(length):
        char_list = [random.choice(RandomString.ALL_CHAR) for i in range(length)]
        random.shuffle(char_list)
        random_string = ''.join(char_list)

        return random_string

    @staticmethod
    def get_digits(line):
        digits = re.findall(r'\d+', line)[0]
        return digits
