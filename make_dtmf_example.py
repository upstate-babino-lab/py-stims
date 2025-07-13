import numpy as np
import soundfile as sf

# DTMF tone frequencies (Hz)
DTMF_FREQS = {
    "1": (697, 1209),
    "2": (697, 1336),
    "3": (697, 1477),
    "A": (697, 1633),
    "4": (770, 1209),
    "5": (770, 1336),
    "6": (770, 1477),
    "B": (770, 1633),
    "7": (852, 1209),
    "8": (852, 1336),
    "9": (852, 1477),
    "C": (852, 1633),
    "*": (941, 1209),
    "0": (941, 1336),
    "#": (941, 1477),
    "D": (941, 1633),
}


def generate_dtmf_tone(digit, duration_ms=100, sample_rate=8000, amplitude=0.5):
    """Generate a DTMF tone for a given digit."""
    if digit not in DTMF_FREQS:
        raise ValueError(f"Invalid DTMF digit: {digit}")
    f1, f2 = DTMF_FREQS[digit]
    t = np.linspace(
        0, duration_ms / 1000, int(sample_rate * duration_ms / 1000), endpoint=False
    )
    tone = amplitude * (np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t))
    return tone


def generate_dtmf_sequence(
    sequence, tone_duration=100, pause_duration=0.1, sample_rate=8000
):
    audio = []
    silence = np.zeros(int(pause_duration * sample_rate))
    for digit in sequence:
        tone = generate_dtmf_tone(digit, tone_duration, sample_rate)
        audio.append(tone)
        audio.append(silence)
    return np.concatenate(audio)


if __name__ == "__main__":
    dtmf_sequence = "123A"
    sample_rate = 8000
    audio_data = generate_dtmf_sequence(dtmf_sequence, sample_rate=sample_rate)

    # Save to a WAV file
    sf.write("dtmf_example_123A.wav", audio_data, samplerate=sample_rate)
    print("Generated 'dtmf_example_123A.wav' with DTMF sequence:", dtmf_sequence)
