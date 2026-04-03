"""
Demonstration of Field validations using pydantic-2
"""
import sys
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """Base class with simple validation Fields"""

    station_id: str = Field(max_length=10, min_length=3)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0, le=100)
    oxygen_level: float = Field(ge=0, le=100)
    last_maintenance: datetime = Field(default=datetime.now())
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(max_length=200, )

    def print_information(self):
        """Print a resume of the SpaceStation"""
        print(f"ID: {self.station_id}")
        print(f"Name: {self.name}")
        print(f"Crew: {self.crew_size} people")
        print(f"Power: {self.power_level}%")
        print(f"Oxygen: {self.oxygen_level}%")
        print(
            f"Status: "
            f"{"Operational" if self.is_operational else "No operational"}"
        )
        print(f"Last Maintenance: {self.last_maintenance.ctime()}")
        print(f"Notes: {self.notes}" if self.notes is not None else "")


def main() -> None:
    """Demonstration of the validation in class attributes"""
    print("Space Station Data Validation")
    print("=" * 40)
    try:
        valid_station: SpaceStation = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True,
            notes=None
        )
        print("Valid station created:")
        valid_station.print_information()
        print("=" * 40)
        print("Expected validation error:")
        invalid_station: SpaceStation = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=25,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            is_operational=True,
            notes=None
        )
        invalid_station.print_information()
    except ValidationError as exc:
        print(exc.errors()[0]['msg'], file=sys.stderr)


if __name__ == "__main__":
    main()
