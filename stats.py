def count_words(text):
    words = text.split()
    count = len(words)
    return count

def char_count(text):
    text = text.lower()
    unique_char = set(text)
    dict = {}
    for char in unique_char:
        count = text.count(char)
        dict.update({char:count})
    
    return dict

def sort_dict(dict):
    dict_sorted = sorted(dict.items(), key=lambda kv: kv[1], reverse=True)
    return dict_sorted