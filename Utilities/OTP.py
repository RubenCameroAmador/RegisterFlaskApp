import random

class OTP:
    @staticmethod
    def generate_otp():
        four_digit_number = random.randint(1000, 9999)
        return str(four_digit_number)