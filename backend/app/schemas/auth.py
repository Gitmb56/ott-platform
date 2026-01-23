from typing import Optional
from pydantic import BaseModel, EmailStr


# ===== REQUEST SCHEMAS =====

class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    full_name: Optional[str] = None


# ===== RESPONSE SCHEMAS =====

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ===== TOKEN PAYLOAD =====

class TokenData(BaseModel):
    email: Optional[EmailStr] = None
