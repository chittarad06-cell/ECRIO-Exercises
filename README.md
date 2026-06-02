# ERICO Python Exercises

This repository contains clean, runnable solutions for the Python exercises from the internship sheet. The work is organized by topic so it looks like a learning portfolio instead of a random collection of files.

## Highlights

- Beginner Python basics with variables, loops, functions, and input validation
- Regex, Base64, ASCII/Unicode, URL encoding, ROT13, CSV, JSON, and binary file handling
- OOP examples using inheritance, encapsulation, class methods, and safe string representations
- API, custom module, logging, collections, stack, queue, deque, and exception handling examples
- Data analysis exercises using NumPy and pandas
- Flask examples for routes, templates, forms, sessions, JSON POST handling, Docker, and production deployment files
- MQTT examples for topics, publisher/subscriber logic, QoS, authentication, TLS notes, and threaded subscribers

## How to Run

Install dependencies if you are running everything locally:

```bash
pip install -r requirements.txt
```

Run the standard-library exercises:

```bash
python 01_python_basics.py
python 02_files_regex_encoding.py
python 03_oop_logging_collections.py
```

Run the data-analysis exercises:

```bash
python 04_data_analysis.py
```

Run the Flask app after installing Flask:

```bash
python flask_portfolio_app/app.py
```

Run MQTT scripts after installing Mosquitto and paho-mqtt:

```bash
python mqtt_examples/publisher.py
python mqtt_examples/subscriber.py
```

## Exercise Map

| Exercises | File or Folder |
|---|---|
| 1-4 | `01_python_basics.py` |
| 5-6 | `02_files_regex_encoding.py` |
| 7-12 | `03_oop_logging_collections.py` |
| 13-21 | `04_data_analysis.py` |
| 22-30 | `flask_portfolio_app/` |
| 31-41 | `mqtt_examples/` |
