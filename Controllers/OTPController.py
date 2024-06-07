from Models.OTPModel import OTP
from Repositories.RegisterRepository import RegisterRepository
from Models.RegisterModel import Register

class OTPController():
    def __init__(self):
        self.register_repository = RegisterRepository()

    #def validate_otp(self, otp_info):
