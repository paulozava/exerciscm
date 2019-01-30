def tally(tournament_results):
    table_elements = [('Team', 'MP', 'W', 'D', 'L', 'P')]
    if tournament_results != '':
        teams = {}
        for play in tournament_results.split('\n'):
            home, away, result = tuple(play.split(';'))
            check_team_existence(away, home, teams)
            account_result(away, home, result, teams)

        table_elements.extend(sorted(sorted([tuple(map(str, team.values())) for team in teams.values()]),
                                    key=lambda x: x[-1], reverse=True))
    table_template = '{:<30} | {:>2} | {:>2} | {:>2} | {:>2} | {:>2}'
    rows = [table_template.format(*element) for element in table_elements]
    table = ('\n'.join(rows))
    return table


def account_result(away, home, result, teams):
    if result == 'loss':
        home, away = away, home
    if result == 'draw':
        teams[home]['D'] += 1
        teams[home]['P'] += 1
        teams[away]['D'] += 1
        teams[away]['P'] += 1
    else:
        teams[home]['W'] += 1
        teams[home]['P'] += 3
        teams[away]['L'] += 1
    teams[home]['MP'] += 1
    teams[away]['MP'] += 1


def check_team_existence(away, home, teams):
    if home not in teams:
        teams[home] = {'Name': home, 'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0}
    if away not in teams:
        teams[away] = {'Name': away, 'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0}
