from enum import Enum
from typing import Literal, Optional, Union, Dict, Any, List
from pydantic import RootModel, BaseModel, field_validator


class StimTypeName(Enum):
    Solid = "Solid"
    Bar = "Bar"
    SinGrating = "SinGrating"
    SqrGrating = "SqrGrating"


class BaseStimulus(BaseModel):
    stimType: StimTypeName
    bgColor: Optional[str] = "black"
    durationMs: Optional[int] = 2000
    headMs: Optional[int] = None  # Duration of black before body
    bodyMs: Optional[int] = None  # Duration of stim between head and tail
    tailMs: Optional[int] = None  # Duration of black after body
    meta: Optional[Dict[str, Any] | None] = None
    model_config = {
        "use_enum_values": True,
        "exclude_none": True,
    }

    @field_validator("durationMs", "headMs", "bodyMs", "tailMs")
    @classmethod
    def validate_multiple_of_20(cls, value):
        if value is not None and (
            not isinstance(value, (int, float)) or value % 20 != 0
        ):
            raise ValueError(
                "Milliseconds must be a multiple of 20 to align with 50Hz framerate"
            )
        return value


class Solid(BaseStimulus):
    stimType: StimTypeName = "Solid"


class Bar(BaseStimulus):
    stimType: Optional[StimTypeName] = "Bar"
    fgColor: Optional[str] = "white"
    width: Optional[int] = 10  # Degrees
    speed: Optional[int] = 10  # Degrees per second
    angle: Optional[int] = 45  # Degrees


class Grating(BaseStimulus):
    stimType: Literal["SinGrating", "SqrGrating"]
    angle: Optional[int] = 45  # Degrees
    fgColor: Optional[str] = "white"  # Half the width
    speed: Optional[int] = 10  # Degrees per second
    width: Optional[int] = 10  # Degrees


class SinGrating(Grating):
    stimType: str = "SinGrating"


class SqrGrating(Grating):
    stimType: str = "SqrGrating"


Stimulus = RootModel[Union[Solid, Bar, SinGrating, SqrGrating]]
Stimuli = List[Stimulus]


class StimSequence(BaseModel):
    name: str
    description: Optional[str] = "Generated from " + __file__
    stimuli: Stimuli
