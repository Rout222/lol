import cloudinary
import cloudinary.uploader
from champs import champs
import click
cloudinary.config(
  cloud_name = 'dtw89d7fd',  
  api_key = '355121738856521',  
  api_secret = 'Bf_P-rpazllg8JhSzLAMVD3M4TQ'  
)
with click.progressbar(champs.items(), label='Progresso') as bar:
  newchamps = []
  for y in bar:
    aux = cloudinary.uploader.upload('https://ddragon.leagueoflegends.com/cdn/8.1.1/img/champion/{}.png'.format(y[1]), use_filename = True)  
    newchamps.append([y[0], y[1], aux['public_id']])

print(newchamps)