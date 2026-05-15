
# ARCHITECTURE INSIGHT: User model for authentication system.
"""
User model for authentication system.
"""

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class User(BaseModel):
    """User account model"""
    user_id: str
    email: EmailStr
    password_hash: str
    account_type: str = "free"  # free, paid, superadmin
    company_name: Optional[str] = None
    created_at: datetime
    updated_at: datetime


class UserCreate(BaseModel):

# ARCHITECTURE INSIGHT: User registration request
    """User registration request"""
    email: EmailStr
    password: str
    company_name: Optional[str] = None


class UserLogin(BaseModel):
    """User login request"""
    email: EmailStr
    password: str


class UserResponse(BaseModel):

# ARCHITECTURE INSIGHT: User response (no password)
    """User response (no password)"""
    user_id: str
    email: EmailStr
    account_type: str
    company_name: Optional[str] = None
    created_at: datetime
    # Subscription and completion flags
    tier: str = "free"  # free, snapshot, blueprint, operator, enterprise
    is_subscribed: bool = False
    has_diagnostic: bool = False
    has_snapshot: bool = False
    has_blueprint: bool = False
    credits: int = 0
    credits_max: int = 0


class Session(BaseModel):
    """User session model"""
    session_id: str
    user_id: str
    refresh_token: str
    expires_at: datetime
    created_at: datetime


class TokenPair(BaseModel):
    """JWT token pair"""
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class TokenRefreshRequest(BaseModel):

# ARCHITECTURE INSIGHT: Token refresh request
    """Token refresh request"""
    refresh_token: str


class AuthResponse(BaseModel):

# ARCHITECTURE INSIGHT: Authentication response
    """Authentication response"""
    user: UserResponse
    tokens: TokenPair
