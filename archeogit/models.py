import dataclasses

from typing import Dict, List


@dataclasses.dataclass(frozen=True)
class Line:
    number: int
    change: str


@dataclasses.dataclass(frozen=True)
class Modifier:
    sha: str
    path: str


@dataclasses.dataclass(frozen=True)
class Section:
    header: List[int]
    body: Dict[str, int]
    footer: List[int]


@dataclasses.dataclass(frozen=True)
class Hunk:
    lines: List[Line]
