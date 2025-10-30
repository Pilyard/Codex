import random

#     fortune_phrases = ['Dont pursue happiness - create it.', 'All things are difficult before they are easy.', 'The early bird gets the worm, but the second mouse gets the cheese.',
#                        'Someone in your life needs a letter from you.', 'Dont just think. Act!', 'Your heart will skip a beat.', 'The fortune you search for is in another cookie.', 'Help! im´being held prisoner in a Chinese bakery!']
# def fortune():
#     print(random.choice(fortune_phrases))
# fortune()
# fortune()
# fortune()

fortune_phrases = ['Dont pursue happiness - create it.', 'All things are difficult before they are easy.', 'The early bird gets the worm, but the second mouse gets the cheese.',
                   'Someone in your life needs a letter from you.', 'Dont just think. Act!', 'Your heart will skip a beat.', 'The fortune you search for is in another cookie.', 'Help! im´being held prisoner in a Chinese bakery!']


def fortune():
    random_phrases = random.randint(0, len(fortune_phrases) - 1)
    print(fortune_phrases[random_phrases])


fortune()
fortune()
fortune()
