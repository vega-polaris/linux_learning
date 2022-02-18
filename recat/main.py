import typer

def main(normal_str: str, ignore_spaces: bool = False, ignore_cases: bool = False):
    reversed_str = normal_str[::-1]
    if ignore_cases:
        reversed_str = reversed_str.lower()
    if ignore_spaces:
        reversed_str = reversed_str.replace(" ", "")
    typer.echo(reversed_str)

if __name__ == "__main__":
    typer.run(main)
    