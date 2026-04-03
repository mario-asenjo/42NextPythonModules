"""
Demonstrates the mastering of validation using @model_validator
for complex business rules
"""
from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, model_validator, ValidationError


class ContactType(str, Enum):
    """Enum for different types of AlienContact's contact type"""
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """Base class for AlienContact objects with pydantic validations"""
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(default=datetime.now())
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType = Field()
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validate_contact(self) -> "AlienContact":
        """Validates requirements based on subject specifications"""
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID should start with 'AC'...")
        if not self.is_verified:
            raise ValueError("Physical contact reports must be verified...")
        if self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses...")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should include received messages...")
        return self

    def print_information(self) -> None:
        print(f"ID: {self.contact_id}")
        print(f"Type: {self.contact_type.value}")
        print(f"Location: {self.location}")
        print(f"Signal: {self.signal_strength}/10")
        print(f"Duration: {self.duration_minutes} minutes")
        print(f"Witnesses: {self.witness_count}")
        print(f"Message: '{self.message_received}'")


def main() -> None:
    """Main CLI entrypoint for AlienContact class demonstration"""
    print("Alien Contact Log Validation")
    print("=" * 40)
    try:
        valid_contact: AlienContact = AlienContact(
            contact_id="AC_2024_001",
            contact_type=ContactType.RADIO,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            is_verified=True,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
        valid_contact.print_information()
        print("\n" + "=" * 40)
        invalid_contact: AlienContact = AlienContact(
            contact_id="AC_2024_001",
            contact_type=ContactType.RADIO,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            is_verified=True,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli"
        )
        invalid_contact.print_information()
    except ValidationError as exc:
        print(exc.errors()[0]['ctx']['error'].args[0])


if __name__ == "__main__":
    main()
