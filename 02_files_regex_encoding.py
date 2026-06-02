"""Exercises 5-6: regex, encoding, files, CSV, JSON, and binary operations."""

import base64
import csv
import json
import re
from codecs import encode as codec_encode
from pathlib import Path
from urllib.parse import quote, unquote


WORK_DIR = Path("generated_outputs")
INPUT_TEXT = (
    "Contact alice@example.com and bob.smith@school.edu on 2026-05-04. "
    "Backup contact: support@erico.org. Meeting date: 2026-06-02."
)


def ensure_input_file():
    WORK_DIR.mkdir(exist_ok=True)
    input_path = WORK_DIR / "input.txt"
    input_path.write_text(INPUT_TEXT, encoding="utf-8")
    return input_path


def exercise_5_text_transformations():
    input_path = ensure_input_file()
    text = input_path.read_text(encoding="utf-8")

    emails = re.findall(r"[\w.-]+@[\w.-]+\.[A-Za-z]{2,}", text)
    (WORK_DIR / "emails.txt").write_text("\n".join(emails), encoding="utf-8")

    updated_text = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3/\2/\1", text)
    (WORK_DIR / "updated_text.txt").write_text(updated_text, encoding="utf-8")

    encoded = base64.b64encode(text.encode("utf-8")).decode("utf-8")
    (WORK_DIR / "encoded.txt").write_text(encoded, encoding="utf-8")

    decoded = base64.b64decode(encoded).decode("utf-8")
    (WORK_DIR / "decoded.txt").write_text(decoded, encoding="utf-8")

    ascii_values = " ".join(str(ord(character)) for character in text)
    (WORK_DIR / "ascii_values.txt").write_text(ascii_values, encoding="utf-8")

    ascii_decoded = "".join(chr(int(value)) for value in ascii_values.split())
    (WORK_DIR / "ascii_decoded.txt").write_text(ascii_decoded, encoding="utf-8")

    url_encoded = quote(text)
    (WORK_DIR / "url_encoded.txt").write_text(url_encoded, encoding="utf-8")

    rot13_text = codec_encode(text, "rot_13")
    (WORK_DIR / "rot13_encoded.txt").write_text(rot13_text, encoding="utf-8")

    return {
        "emails": emails,
        "updated_text": updated_text,
        "base64_round_trip": decoded == text,
        "ascii_round_trip": ascii_decoded == text,
        "url_round_trip": unquote(url_encoded) == text,
        "rot13_preview": rot13_text[:40],
    }


def exercise_6_file_operations():
    WORK_DIR.mkdir(exist_ok=True)
    notes_path = WORK_DIR / "notes.txt"

    with notes_path.open("w", encoding="utf-8") as file:
        file.write("First line\n")
        file.write("Second line\n")

    with notes_path.open("a", encoding="utf-8") as file:
        file.write("Appended line\n")

    csv_path = WORK_DIR / "students.csv"
    rows = [
        {"name": "Asha", "score": 91},
        {"name": "Ravi", "score": 86},
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "score"])
        writer.writeheader()
        writer.writerows(rows)

    json_path = WORK_DIR / "students.json"
    json_path.write_text(json.dumps(rows, indent=2), encoding="utf-8")

    binary_path = WORK_DIR / "sample.bin"
    binary_path.write_bytes(bytes([80, 89, 84, 72, 79, 78]))

    line_count = sum(1 for _ in notes_path.open(encoding="utf-8"))
    return {
        "notes": notes_path.read_text(encoding="utf-8").splitlines(),
        "csv_file": str(csv_path),
        "json_file": str(json_path),
        "binary_text": binary_path.read_bytes().decode("ascii"),
        "line_count": line_count,
    }


if __name__ == "__main__":
    print("Exercise 5:", exercise_5_text_transformations())
    print("Exercise 6:", exercise_6_file_operations())
