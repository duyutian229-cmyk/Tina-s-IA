import sys
from pathlib import Path

import pygame


DEFAULT_AUDIO_FILE = Path(__file__).parent / "audio" / "test.ogg"


def play_audio(audio_file):
    if not audio_file.exists():
        print(f"Audio file not found: {audio_file}")
        print("Put a test .ogg file there, or pass an audio file path to this script.")
        return

    pygame.mixer.init()

    try:
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play(loops=-1)
        print(f"Now playing: {audio_file.name}")
        input("Press Enter to stop playback...")
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()


if __name__ == "__main__":
    selected_file = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_AUDIO_FILE
    play_audio(selected_file)
