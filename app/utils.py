# store all utilities like hashing logic

from passlib.context import CryptContext

# we are telling passlib what is the default hashing algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str) -> str:
    # This function hashes the plain-text password before saving it to the database.
    # We store the hash, not the raw password.
    return pwd_context.hash(password)


def verify(plain_password: str, hashed_password: str) -> bool:
    # This compares the plain password entered by the user with the stored hash.
    return pwd_context.verify(plain_password, hashed_password)



