'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.

times = ('Flamento', 'Santos', 'Gremio', 'Athletico Paranaense', 'São Paulo',
        'Internacional', 'Corintias', 'Fortaleza', 'Goiais', 'Bahia', 'Vasco da Gama', 'Atletico',
        'Fluminense', 'Botafoto', 'Ceara', 'Cruzeiro', 'Csa', 'Chapecoense', 'Avaí')
print('-=' * 15)
print('Lista de times do Brasileirão: {}'.format(times))
print('-=' * 15)
print('Os 5 primeiros times são: {}'.format(times[0:5]))
print('-=' * 15)
print('Os 4 ultimos times colocados são: {}'.format(times[-4:]))
print('-=' * 15)
print('Os times em Ordem alfabética: {}'.format(sorted(times)))
print('-=' * 15)
print('O time da Chapecoense está na {}ª posição'.format(times.index("Chapecoense")))
print('-=' * 15)'''

times = ('Corinthians', 'Atlético-MG', 'Flamengo', 'Bragantino', 'Santos',
         'Fluminense', 'São Paulo', 'Coritiba', 'América-MG', 'Botafogo',
         'Cuiabá', 'Ceará', 'Internacional', 'Avaí', 'Palmeiras',
         'Juventude', 'Goiás', 'Atlético-GO', 'Fortaleza', 'Athletico-PR')
print('-=' * 15)
print('Lista de times do brasileirão 2022: {}'.format(times))
print('-=' * 15)
print('Os 5 primeiros times são: {}'.format(times[0:5]))
print('-=' * 15)
print('Os 4 ultimos colocados são: {}'.format(times[-4:]))
print('-=' * 15)
print('Em ordem alfabetica: {}'.format(sorted(times)))
print('-=' * 15)
print('O time do Flamengo está na {}ª posição'.format(times.index("Flamengo") + 1))
print('-=' * 15)
