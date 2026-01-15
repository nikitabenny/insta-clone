"""Build static HTML site from directory of HTML templates and plain files."""
import click as click
import pathlib
import json
import jinja2


def read():
    config_filename = pathlib.Path("../insta485/config.json")
    with config_filename.open() as config_file:
        config_list = json.load(config_file)

    print(config_list)

    

def main():
    """Top level command line interface."""
    print("Hello world!")

    @click.command()
    @click.argument("input_dir", nargs=1, type=click.Path(exists=True))
    def main(input_dir):
        input_dir = pathlib.Path(input_dir)
        print(f"DEBUG input_dir={input_dir}")

    read()




if __name__ == "__main__":
    main()
