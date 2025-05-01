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
