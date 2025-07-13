import soundfile as sf
import numpy as np
import resampy
from dtmf import detect


def detect_dtmf_in_file(audio_file_path):
    try:
        audio_data_float, sample_rate = sf.read(audio_file_path)
        print(f"Loaded audio: {audio_data_float.shape}, {sample_rate} Hz")

        # Convert to mono if multi-channel
        if audio_data_float.ndim > 1:
            print(f"Audio has {audio_data_float.shape[1]} channels. Averaging to mono.")
            audio_data_float = audio_data_float.mean(axis=1)

        # Check duration
        duration_sec = len(audio_data_float) / sample_rate
        if duration_sec < 0.1:
            print("Error: Audio is too short for DTMF detection.")
            return

        # Normalize
        max_val = np.max(np.abs(audio_data_float))
        if max_val > 0:
            audio_data_float = audio_data_float / max_val

        # Resample to 8000 Hz
        if False and sample_rate != 8000:
            print(f"Resampling from {sample_rate} Hz to 8000 Hz...")
            audio_data_float = resampy.resample(audio_data_float, sample_rate, 8000)
            sample_rate = 8000

        # Convert to int16
        audio_np_int16 = (audio_data_float * 32767).astype(np.int16)

        # Run DTMF detection
        # Default detect_threshold is 0.7 (lower will detect more tones)
        # Assumes a tone duration of ≥ 40–50 ms.
        detected_tones = detect(audio_np_int16, sample_rate, detect_threshold=0.5)

        if detected_tones:
            count_all = 0
            count_tones = 0
            for detection in detected_tones:
                count_all += 1
                if detection.tone:
                    count_tones += 1
                    start_time = detection.start / sample_rate
                    end_time = detection.end / sample_rate
                    duration = end_time - start_time
                    print(
                        f"  Digit: {detection.tone}, Start: {start_time:.3f}s, End: {end_time:.3f}s, Duration: {1000*duration:.1f}ms"
                    )
            print(f"Tones detected: {count_tones}/{count_all}")
        else:
            print("No DTMF tones detected.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python your_script.py <audio_file>")
        sys.exit(1)

    audio_file = sys.argv[1]

    detect_dtmf_in_file(audio_file)
