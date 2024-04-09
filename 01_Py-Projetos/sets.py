#Set 

planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumeia', 'Makemake'}
print(planeta_anao)
print(len(planeta_anao))

for astro in planeta_anao:
    print(astro.upper())

astros = ['Lua', 'Venus', 'Sirius', 'Marte', 'Lua']
print(astros, end=' ')
astro_set = set(astros)
print(astro_set) 