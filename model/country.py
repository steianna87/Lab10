from dataclasses import dataclass


@dataclass
class Country:
    StateAbb: str
    CCode: int
    StateNme: str

    def __str__(self):
        return f"{self.StateNme}"

    def __hash__(self):
        return hash(self.CCode)
