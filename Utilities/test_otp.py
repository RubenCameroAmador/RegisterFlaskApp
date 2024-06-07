import unittest
from OTP import OTP  # Asegúrate de que la ruta sea correcta

class TestOTP(unittest.TestCase):
    def test_generate_otp(self):
        otp = OTP.generate_otp()

        # Verificar que el OTP es una cadena de 4 dígitos
        self.assertEqual(len(otp), 4)
        self.assertTrue(otp.isdigit())  # Verificar que el OTP es un número

        # Verificar que el valor del OTP está dentro del rango esperado
        otp_int = int(otp)
        self.assertGreaterEqual(otp_int, 1000)
        self.assertLessEqual(otp_int, 9999)

if __name__ == '__main__':
    unittest.main()
