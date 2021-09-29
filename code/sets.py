pokemon_tipo_fuego = { 'Charizard', 'Moltres' }
pokemon_tipo_volador = { 'Charizard', 'Butterfree', 'Pidgeot', 'Fearow', 'Dodrio', 'Gyarados', 'Aerodactyl',
  'Articuno', 'Zapdos', 'Moltres', 'Dragonite' }
pokemon_tipo_veneno = { 'Butterfree' }
pokemon_tipo_normal = { 'Pidgeot', 'Fearow', 'Dodrio' }
pokemon_tipo_agua = { 'Gyarados' }
pokemon_tipo_roca = { 'Aerodactyl' }
pokemon_tipo_hielo = { 'Articuno' }
pokemon_tipo_electrico = { 'Zapdos' }
pokemon_tipo_dragon = { 'Dragonite' }

my_set1 = pokemon_tipo_fuego | pokemon_tipo_agua
print(f'Pokemon tipo fuego | agua: {my_set1}')

my_set2 = pokemon_tipo_normal & pokemon_tipo_volador
print(f'Pokemon tipo normal & volador: {my_set2}')

my_set3 = pokemon_tipo_volador - pokemon_tipo_fuego
print(f'Pokemon tipo volador - fuego: {my_set3}')

my_set4 = pokemon_tipo_dragon ^ pokemon_tipo_electrico
print(f'Pokemon tipo dragon ^ electrico: {my_set4}')
