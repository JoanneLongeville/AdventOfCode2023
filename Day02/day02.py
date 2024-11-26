# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# Games 1, 2 and 5 are possible, so answer's 8


# Compare each game to the bag
# If colors and numbers match, add to possible games
# Sum the number of possible games

bag = {'red': 12, 'green': 13, 'blue': 14}


def import_yml(file):
    with open(file, 'r') as file:
        input = file.readlines()  # yaml.safe_load(file)
    return [line.strip() for line in input]


def part01_test():
    games = import_yml('input_test.yml')
    games_split = {}
    for game in games:
        if ':' in game:
            game_id, contents = game.split(":", 1)
            games_split[game_id.strip()] = [part.strip() for part in contents.split(";")]
    return games_split


print("part01_test", part01_test())