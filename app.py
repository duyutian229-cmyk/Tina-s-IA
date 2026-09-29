import sqlite3
from pathlib import Path

import pygame
from flask import Flask, jsonify, render_template, request

from audio_player import play_test_audio, stop_test_audio

app = Flask(__name__)
DATABASE = Path(__file__).with_name("cafe_music.db")


def init_database():
    with sqlite3.connect(DATABASE) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                drink TEXT NOT NULL,
                nickname TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)


init_database()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    drink = request.form["drink"]
    nickname = request.form["nickname"].strip()

    if not nickname:
        return jsonify(error="Nickname is required."), 400

    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.execute(
            "INSERT INTO orders (drink, nickname) VALUES (?, ?)",
            (drink, nickname),
        )
        order_id = cursor.lastrowid

    audio_started = True
    try:
        play_test_audio()
    except (FileNotFoundError, pygame.error):
        app.logger.exception("Could not play the test audio")
        audio_started = False

    return jsonify(
        order_id=order_id,
        drink=drink,
        nickname=nickname,
        audio_started=audio_started,
    )


@app.route("/stop-audio", methods=["POST"])
def stop_audio():
    stop_test_audio()
    return jsonify(stopped=True)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
