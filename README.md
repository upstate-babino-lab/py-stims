# py-stims
Python utilities for creating `.stims.json` stimulus sequence files, for use with EyeStims

## Install dependency
```Bash
$ pip install pydantic
```

## Example
The following file `example_stims.py` creates four stimuli:
```Python
from stimulus_model import Solid, Bar, SinGrating, SqrGrating, StimSequence

stimuli = [
    Solid(bodyMs=1000, bgColor="green"),
    Bar(fgColor="orange"),
    SqrGrating(),
    SinGrating(speed=50, angle=-45)
    ]

stim_sequence = StimSequence(
    name="Example stims from Python",
    description="Generated from " + __file__,
    stimuli=stimuli,
)


print(stim_sequence.model_dump_json(exclude_none=True, indent=2))
```

## Creating a .stims.json file
From the command line, run your program as follows
```Bash
$ python example_stims.py > example.stims.json
```
This creates the following file `example.stims.json` that can be loaded by [EyeStims](https://github.com/upstate-babino-lab/eye-stims) to build a video `.mp4` file.
```JSON
{
  "name": "Example stims from Python",
  "description": "Generated from /home/pwellner/myrepos/py-stims/example_stims.py",
  "stimuli": [
    {
      "name": "Solid",
      "bgColor": "green",
      "durationMs": 5000.0,
      "bodyMs": 1000.0
    },
    {
      "name": "Bar",
      "bgColor": "black",
      "durationMs": 5000.0,
      "fgColor": "orange",
      "width": 10.0,
      "speed": 10.0,
      "angle": 45.0
    },
    {
      "name": "SqrGrating",
      "bgColor": "black",
      "durationMs": 5000.0,
      "angle": 45.0,
      "fgColor": "white",
      "speed": 10.0,
      "width": 10.0
    },
    {
      "name": "SinGrating",
      "bgColor": "black",
      "durationMs": 5000.0,
      "angle": -45.0,
      "fgColor": "white",
      "speed": 50.0,
      "width": 10.0
    }
  ]
}
```