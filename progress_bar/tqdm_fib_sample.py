from tqdm import tqdm
import click

pbar = None

@click.command()
@click.argument('num', type=click.INT)
def cmd(num):
    """Calc Fibonacci Number with ProgressBar."""
    # set up progress bar
    global pbar
    pbar = tqdm(total=num)
    # calc fibonacci
    fibnum = fib(num)
    # close & finish
    pbar.close()
    click.echo('Finish')

def fib(n):
    global pbar
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
        pbar.update(1)   
    return b

if __name__ == '__main__':
    cmd()
