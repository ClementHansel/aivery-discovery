
# ARCHITECTURE INSIGHT: Data models for contact form
"""Data models for contact form"""
from pydantic import BaseModel, Field, EmailStr


class ContactForm(BaseModel):

# ARCHITECTURE INSIGHT: Contact form submission
    """Contact form submission"""
    name: str = Field(min_length=1, description="Contact name")
    company: str = Field(min_length=1, description="Company name")
    email: EmailStr = Field(description="Contact email address")
    message: str = Field(min_length=10, description="What do you want to build?")


class ContactResponse(BaseModel):

# ARCHITECTURE INSIGHT: Response after contact form submission
    """Response after contact form submission"""
    success: bool = Field(description="Whether submission was successful")
    message: str = Field(description="Response message")
