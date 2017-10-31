{% if cookiecutter.script == "y" -%}
import click
import schedule
{%- endif %}

{% if cookiecutter.script == "y" -%}
@click.command()
#@click.option('--opt', type=click.Choice(['opt1', 'opt2', 'opt3']))
def main():  # Add click options above to parameters
    """
    Primary entry point for script command.
    """
    print("It works!")
    return
{%- endif %}
