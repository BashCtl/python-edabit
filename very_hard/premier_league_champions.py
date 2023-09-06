def champions(teams):
    sort_func = lambda club: (club["wins"] * 3 + club["draws"], club["scored"] - club["conceded"])
    teams = sorted(teams, key=sort_func, reverse=True)
    return teams[0]["name"]


print(champions([
    {
        "name": "Manchester United",
        "wins": 30,
        "loss": 3,
        "draws": 5,
        "scored": 88,
        "conceded": 20,
    },
    {
        "name": "Arsenal",
        "wins": 24,
        "loss": 6,
        "draws": 8,
        "scored": 98,
        "conceded": 29,
    },
    {
        "name": "Chelsea",
        "wins": 22,
        "loss": 8,
        "draws": 8,
        "scored": 98,
        "conceded": 29,
    }
]))
