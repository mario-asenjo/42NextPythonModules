"""
Demonstration on nested pydantic models and complex data relationships
"""
from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, Field, model_validator, ValidationError


class Rank(str, Enum):
    """Crew ranks representation"""
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """Individual crew member representation"""
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field(default=Rank.CADET)
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    """Mission with crew list representation"""
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(default=datetime.now())
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(max_length=5000, default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    def is_cap_in_crew(self) -> bool:
        """Verifies that there is a Captain or a Commander in SpaceMission"""
        for member in self.crew:
            if member.rank is Rank.CAPTAIN or member.rank is Rank.COMMANDER:
                return True
        return False

    def verify_experience(self) -> bool:
        """Verifies that if Long mission, everyone is +5 years experienced"""
        if self.duration_days > 365:
            for member in self.crew:
                if member.years_experience < 5:
                    return False
            return True
        else:
            return True

    @model_validator(mode="after")
    def validate_space_mission(self) -> "SpaceMission":
        """Assure that every safety requirement is satisfied"""
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'...")
        if not self.is_cap_in_crew():
            raise ValueError(
                "Mission must have at least one Commander or Captain..."
            )
        if not self.verify_experience():
            raise ValueError(
                "Long missions (> 365 days) need 50% "
                "experienced crew (+5 years)..."
            )
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active...")
        return self

    def print_information(self) -> None:
        """Print information on SpaceMission object"""
        print(f"Mission: {self.mission_name}")
        print(f"ID: {self.mission_id}")
        print(f"Destination: {self.destination}")
        print(f"Duration: {self.duration_days}")
        print(f"Budget: ${self.budget_millions}M")
        print("Crew members:")
        for member in self.crew:
            print(
                f"- {member.name} ({member.rank.value})"
                f" - {member.specialization}"
            )


def main() -> None:
    """Demonstration of the Space Mission Crew validation program"""
    print("Space Mission Crew Validation")
    print("=" * 40)
    try:
        valid_mission: SpaceMission = SpaceMission(
            mission_name="Mars Colony Establishment",
            mission_id="M2024_MARS",
            destination="Mars",
            duration_days=900,
            budget_millions=2500,
            crew=[
                CrewMember(
                    member_id="SC-sarah",
                    name="Sarah Connor",
                    rank=Rank.COMMANDER,
                    age=20,
                    specialization="Mission Command",
                    years_experience=6,
                    is_active=True
                ),
                CrewMember(
                    member_id="JS-john",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=20,
                    specialization="Navigation",
                    years_experience=6,
                    is_active=True
                ),
                CrewMember(
                    member_id="AJ-alice",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=20,
                    specialization="Engineering",
                    years_experience=6,
                    is_active=True
                )
            ],
            mission_status="Active",
            launch_date=datetime.now()
        )
        valid_mission.print_information()
        print("\n" + "=" * 40)
        invalid_mission: SpaceMission = SpaceMission(
            mission_name="Mars Colony Establishment",
            mission_id="M2024_MARS",
            destination="Mars",
            duration_days=900,
            budget_millions=2500,
            crew=[
                CrewMember(
                    member_id="SC-sarah",
                    name="Sarah Connor",
                    rank=Rank.LIEUTENANT,
                    age=20,
                    specialization="Mission Command",
                    years_experience=2,
                    is_active=True
                ),
                CrewMember(
                    member_id="JS-john",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=20,
                    specialization="Navigation",
                    years_experience=2,
                    is_active=True
                ),
                CrewMember(
                    member_id="AJ-alice",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=20,
                    specialization="Engineering",
                    years_experience=2,
                    is_active=True
                )
            ],
            mission_status="Active",
            launch_date=datetime.now()
        )
        invalid_mission.print_information()
    except ValidationError as exc:
        print(exc.errors()[0]['ctx']['error'])


if __name__ == "__main__":
    main()
