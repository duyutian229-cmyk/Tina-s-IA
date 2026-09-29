from pathlib import Path
from threading import Lock

import pygame


TEST_AUDIO = Path(__file__).parent / "audio" / "test.ogg"
_player_lock = Lock()


def play_test_audio():
    """Start the test audio on the computer running Flask."""
    if not TEST_AUDIO.is_file():
        raise FileNotFoundError(f"Audio file not found: {TEST_AUDIO}")

    with _player_lock:
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        pygame.mixer.music.load(str(TEST_AUDIO))
        pygame.mixer.music.play(loops=-1)


def stop_test_audio():
    """Stop the test audio without stopping the Flask server."""
    with _player_lock:
        if pygame.mixer.get_init():
            pygame.mixer.music.stop()
