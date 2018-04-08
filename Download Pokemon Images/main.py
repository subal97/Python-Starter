import urllib.request

#temp = "https://assets.pokemon.com/assets/cms2/img/pokedex/detail/003.png"

beg_pokemon = 1
last_pokemon = 807
for i in range(beg_pokemon,last_pokemon):
	try:
		path = 'images/'+'{:04d}'.format(i)+'.png'
		url = 'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/'+'{:03d}'.format(i)+'.png'
		urllib.request.urlretrieve(url, path)
		print("Saved " + '{:04d}'.format(i)+'.png')
	except Exception as e:
		print("Error occured for pokemon picture: " + '{:04d}'.format(i))
		print(str(e))
print("Finished!")
