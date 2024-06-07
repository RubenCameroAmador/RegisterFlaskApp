from Repositories.RegisterRepository import RegisterRepository
from Models.RegisterModel import Register
import hashlib
from Utilities.OTP import OTP
from Utilities.MailSend import MailSend

class RegisterController():
    def __init__(self):
        self.register_repository = RegisterRepository()
        self.mail_send = MailSend()

    def create(self, infoUser):
        new_user = Register(infoUser)
        user_password = infoUser["password"]
        if(self.uniqueName(infoUser["email"])==False):
            new_user.password = self.encrypt_sha256(user_password)
            otp = OTP.generate_otp()
            new_user.otp_code = otp

            #Envio el correo: 
            self.mail_send.send_email(infoUser["email"], otp)

            self.register_repository.save(new_user)
            message = {
                "status": "User created",
                "message": "User have been created succesfully"
            }
            return message
        else:
            message = {
                "status": "User have not been created",
                "message": "The email address already exists"
            }
            return message

    def uniqueName(self, email):
        users = self.register_repository.findAll()
        for user in users:
            if(email == user["email"]):
                return True
        return False
    
    def encrypt_sha256(self, input_string):
        sha256_hash = hashlib.sha256()
        sha256_hash.update(input_string.encode('utf-8'))
        return sha256_hash.hexdigest()