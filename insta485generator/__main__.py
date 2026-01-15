"""Build static HTML site from directory of HTML templates and plain files."""
import click as click
import pathlib
import json
import jinja2
import shutil


@click.command()
@click.argument("input_dir", nargs=1, type=click.Path(exists=True))
def main(input_dir):
    input_dir = pathlib.Path(input_dir)
    print(f"DEBUG input_dir={input_dir}")

    config_filename = pathlib.Path(input_dir / "config.json")
    with config_filename.open() as config_file:
        #returns data as python list
        config_list = json.load(config_file)
    

    template_dir = input_dir / "templates"
    
    template_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(str(template_dir)),
        autoescape=jinja2.select_autoescape(['html', 'xml']),
    )

    

    template = template_env.get_template("index.html")

    #rendering with context
    rendered = template.render(config_list[0]['context'])

    #render template to output file
    url = config_list[0]['url']
    url = url.lstrip("/")  # remove leading slash
    output_dir = pathlib.Path("generated_html")  # convert str to Path object, when --output is provided
    output_path = output_dir/url/"index.html"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered)


    static_path = pathlib.Path(input_dir / "static")

    if(static_path.exists()):
        shutil.copytree(static_path, output_dir,dirs_exist_ok=True)




if __name__ == "__main__":
    main()
