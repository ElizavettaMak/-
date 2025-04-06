list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
n_players = len(list_players) # Общее количество игроков
one_team = list_players[:n_players//2]
two_team = list_players[n_players//2:]
print(one_team)
print(two_team)