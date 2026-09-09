# Application Activity Logger

A menu-driven Python application that demonstrates logging, exception handling, and modular design. Users can authenticate, perform calculations, and manage files — all activities are captured in log files with timestamps.

---

## Project Structure

```
application_activity_logger/
├── main.py              # Entry point — menu loop and user dispatch
├── logger.py            # Centralized logging configuration
├── auth.py              # Login and logout functionality
├── calculator.py        # Basic arithmetic operations
├── file_operations.py   # Read and write files from data/ directory
├── data/                # Directory for user-created files (auto-generated)
└── logs/
    ├── application.log  # All log levels (DEBUG through CRITICAL)
    └── error.log        # WARNING and above only
```

## Modules

| Module | Purpose |
|---|---|
| `main.py` | Displays the menu, tracks login state, routes user choices to other modules |
| `logger.py` | Configures loggers with file and console handlers using a unified format |
| `auth.py` | Handles login (`admin` / `admin123`) and logout with session tracking |
| `calculator.py` | Prompts for two numbers and an operator, returns the result |
| `file_operations.py` | Reads from and writes to files inside the `data/` directory |

## Running the Application

```bash
cd application_activity_logger
python3 main.py
```

### Menu Options

| Choice | Action | Requires Login |
|---|---|---|
| 1 | Login | No |
| 2 | Calculate | Yes |
| 3 | Read a File | Yes |
| 4 | Write a File | Yes |
| 5 | Logout | — |

### Credentials

- **Username:** `admin`
- **Password:** `admin123`

---

## Logging Configuration

### Log Format

All log entries use a human-readable format:

```
2026-09-09 22:19:50 | INFO     | auth.py | User logged in
```

```
timestamp | level | filename | message
```

### Log Files

| File | Contents |
|---|---|
| `logs/application.log` | Every log event at DEBUG level and above |
| `logs/error.log` | Only WARNING, ERROR, and CRITICAL events |

### Handler Summary

| Handler | Output | Minimum Level |
|---|---|---|
| `FileHandler` (application.log) | `logs/application.log` | DEBUG |
| `FileHandler` (error.log) | `logs/error.log` | WARNING |
| `StreamHandler` | Console / terminal | INFO |

---

## Logging Levels

Python's `logging` module defines five standard severity levels. Each level has a numeric value — lower numbers indicate less severe events, higher numbers indicate more critical events.

| Level | Numeric Value | Description |
|---|---|---|
| `DEBUG` | **10** | Detailed diagnostic information intended for developers. Example: `"Login attempt started"` |
| `INFO` | **20** | Confirmation that things are working as expected. Example: `"User logged in"` |
| `WARNING` | **30** | Something unexpected happened, but the application can continue. Example: `"File was empty"` |
| `ERROR` | **40** | The application failed to perform a specific operation. Example: `"File could not be opened"` |
| `CRITICAL` | **50** | The application itself may be unable to continue running. Example: `"Unexpected application failure"` |

### How Levels Are Used in This Project

```
DEBUG    →  Captures entry points of functions (login started, calculation started, etc.)
INFO     →  Confirms successful operations (user logged in, file written, calculation done)
WARNING  →  Handles recoverable issues (empty file, division by zero, invalid input)
ERROR    →  Logs operation failures (file not found, permission denied)
CRITICAL →  Logs unexpected exceptions caught by top-level handlers
```

### Level Hierarchy

A logger set to level `X` captures all messages with a numeric value **greater than or equal to** `X`. For example:

- `application.log` is set to `DEBUG` (10) → captures all 5 levels
- `error.log` is set to `WARNING` (30) → captures WARNING, ERROR, and CRITICAL only
- Console output is set to `INFO` (20) → captures INFO, WARNING, ERROR, and CRITICAL
