# ECRIO Python Exercises Portfolio

This repository contains the Python exercises from the internship sheet, organized as a polished learning portfolio. The exercises are simple by design, but the implementation focuses on clarity, correct construct selection, reusable code, and practical examples.

## Portfolio Approach

Instead of creating forty-one disconnected files, the work is grouped by topic. This makes the repository easier to review and shows that the exercises are understood as connected Python skills:

- `01_python_basics.py`: beginner syntax, variables, loops, functions, and conditionals
- `02_files_regex_encoding.py`: regex, file handling, encoding, CSV, JSON, and binary operations
- `03_oop_logging_collections.py`: OOP, logging, collections, stack, queue, deque, and exceptions
- `04_data_analysis.py`: NumPy, pandas, cleaning, grouping, pivot tables, normalization, and trends
- `flask_portfolio_app/`: Flask routes, templates, forms, sessions, API handling, Docker, and deployment files
- `mqtt_examples/`: MQTT research, topic design, publisher/subscriber scripts, QoS, security notes, and concurrency ideas

## What Makes These Exercises Stand Out

- Repeated user interaction uses `while` loops because the number of repetitions is user-controlled.
- Fixed-size or range-based repetition uses `for` loops because the number of iterations is known.
- List comprehensions are used where they make filtering and transformation compact and readable.
- Functions are used to separate each exercise into reusable units.
- OOP examples use actual inheritance and encapsulation, not only class syntax.
- pandas is used for data analysis because vectorized operations are cleaner and more efficient than manual row loops.
- Logging and exception handling are included to show production-style thinking.
- Flask and MQTT examples are written as runnable mini systems, not only theory notes.

## Exercise Coverage

| Exercises | Topic | File or Folder | Implementation Strength |
|---|---|---|---|
| 1-4 | Python basics | `01_python_basics.py` | Shows variables, lists, tuples, functions, recursion, lambda, `for`, `while`-style thinking, `break`, `continue`, and validation |
| 5-6 | Files and encoding | `02_files_regex_encoding.py` | Uses regex extraction, date replacement, Base64 round-trip, ASCII conversion, URL encoding, ROT13, CSV, JSON, and binary files |
| 7-12 | OOP and reliability | `03_oop_logging_collections.py` | Uses dataclasses, inheritance, encapsulation, class methods, logging levels, stack, queue, deque, custom exceptions, `try/except/finally`, and assertions |
| 13-21 | Data analysis | `04_data_analysis.py` | Uses NumPy statistics, pandas cleaning, filtering, grouping, pivot tables, Min-Max scaling, Z-score normalization, JSON conversion, and rolling averages |
| 22-30 | Flask | `flask_portfolio_app/` | Includes routes, query parameters, templates, forms, sessions, JSON POST validation, `requirements.txt`, `Procfile`, and `Dockerfile` |
| 31-41 | MQTT | `mqtt_examples/` | Includes MQTT vs HTTP report, topic hierarchy, publisher, subscriber, callbacks, QoS examples, authentication/TLS notes, IoT simulation, and threading |

## Design Notes by Section

### Exercises 1-4: Python Basics

These exercises are implemented as functions so every output can be reused or tested. A recursive factorial function is included to show recursion clearly, while list comprehensions are used for even-number filtering because they are cleaner than manually appending inside long loops.

### Exercises 5-6: Files, Regex, and Encoding

The file exercises use `pathlib.Path` for modern file handling. Regex is used for email extraction and date replacement because pattern matching is the correct tool for structured text. Base64, ASCII, URL encoding, and ROT13 are implemented as round trips so the output proves the transformation can be reversed.

### Exercises 7-12: OOP, Logging, Collections, and Errors

The `Car` and `ElectricCar` classes demonstrate inheritance, method overriding, encapsulation through a private battery field, and a class method for car age. Collections are chosen by purpose: list for ordered data, tuple for fixed data, set for uniqueness, dictionary for labeled data, stack for last-in-first-out behavior, and deque for efficient queue operations.

### Exercises 13-21: Data Analysis

NumPy is used for numerical calculations, while pandas is used for table-shaped data. Missing values are filled before analysis, duplicates are removed, groupby operations summarize categories, and rolling averages demonstrate time-series trend extraction.

### Exercises 22-30: Flask

The Flask app is structured like a small web project. Routes are used for pages, templates are used for dynamic HTML, sessions are used for login state, and POST validation is used for JSON data. Deployment files are included to show awareness of production setup.

### Exercises 31-41: MQTT

The MQTT section shows both theory and implementation. It explains why MQTT is preferred for IoT-style repeated sensor messages, then provides publisher and subscriber scripts using topic wildcards and callback functions.

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run standard-library exercises:

```bash
python 01_python_basics.py
python 02_files_regex_encoding.py
python 03_oop_logging_collections.py
```

Run data exercises:

```bash
python 04_data_analysis.py
```

Run Flask examples:

```bash
python flask_portfolio_app/app.py
```

Run MQTT examples after installing Mosquitto:

```bash
python mqtt_examples/subscriber.py
python mqtt_examples/publisher.py
```

## Verification

The standard-library and pandas exercise files were executed locally. Flask and MQTT scripts are dependency-ready and include their required project files, but full MQTT execution requires a local Mosquitto broker.


