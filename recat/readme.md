# Recat
This tiny CLI tool reverses a python string.

# How to run
First, install [typer](https://typer.tiangolo.com/) via `pip install -r requirements.txt` or `pip install typer`.
From this directory, run `python main.py <string to reverse> <flags>`

# What are the flags?
This little program can be told to ignore spaces:
```
❯ python main.py "hello world"
dlrow olleh

❯ python main.py "hello world" --ignore-spaces
dlrowolleh
```

...or ignore cases:
```
❯ python main.py "HelLo WorLD"
DLroW oLleH

❯ python main.py "HelLo WorLD" --ignore-cases
dlrow olleh

```
...or, of course, both:
```
❯ python main.py "HelLo WorLD" --ignore-cases --ignore-spaces
dlrowolleh
```
