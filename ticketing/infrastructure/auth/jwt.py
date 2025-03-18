from jose import JWTError, jwt

from infrastructure.config import settings


class JWTService:
    def create_access_token(self, data: dict):
        return jwt.encode(data, settings.secret_key, algorithm="HS256")

    def verify_token(self, token: str) -> dict:
        try:
            return jwt.decode(token, settings.secret_key, algorithms=["HS256"])
        except JWTError:
            raise ValueError("Invalid token")
