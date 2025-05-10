import click

@click.group()
def cli():
    """LambdaForge CLI for managing Lambda function tools."""
    pass

@cli.command()
def deploy():
    """Deploy the Lambda function."""
    click.echo("Deploying Lambda function...")

if __name__ == "__main__":
    cli()