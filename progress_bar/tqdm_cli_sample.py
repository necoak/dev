from tqdm import tqdm
import click
from time import sleep
from math import ceil

@click.command()
@click.argument('count', type=click.INT)
@click.argument('add', type=click.INT)
@click.argument('sleeptime', type=click.INT)
def cmd(count, add, sleeptime):
    """プログレスバーサンプル（count数をsleeptime秒ずつadd分ずつ加算していく）"""
    click.echo('count: %s add: %s sleeptime:%s'%(count, add, sleeptime))
    pbar = tqdm(total=count)
    for i in range(ceil(count / add)):
        sleep(sleeptime)
        if add*(i+1) <= count:
            pbar.update(add)
        else:
            pbar.update(count % add)
        
if __name__ == '__main__':
    cmd()
