*This project has been created as part of the 42 curriculum by mfakih.*

### Data Quest: The Cyber Archives
---

Welcome to the **Digital Preservation Division**. This module is a deep dive into Python’s file handling and resource management, designed to simulate high-stakes data archiving in the year 2087.

## Overview
This project focuses on mastering **Python File I/O**, **Stream Management**, and **Context Managers** to ensure no digital knowledge is lost to information entropy.

---

| Exercise | Title | Core Concept | Purpose |
| :--- | :--- | :--- | :--- |
| **Ex 00** | Ancient Text Recovery | `open(mode='r')` | Recovering data from legacy storage units. |
| **Ex 01** | Archive Creation | `open(mode='w')` | Establishing new preservation protocols. |
| **Ex 02** | Stream Management | `sys.stdin/out/err` | Mastering the three sacred data channels. |
| **Ex 03** | Vault Security | `with` Statement | Ensuring automatic resource cleanup (RAII). |
| **Ex 04** | Crisis Response | `try...except` | Handling corrupted or missing archives. |

---

## General Rules

* **Python 3.10+** only.
* **Strict flake8** linting compliance.
* **Type hints** are mandatory for all functions.
* **Authorized Tools:** Only the `sys` module and built-ins (`open`, `print`, `input`) are allowed.

---

## How to Test

Before beginning your missions, you must generate the required test files:

1. **Extract Tools:** `tar -xzf data-generator-tools.tar.gz`
2. **Generate Data:** `python3 data_generator.py`

### Manual CLI Testing
Run each script to verify the output matches the required system logs:

* **Ex 00:** `python3 ft_ancient_text.py`
* **Ex 02:** `python3 ft_stream_management.py`
* **Ex 04:** `python3 ft_crisis_response.py`

---

## The Archivist's Code

> "Every file operation must be secure, every resource properly managed, and every error gracefully handled. The Archives have survived because archivists follow these sacred protocols."