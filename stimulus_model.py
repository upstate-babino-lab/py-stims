from enum import Enum
from typing import Literal, Optional, Union, Dict, Any, List
from pydantic import RootModel, BaseModel


class StimTypeName(Enum):
    Solid = "Solid"
    Bar = "Bar"
    SinGrating = "SinGrating"
    SqrGrating = "SqrGrating"


class BaseStimulus(BaseModel):
    name: StimTypeName
    bgColor: Optional[str] = "black"
    durationMs: Optional[float] = 5000
    headMs: Optional[float] = None
    bodyMs: Optional[float] = None
    tailMs: Optional[float] = None
    meta: Optional[Dict[str, Any] | None] = None
    model_config = {
        "use_enum_values": True,
        "exclude_none": True,
    }


class Solid(BaseStimulus):
    name: StimTypeName = "Solid"


class Bar(BaseStimulus):
    name: Optional[StimTypeName] = "Bar"
    fgColor: Optional[str] = "white"
    width: Optional[float] = 10
    speed: Optional[float] = 10
    angle: Optional[float] = 45


class Grating(BaseStimulus):
    name: Literal["SinGrating", "SqrGrating"]
    angle: Optional[float] = 45
    fgColor: Optional[str] = "white"
    speed: Optional[float] = 10
    width: Optional[float] = 10


class SinGrating(Grating):
    name: str = "SinGrating"


class SqrGrating(Grating):
    name: str = "SqrGrating"


Stimulus = RootModel[Union[Solid, Bar, SinGrating, SqrGrating]]

class StimSequence(BaseModel):
    name: str
    description: Optional[str] = "Generated from " + __file__
    stimuli: List[Stimulus]