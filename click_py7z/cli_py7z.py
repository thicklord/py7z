import click
from cmprssn.ext_all import *
from cmprssn.pprss import *



@click.command()
@click.argument("ppath", type=click.Path)
@click.option("--level", "-l", type=int, default=0)
@click.option("--depth", "-d", type=click.Choice(["R", "S", "P"]), default="P")
@click.option("--remove", "-r", is_flag=True)
def compressor(ppath, level, depth):
    
    squeezer(ppath, level, depth)


@click.command()
@click.argument("ppath", type=click.Path)
@click.option("--remove", "-r", is_flag=True, help='Triggers removal of archives after successful decompression')
@click.option("--include-extension", "-ie", "extensions", multiple=True)
def extractor(epath, extensions):
    
    extensions = list(extensions)

    master_blaster(epath, extensions)
    
    
    
    pass







