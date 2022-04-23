"""Cli interface for PriceDataCollector"""
import click

from fiole.resources.WebServer import WebServer

server = WebServer()

@click.group()
def main():
    """Fiole Server"""
    
    
@main.command()
def start():
    server.run()
    
if __name__ == "__main__":
    main()