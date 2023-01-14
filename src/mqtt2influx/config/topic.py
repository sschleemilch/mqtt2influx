from dataclasses import dataclass

@dataclass
class Topic:
    name: str
    type: str

    def __repr__(self) -> str:
        return f"Topic, {self.name=}, {self.type=}"

    def __hash__(self) -> int:
        return hash(self.name) + hash(self.type)