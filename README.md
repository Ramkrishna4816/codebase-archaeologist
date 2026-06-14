# Codebase Archaeologist

Codebase Archaeologist is an experimental software evolution research project that studies how software systems change over time.

Unlike traditional repository analysis tools that focus on code structure, architecture, or documentation, Codebase Archaeologist treats a codebase as a living system and analyzes its evolutionary history.

The goal is to discover hidden patterns in software development that are often invisible to developers themselves.

---

## Motivation

Most developer tools answer questions such as:

* What does this code do?
* How is the architecture organized?
* Which modules depend on each other?

Codebase Archaeologist asks different questions:

* Which files evolve together over time?
* Which modules accumulate hidden development pressure?
* How does software age?
* Which parts of a system become knowledge silos?
* Can future maintenance risks be detected from historical evolution?

The project aims to function as a scientific instrument for software evolution rather than a traditional developer productivity tool.

---

## Current Feature: Evolutionary Coupling Detection

The first implemented feature detects **evolutionary coupling**.

Two files are considered evolutionarily coupled if they repeatedly change together across the commit history of a repository.

Example:

Commit 1:

* auth.py
* user.py

Commit 2:

* payment.py
* invoice.py

Commit 3:

* auth.py
* user.py

Result:

auth.py ↔ user.py = 2 co-changes

This relationship may exist even when there is no direct import or code dependency between the files.

---

## Architecture

Repository

↓

Git Commit History

↓

Changed File Extraction

↓

Evolutionary Coupling Analysis

↓

Hidden Relationship Discovery

---

## Technologies Used

* Python
* GitPython
* Pandas
* NetworkX
* Matplotlib

---

## Project Structure

```text
codebase-archaeologist/
│
├── analyzer/
│   ├── git_reader.py
│   ├── coupling_detector.py
│   └── report.py
│
├── main.py
├── requirements.txt
└── .gitignore
```

---

## Running the Project

Clone the repository:

```bash
git clone https://github.com/Ramkrishna4816/codebase-archaeologist.git
cd codebase-archaeologist
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate:

```bash
source .venv/Scripts/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

---

## Future Research Directions

* Evolutionary Stress Zone Detection
* Architectural Drift Analysis
* Knowledge Fossilization Detection
* Mutation Pattern Mining
* Software Aging Analysis
* Hidden Evolutionary Organ Discovery
* Evolutionary Risk Prediction
* Contributor Knowledge Mapping

---

## Vision

Codebase Archaeologist is an attempt to study software repositories the way archaeologists study ancient civilizations — by reconstructing hidden evolutionary processes from historical artifacts.

The long-term goal is to discover previously unnoticed laws of software evolution.
