import os
def count_word_frequency(file_path):
    """Count the frequency of words in a file."""
    word_frequency = {}

    with open("a.txt", 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                if word in word_frequency:
                    word_frequency[word] += 1
                else:
                    word_frequency[word] = 1

    return word_frequency

# Example usage
frequency = count_word_frequency("a.txt")

# Print the word frequencies
for word, count in frequency.items():
    print(f'{word}: {count}')
print(os.path.getsize("a.txt"))           # to print the file size
