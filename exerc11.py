import numpy as np 

def get_words_with_three_more_letters(words: np.ndarray) -> np.ndarray:
    return np.array([word for word in words if len(word) >= 3])





words = np.array(["Rei Ayanami", "Asuka Langley Soryu", "Shinji Ikari", "Misato Katsuragi", "Ritsuko Akagi", "Gendo Ikari", "Kaworu Nagisa", "Toji Suzuhara", "Kensuke Aida", "Hikari Horaki"])
filtered_words = get_words_with_three_more_letters(words)
print(filtered_words)
