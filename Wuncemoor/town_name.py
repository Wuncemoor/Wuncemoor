import numpy as np
import random


def town_name_generate():
    x = np.random.random_sample()
    syllables = -1
    weights = np.array([0.05, 0.35, 0.45, 0.10, 0.05], dtype=np.float64)
    weights = weights.cumsum()

    for i in range(len(weights)):
        if x < weights[i]:
            syllables = i + 1
            break

    first_possibilities = ['Aber', 'An', 'And', 'Ant', 'Aru', 'Ban', 'Bar', 'Bel', 'Cyp', 'Dob', 'Has', 'Mo', 'Oran',
                           'Paro', 'Sli', 'Step', 'Suk', 'Thim', 'Willem']

    second_possibilities = ['ana', 'ba', 'buda', 'dar', 'dare', 'dorra', 'eau', 'humi', 'i', 'jestad', 'mo', 'phu',
                            'rich', 'ro', 'rus', 'stad', 'ti', 'ven']

    third_possibilities = ['dos', 'kert', 'mi', 'ni', 'pan']

    fourth_possibilities = ['test']

    fifth_possibilities = ['TEST']

    first_syllable = random.choice(first_possibilities)
    second_syllable = random.choice(second_possibilities)
    third_syllable = random.choice(third_possibilities)
    fourth_syllable = random.choice(fourth_possibilities)
    fifth_syllable = random.choice(fifth_possibilities)

    town_name = first_syllable
    if syllables == 2:
        town_name = first_syllable + second_syllable
    if syllables == 3:
        town_name = first_syllable + second_syllable + third_syllable
    if syllables == 4:
        town_name = first_syllable + second_syllable + third_syllable + fourth_syllable
    if syllables == 5:
        town_name = first_syllable + second_syllable + third_syllable + fourth_syllable + fifth_syllable
    print(town_name)
