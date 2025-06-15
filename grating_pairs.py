from stimulus_model import Solid, SinGrating, StimSequence, Stimuli
import uuid
import random

repetitions = 4  # 25
durations = [1000]  # Multiples of 20
# 0 is 1 (max) contrast, -1 is 0.1 contrast, -2 is 0.01
# -2.2 is minimal contrast, <=-2.3 is same color for 8 bit color
start_log_contrast = 0
log_contrast_step = -0.1
n_contrasts = 5
angles = [45]
speed = 10  # Degrees per second


def linear_to_hex(f: float) -> str:
    """Gamma compress linear light intensity between zero and one."""
    n = round(pow(f, 1 / 2.2) * 255)
    hex_value = ""
    if n < 10:
        hex_value = "0"
    hex_value += hex(n)[2:]  # Convert to hex, remove '0x' prefix
    return "#" + hex_value * 3


def log_contrast_to_linear(log_c: float) -> list[float]:
    c = pow(10, log_c) / 2
    return [0.5 + c, 0.5 - c]


cpds = [0.01, 0.1, 0.2, 0.3, 0.4, 0.5]  # Cycles per degree

colors = [
    [linear_to_hex(c) for c in log_contrast_to_linear(logC)]
    for logC in [
        (x * log_contrast_step + start_log_contrast) for x in range(n_contrasts)
    ]
]

stimuli: Stimuli = []

for cpd in cpds:
    for angle in angles:
        for color_pair in colors:
            for duration_ms in durations:
                for _ in range(repetitions):
                    id = str(uuid.uuid4())

                    left = SinGrating(
                        durationMs=duration_ms,
                        headMs=0,
                        bodyMs=500,
                        bgColor=color_pair[0],
                        speed=speed,
                        cpd=cpd,
                        angle=angle,
                        fgColor=color_pair[1],
                        meta={"group": id},
                    )
                    stimuli.append(left)

                    right = SinGrating(
                        durationMs=duration_ms,
                        headMs=0,
                        bodyMs=500,
                        bgColor=color_pair[0],
                        speed=speed,
                        cpd=cpd,
                        angle=-angle,
                        fgColor=color_pair[1],
                        meta={
                            "group": id,
                        },
                    )
                    stimuli.append(right)

random.shuffle(stimuli)

stim_sequence = StimSequence(
    title="Grating pairs",
    description="Generated from " + __file__,
    stimuli=stimuli,
)

print(stim_sequence.model_dump_json(exclude_none=True, indent=2))
