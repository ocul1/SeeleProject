# WriterDeck

A terminal journaling tool. Write an entry, hit `END` on a new line, and it's saved with your name, a title, and a timestamp.

## What it does

WriterDeck is a small CLI for quick journal entries. Each entry gets an author, a title, a date, and a time, and is appended to a single running log file so your whole history lives in one place.

Named after the SEELE monoliths from *Neon Genesis Evangelion* — a small nod, nothing more sinister than that.

## Requirements

- A computer capable of running Python 3
- No external dependencies — everything used is part of the Python standard library

## Usage

Run the program with `python writerdeckProgram.py`. You'll be walked through: 1. Your name, 2. An entry title, 3. The entry itself — type freely across as many lines as you want, then type `END` on its own line to finish. The entry is saved to `writerDeck/writerdeck.txt`, with the author, title, date, and time recorded above the text. The program then asks if you'd like to write another entry before exiting.

## Notes

- The `writerDeck/` directory is created automatically on first run if it doesn't already exist.
- All entries live in one text file, appended in order, so the log doubles as a simple running journal you can read straight through.

## Possible next steps

- Store entries as JSON instead of a flat text file, so individual entries can be queried, edited, or exported
- A `list` or `search` command to pull up past entries by title or date
- Multi-user support beyond a free-text name field
