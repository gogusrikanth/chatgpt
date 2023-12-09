from prompt_processing import tokenizer
import json
import numpy as np
from collections import Counter
def read_file(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                print(tokenizer(line))
def tokenizer(content):
    cw = ["i","the", "and", "of", "to", "in", "is", "you", "that", "it", "he", "she", "we", "they", "I", "am", "for", "was", "on", "with", "as", "by", "at", "but", "not", "from", "or", "an", "if", "this", "all", "have", "one", "can", "will", "would", "about", "there", "out", "up", "so", "what", "when", "how", "which", "who", "get", "go", "me", "him", "her", "his", "its", "our", "your", "their", "my", "no", "do", "are", "were", "been", "into", "more", "time", "can't", "should", "could", "did", "has", "had", "may", "might", "must", "shall", "should", "us", "them", "before", "after", "over", "under", "between", "through", "because", "why", "now", "then", "still", "just", "too", "down", "also", "well", "here", "back", "only", "even", "very", "good", "first", "new", "way", "want", "give", "day", "most", "work", "make", "know", "see", "come", "take", "need", "use", "feel", "try", "call", "should", "turn", "long", "great", "little", "own", "right", "place", "house", "man", "old", "year", "last", "people", "part", "tell", "point", "case", "week", "company", "number", "fact", "question", "point", "group", "fact", "question", "point", "group", "world", "different", "example", "hand", "small", "large", "place", "turn", "right", "big", "high", "start", "same", "part", "good", "line", "seem", "hand", "keep", "house", "place", "line", "name", "night", "run", "move", "live", "year", "place", "try", "home", "life", "case", "side", "name", "world", "end", "keep", "look", "use", "own", "same", "home", "work", "look", "part", "place", "try", "case", "hand", "place", "line", "move", "name", "part", "point", "right", "same", "work", "end", "feel", "keep", "live", "look", "make", "own", "place", "try", "use", "world", "year", "people", "find", "house", "line", "name", "place", "work", "live", "people", "right", "case", "home", "end", "life", "look", "name", "part", "people", "right", "world", "back", "end", "hand", "home", "name", "people", "work", "life", "look", "place", "end", "home", "life", "line", "people", "place", "work", "point", "right", "side", "use", "work", "day", "end", "home", "house", "life", "part", "point", "week", "work", "hand", "life", "place", "part", "try", "week", "year", "end", "hand", "life", "line", "part", "place", "point", "side", "week", "work", "year", "back", "end", "house", "line", "look", "place", "world", "year", "life", "part", "people", "place", "right", "year", "line", "point", "work", "place", "work", "house", "line", "look", "make", "place", "try", "work", "life", "look", "place", "point", "week", "work", "day", "hand", "line", "look", "place", "year", "work", "people", "line", "work", "year", "end", "life", "name", "place", "world", "work", "life", "name", "place", "year", "people", "world", "year", "line", "point", "right", "work", "year", "end", "life", "place", "people", "week", "hand", "home", "life", "look", "part", "week", "year", "back", "end", "home", "house", "line", "place", "world", "year", "life", "part", "people", "place", "right", "year", "line", "point", "work", "place", "work", "house", "line", "look", "make", "place", "try", "work", "life", "look", "place", "point", "week", "work", "day", "hand", "line", "look", "place", "year", "work", "people", "line", "work", "year", "end", "life", "name", "place", "world", "work", "life", "name", "place", "year", "people", "world", "year", "line", "point", "right", "work", "year", "end", "life", "place", "people", "week", "hand", "home", "life", "look", "part", "week", "year", "back", "end", "home", "house", "line", "place", "world", "year", "life", "part", "people", "place", "right", "year", "line", "point", "work", "place", "work", "house", "line", "look", "make", "place", "try", "work", "life", "look", "place", "point", "week", "work", "day", "hand", "line", "look", "place", "year", "work", "people", "line", "work", "year", "end", "life", "name", "place", "world", "work", "life", "name", "place", "year", "people", "world", "year", "line"]
    content = content.lower()
    content = content.replace(","," ")
    content = content.replace("."," ")
    content = content.replace("!"," ")
    content = content.replace("?"," ")
    tokens = content.split(" ")
    tokens = set(tokens)
    if '' in tokens:
        tokens.remove('')
    n_tokens = []
    for token in tokens:
        if token not in cw:
            n_tokens.append(token)
    return n_tokens

# Function to compute the cosine similarity between two vectors
def cosine_similarity(vec1, vec2):
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    similarity = dot_product / (norm_vec1 * norm_vec2)
    return similarity

# Function to preprocess and tokenize a sentence
def tokenize(sentence):
    return sentence.lower().split()

def classify(user_input):
    # Sample list of sentences
    sentences = [
        ["I like programming","stmt"],
        ["Python is great for programming","what"],
        ["Machine learning is interesting","stmt"],
        ["I met an old lady at the gym, she is so strong for her age","where"]]

    # Tokenize and count word frequencies
    word_counts = Counter()
    for sentence in sentences:
        words = tokenize(sentence[0])
        word_counts.update(words)

    # Create a unique vocabulary
    vocab = list(word_counts.keys())

    # Create word vectors based on word frequency (using one-hot encoding)
    word_vectors = {}
    for i, word in enumerate(vocab):
        vector = np.zeros(len(vocab))
        vector[i] = 1.0  # Set the corresponding index to 1
        word_vectors[word] = vector

    # Tokenize the user input
    user_words = tokenize(user_input)

    # Calculate the user input vector
    user_vector = np.zeros(len(vocab))
    for word in user_words:
        if word in vocab:
            user_vector[vocab.index(word)] = 1.0

    # Calculate the similarity between user input and each sentence in the list
    similarities = []

    for sentence in sentences:
        sentence_vector = np.zeros(len(vocab))
        words = tokenize(sentence[0])
        for word in words:
            if word in vocab:
                sentence_vector[vocab.index(word)] = 1.0
        similarity = cosine_similarity(user_vector, sentence_vector)
        similarities.append(similarity)

    # Find the most similar sentence
    most_similar_index = np.argmax(similarities)
    most_similar_sentence = sentences[most_similar_index]
    return most_similar_sentence,most_similar_index,similarities
def extract(keywords):
    cities = ["hyderabad","mumbai","delhi","nellore"]
    countries = ["bharat","uk","us","brazil","russia"]
    names = ["pavan","engineer","software","movie"]
    k_types = {
        "what":[names],
        "where":["here","there","where","place","city","hometown",cities,countries],
        "when":["today","tomorrow","tonight","am","pm"]
    }
    print(keywords)
    kwds = []
    for kw in keywords:
        for k_type in k_types:
            for k in k_types[k_type]:
                if not isinstance(k, list):
                    if kw in k:
                        kwds.append([kw,k_type])
                else:
                    for j in k:
                        if kw in j:
                            kwds.append([kw,k_type])
    return kwds
# user_input = input("Enter a sentence: ")
# most_similar_sentence,most_similar_index,similarities = classify(user_input)
# print("User input:", user_input)
# print("Most similar sentence:", most_similar_sentence[0])
# print("Intent:", most_similar_sentence[1])
# print("Cosine Similarity:", similarities[most_similar_index])
# extract(set(tokenizer("This is Pavan, I am basically from nellore, but currently in Hyderabad. I will be going back to my hometown tomorrow.")))
# read_file('data.txt')
# I found a dog at the hallway, he is so cute