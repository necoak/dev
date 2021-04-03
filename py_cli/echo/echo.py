#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click

@click.command()
def cmd():
    intext = input()
    click.echo(intext)


if __name__ == '__main__':
    cmd()
