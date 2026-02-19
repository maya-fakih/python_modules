from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import List
from enum import Enum


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_mission_rules(self):
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        has_commander_captain = any(
            member.rank in [Rank.COMMANDER, Rank.CAPTAIN]
            for member in self.crew
        )
        if not has_commander_captain:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced_count = sum(
                1 for member in self.crew
                if member.years_experience >= 5
            )
            if experienced_count < len(self.crew) / 2:
                s = "need 50% experienced crew (5+ years)"
                raise ValueError(f"Long missions (>365 days) {s}")

        inactive_members = [
            member.name for member in self.crew if not member.is_active
        ]
        if inactive_members:
            raise ValueError(
                f"Inactive crew members: {', '.join(inactive_members)}"
            )

        return self


def main():
    print("Space Mission Crew Validation")
    print("=" * 40)

    valid_crew = [
        CrewMember(
            member_id="CMD01",
            name="Sarah Connor",
            rank=Rank.COMMANDER,
            age=45,
            specialization="Mission Command",
            years_experience=20,
            is_active=True
        ),
        CrewMember(
            member_id="LT02",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=32,
            specialization="Navigation",
            years_experience=8,
            is_active=True
        ),
        CrewMember(
            member_id="OFF03",
            name="Alice Johnson",
            rank=Rank.OFFICER,
            age=28,
            specialization="Engineering",
            years_experience=5,
            is_active=True
        )
    ]

    valid_mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date="2025-01-15T10:00:00",
        duration_days=900,
        crew=valid_crew,
        budget_millions=2500.0
    )

    print("\nValid mission created:")
    print(f"Mission: {valid_mission.mission_name}")
    print(f"ID: {valid_mission.mission_id}")
    print(f"Destination: {valid_mission.destination}")
    print(f"Duration: {valid_mission.duration_days} days")
    print(f"Budget: ${valid_mission.budget_millions}M")
    print(f"Crew size: {len(valid_mission.crew)}")
    print("Crew members:")
    for member in valid_mission.crew:
        print(f"- {member.name} ({member.rank.value}) - "
              f"{member.specialization}")

    print("=" * 40)

    invalid_crew = [
        CrewMember(
            member_id="OFF01",
            name="John Doe",
            rank=Rank.OFFICER,
            age=30,
            specialization="Pilot",
            years_experience=3,
            is_active=True
        ),
        CrewMember(
            member_id="OFF02",
            name="Jane Doe",
            rank=Rank.OFFICER,
            age=28,
            specialization="Engineer",
            years_experience=2,
            is_active=True
        )
    ]

    try:
        SpaceMission(
            mission_id="M2024_VENUS",
            mission_name="Venus Expedition",
            destination="Venus",
            launch_date="2025-03-20T10:00:00",
            duration_days=200,
            crew=invalid_crew,
            budget_millions=1500.0
        )
    except ValidationError as e:
        print("\nExpected validation error:")
        for error in e.errors():
            print(f"- {error['msg']}")


if __name__ == "__main__":
    main()
