import random

data = [
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 620,
        "description": "Footballer",
        "country": "Portugal",
    },
    {
        "name": "Lionel Messi",
        "follower_count": 500,
        "description": "Footballer",
        "country": "Argentina",
    },
    {
        "name": "Selena Gomez",
        "follower_count": 430,
        "description": "Singer and actress",
        "country": "USA",
    },
    {
        "name": "Kylie Jenner",
        "follower_count": 400,
        "description": "Media personality",
        "country": "USA",
    },
    {
        "name": "Dwayne Johnson",
        "follower_count": 390,
        "description": "Actor and wrestler",
        "country": "USA",
    },
    {
        "name": "Ariana Grande",
        "follower_count": 380,
        "description": "Singer",
        "country": "USA",
    },
    {
        "name": "Kim Kardashian",
        "follower_count": 360,
        "description": "Media personality",
        "country": "USA",
    },
    {
        "name": "Beyoncé",
        "follower_count": 320,
        "description": "Singer",
        "country": "USA",
    },
    {
        "name": "Khloé Kardashian",
        "follower_count": 310,
        "description": "Media personality",
        "country": "USA",
    },
    {
        "name": "Justin Bieber",
        "follower_count": 290,
        "description": "Singer",
        "country": "Canada",
    },
    {
        "name": "Taylor Swift",
        "follower_count": 280,
        "description": "Singer-songwriter",
        "country": "USA",
    },
    {
        "name": "Virat Kohli",
        "follower_count": 270,
        "description": "Cricketer",
        "country": "India",
    },
    {
        "name": "Jennifer Lopez",
        "follower_count": 250,
        "description": "Singer and actress",
        "country": "USA",
    },
    {
        "name": "Neymar",
        "follower_count": 240,
        "description": "Footballer",
        "country": "Brazil",
    },
    {
        "name": "Nicki Minaj",
        "follower_count": 230,
        "description": "Rapper",
        "country": "USA",
    },
    {
        "name": "Miley Cyrus",
        "follower_count": 210,
        "description": "Singer",
        "country": "USA",
    },
    {
        "name": "Kendall Jenner",
        "follower_count": 200,
        "description": "Model",
        "country": "USA",
    },
    {
        "name": "Shakira",
        "follower_count": 190,
        "description": "Singer",
        "country": "Colombia",
    },
    {
        "name": "LeBron James",
        "follower_count": 160,
        "description": "Basketball player",
        "country": "USA",
    },
    {
        "name": "Billie Eilish",
        "follower_count": 150,
        "description": "Singer",
        "country": "USA",
    },
]

game_over = False
score = 0


def format_text(celeb):
    name = celeb["name"]
    desc = celeb["description"]
    country = celeb["country"]

    return f"{name}, a {desc}, from {country}"


def is_answer_correct(input, option_a, option_b):
    if option_a > option_b:
        return input == "a"
    else:
        return input == "b"


a = random.choice(data)
while not game_over:
    b = random.choice(data)

    if a == b:
        b = random.choice(data)

    print(f"Compare A: {format_text(a)}")
    print("VS")
    print(f"Against B: {format_text(b)}")

    user_input = input("\nWho has more followers? Type A or B: ").lower()
    print(f"\nscore: {score}")

    is_correct = is_answer_correct(user_input, a["follower_count"], b["follower_count"])

    if is_correct:
        score += 1
        a = b

    else:
        print(f"Incorrect answer, Your total score is {score}")
        game_over = True
