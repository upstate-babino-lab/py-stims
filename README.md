# py-stims

Python utilities for creating `.stims.json` stimulus sequence files, for use with EyeStims

## Install dependency

With Python version `> 3.10`, there is only one dependency:

```Bash
$ pip install pydantic
```

#### Or, use the provided Conda environment:

Assuming you have already [installed conda](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html)

```
$ conda env create -f environment.yml -n stims
$ conda activate stims
```

## Minimal Example

The program `example_stims.py` creates four stimuli:

```Python
from stimulus_model import Solid, Bar, SinGrating, SqrGrating, StimSequence

stimuli = [
    Solid(bodyMs=1000, bgColor="green"),
    Bar(fgColor="orange"),
    SqrGrating(),
    SinGrating(speed=50, angle=-45),
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

This creates the file `example.stims.json` which can be loaded by [EyeStims](https://github.com/upstate-babino-lab/eye-stims) to build a video.

```JSON
{
  "title": "Example stims from Python",
  "description": "Generated from /home/pwellner/myrepos/py-stims/example_stims.py",
  "stimuli": [
    {
      "stimType": "Solid",
      "bgColor": "green",
      "durationMs": 2000,
      "bodyMs": 1000
    },
    {
      "stimType": "Bar",
      "bgColor": "black",
      "durationMs": 2000,
      "fgColor": "orange",
      "width": 10,
      "speed": 10,
      "angle": 45
    },
    {
      "stimType": "SqrGrating",
      "bgColor": "black",
      "durationMs": 2000,
      "angle": 45,
      "fgColor": "white",
      "speed": 10,
      "width": 10
    },
    {
      "stimType": "SinGrating",
      "bgColor": "black",
      "durationMs": 2000,
      "angle": -45,
      "fgColor": "white",
      "speed": 50,
      "width": 10
    }
  ]
}
```

## More complex Example

For a more interesting example, see [grating_pairs.py](grating_pairs.py
