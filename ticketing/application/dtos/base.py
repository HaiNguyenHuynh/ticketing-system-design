from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class BaseDTO(BaseModel):
    class Config:
        from_attributes = True
        use_enum_values = True


class BaseResponse(BaseDTO):
    success: bool = True
    error_code: Optional[str]
    message: Optional[str]
    timestamp: datetime = datetime.now()
