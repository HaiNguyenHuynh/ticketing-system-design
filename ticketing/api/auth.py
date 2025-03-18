from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from api.exceptions import InvalidCredentialsError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")

async def get_current_user(
    token: str = Depends(oauth2_scheme)
) -> User:
    credentials_exception = InvalidCredentialsError()
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: UUID = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = await user_repo.find_by_id(user_id)
    if user is None:
        raise credentials_exception
        
    return user