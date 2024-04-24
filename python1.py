import nltk
from nltk.corpus import stopwords
from collections import Counter

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Function to read file contents
name="main"
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Function to remove stopwords
def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    words = nltk.word_tokenize(text)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return filtered_words

# Function to count word frequency
def count_word_frequency(words):
    word_counts = Counter(words)
    return word_counts

# Main function
def main():
    # Read file contents
    filename = "paragraphs.txt"
    text = read_file(filename)

    # Remove stopwords
    filtered_words = remove_stopwords(text)

    # Count word frequency
    word_counts = count_word_frequency(filtered_words)

    # Display word frequency count
    print("Word Frequency Count:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")
    

if name=="main":
    main()