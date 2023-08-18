def duplicate_count(text):
    text = text.lower()
    
    letters = {}
    duplicates = 0
    for i in text:
        if i in letters:
            letters[i] += 1
            if letters[i] == 2:
                duplicates += 1
        else:
            letters[i] = 1
            
    return duplicates
    