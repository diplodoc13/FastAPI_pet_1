from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(self: str):
        return pwd_cxt.hash(self)

    def verify(self: str, plain_password: str):
        return pwd_cxt.verify(plain_password, self)