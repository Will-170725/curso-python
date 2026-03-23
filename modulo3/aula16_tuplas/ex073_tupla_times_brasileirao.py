# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.

tabela2018 = ('Corinthians','Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético-MG', 'Botafogo', 'Athletico-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO',)
tabela2026 = ('Athletico-PR', 'Atlético-MG', 'Bahia', 'Botafogo', 'Bragantino', 'Chapecoense', 'Corinthians', 'Coritiba', 'Cruzeiro', 'Flamengo', 'Fluminense', 'Grêmio', 'Internacional', 'Mirassol', 'Palmeiras', 'Remo', 'Santos', 'São Paulo', 'Vasco', 'Vitória')

print(f'Lista de times do Brasileirão 2018: {tabela2018}')
print(f'Os cinco primeiros colocados do Campeonato Brasileiro de Futebol de 2018 são {tabela2018[0:5]}')
print(f'Os últimos quatro colocados da tabela 2018 são: {tabela2018[-4:]}')
print(f'Lista de times em ordem alfabética: {sorted(tabela2018)}')
print(f'A Chapecoense se encontra na posição {tabela2018.index('Chapecoense') + 1} da tabela.')

print(f'Lista de times do campeonato Brasileiro de Futebold 2026: {tabela2026}')
print(f'Os cinco primeiros são: {tabela2026[0:5]}')
print(f'Os últimos quatro são: {tabela2026[-4:]}')
print(f'Times em ordem alfabética: {sorted(tabela2026)}')
print(f'O Chapécoense está na {tabela2026.index('Chapecoense') + 1}ª posição')

# Resolução do professor

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')
print('-=' * 15)
print(f'Lista de times: {times}')
print('-=' * 15)
for t in times:
    print(t)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição')
