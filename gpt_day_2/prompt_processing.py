import json
def tokenizer(content):
    cw = ["the", "and", "of", "to", "in", "is", "you", "that", "it", "he", "she", "we", "they", "I", "am", "for", "was", "on", "with", "as", "by", "at", "but", "not", "from", "or", "an", "if", "this", "all", "have", "one", "can", "will", "would", "about", "there", "out", "up", "so", "what", "when", "how", "which", "who", "get", "go", "me", "him", "her", "his", "its", "our", "your", "their", "my", "no", "do", "are", "were", "been", "into", "more", "time", "can't", "should", "could", "did", "has", "had", "may", "might", "must", "shall", "should", "us", "them", "before", "after", "over", "under", "between", "through", "because", "why", "now", "then", "still", "just", "too", "down", "also", "well", "here", "back", "only", "even", "very", "good", "first", "new", "way", "want", "give", "day", "most", "work", "make", "know", "see", "come", "take", "need", "use", "feel", "try", "call", "should", "turn", "long", "great", "little", "own", "right", "place", "house", "man", "old", "year", "last", "people", "part", "tell", "point", "case", "week", "company", "number", "fact", "question", "point", "group", "fact", "question", "point", "group", "world", "different", "example", "hand", "small", "large", "place", "turn", "right", "big", "high", "start", "same", "part", "good", "line", "seem", "hand", "keep", "house", "place", "line", "name", "night", "run", "move", "live", "year", "place", "try", "home", "life", "case", "side", "name", "world", "end", "keep", "look", "use", "own", "same", "home", "work", "look", "part", "place", "try", "case", "hand", "place", "line", "move", "name", "part", "point", "right", "same", "work", "end", "feel", "keep", "live", "look", "make", "own", "place", "try", "use", "world", "year", "people", "find", "house", "line", "name", "place", "work", "live", "people", "right", "case", "home", "end", "life", "look", "name", "part", "people", "right", "world", "back", "end", "hand", "home", "name", "people", "work", "life", "look", "place", "end", "home", "life", "line", "people", "place", "work", "point", "right", "side", "use", "work", "day", "end", "home", "house", "life", "part", "point", "week", "work", "hand", "life", "place", "part", "try", "week", "year", "end", "hand", "life", "line", "part", "place", "point", "side", "week", "work", "year", "back", "end", "house", "line", "look", "place", "world", "year", "life", "part", "people", "place", "right", "year", "line", "point", "work", "place", "work", "house", "line", "look", "make", "place", "try", "work", "life", "look", "place", "point", "week", "work", "day", "hand", "line", "look", "place", "year", "work", "people", "line", "work", "year", "end", "life", "name", "place", "world", "work", "life", "name", "place", "year", "people", "world", "year", "line", "point", "right", "work", "year", "end", "life", "place", "people", "week", "hand", "home", "life", "look", "part", "week", "year", "back", "end", "home", "house", "line", "place", "world", "year", "life", "part", "people", "place", "right", "year", "line", "point", "work", "place", "work", "house", "line", "look", "make", "place", "try", "work", "life", "look", "place", "point", "week", "work", "day", "hand", "line", "look", "place", "year", "work", "people", "line", "work", "year", "end", "life", "name", "place", "world", "work", "life", "name", "place", "year", "people", "world", "year", "line", "point", "right", "work", "year", "end", "life", "place", "people", "week", "hand", "home", "life", "look", "part", "week", "year", "back", "end", "home", "house", "line", "place", "world", "year", "life", "part", "people", "place", "right", "year", "line", "point", "work", "place", "work", "house", "line", "look", "make", "place", "try", "work", "life", "look", "place", "point", "week", "work", "day", "hand", "line", "look", "place", "year", "work", "people", "line", "work", "year", "end", "life", "name", "place", "world", "work", "life", "name", "place", "year", "people", "world", "year", "line"]
    intents = {
        "what": ["what", "explain", "describe", "list", "define", "tell me about", "provide information on", "clarify"],
        "where": ["where", "locate", "place", "application", "find", "identify", "discover", "destination"],
        "who": ["who", "person", "individual", "identity", "character", "name", "figure"],
        "when": ["when", "period", "timing", "time", "duration", "date", "moment", "schedule", "timeline"],
        "how": ["how", "method", "way", "process", "procedure", "technique", "approach"],
        "why": ["why", "reason", "purpose", "cause", "motivation", "explanation", "justification"]
    }
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
            notin = False
            for intent in intents:
                notin = False
                if token not in intents[intent]:
                    notin = True
                else:
                    notin = False
                    break
            if notin == True:
                n_tokens.append(token)
    intnt = ["stmt"]
    for token in tokens:
        for intent in intents:
            if token in intents[intent]:
                intnt.append(intent)
    if len(intnt) != 1:
        intnt.remove("stmt")
    result = {
        "number_of_tokens": len(tokens),
        "number_of_keywords": len(n_tokens),
        "keywords": n_tokens,
        "intent": intnt
    }
    json_result = json.dumps(result, indent=4)  # You can adjust the indent for formatting
    return json_result