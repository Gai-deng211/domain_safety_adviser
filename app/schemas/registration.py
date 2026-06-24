from pydantic import BaseModel
from datetime import date
from typing import Optional

class RegistrationData(BaseModel):
    domain: str
    registered_on: Optional[date]
    expires_on: Optional[date]
    updated_on: Optional[date]
    registrar: Optional[str] = None
    registrant_organization: Optional[str] = None
    registrant_country: Optional[str] = None
    status: Optional[list[str]] = None

    def __str__(self) -> str:
        return (
            f"Domain: {self.domain}\n"
            f"Registered_on: {self.registered_on}\n"
            f"Expires_on: {self.expires_on}\n"
            f"Updated_on: {self.updated_on}\n"
            f"Registrar: {self.registrar}\n"
            f"Registrant Organization: {self.registrant_organization}\n"
            f"Registrant Country: {self.registrant_country}\n"
            f"Status: {', '.join(self.status) if self.status else None}\n"
        )