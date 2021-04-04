#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import re

@click.command()
def cmd():
    stdin_stream = click.get_text_stream('stdin')
    stdin_text = stdin_stream.readline()
    while stdin_text:
        click.echo(stdin_text[0:-1])
        stdin_text = stdin_stream.readline()

if __name__ == '__main__':
    cmd()
