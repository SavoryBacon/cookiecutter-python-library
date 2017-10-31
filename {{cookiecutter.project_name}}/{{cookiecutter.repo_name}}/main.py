{% if cookiecutter.script == "y" -%}
import click
from {{cookiecutter.repo_name}}.scheduler.engines import blocking_scheduler
import {{cookiecutter.repo_name}}.scheduler.jobs as scheduler_jobs


@click.command()
#@click.option('--opt', type=click.Choice(['opt1', 'opt2', 'opt3']))
def main():  # Add click options above to parameters
    """
    Primary entry point for script command.
    """
    blocking_scheduler.add_job(
        scheduler_jobs.sample_job,
        kwargs={
            # kwargs to pass to job callable
        },
        id='sample_job_id',
        misfire_grace_time=60,  # allow 60 seconds to retrigger job
        coalesce=True,  # combine missed jobs with upcoming jobs
        max_instances=1,  # only ever have one instance of this job running at once
        trigger='cron',  # scheduler type
        **get_trigger_kwargs()
    )

    blocking_scheduler.start()

def get_trigger_kwargs():
    return {
        'minute': '*/1',
        'hour': '*',
        'day_of_week': '*',
        'day': '*',
        'month': '*',
    }
{%- endif %}
