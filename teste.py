import click
with click.progressbar([1,2,3,4,5,6].items(), label='Calculando dados brutos') as bar:
	print(bar)