import numpy as np


def how_many_words_starts_with_A(words: np.array) -> int:
    count = 0
    for word in words:
        if word[0].lower() == "a":
            count += 1

    return count



words = np.array(["Rei Ayanami", "Asuka Langley Soryu", "Shinji Ikari", "Misato Katsuragi", "Ritsuko Akagi", "Gendo Ikari", "Kaworu Nagisa", "Toji Suzuhara", "Kensuke Aida", "Hikari Horaki"])

print(f"There are {how_many_words_starts_with_A(words)} words that start with the letter 'A'")
