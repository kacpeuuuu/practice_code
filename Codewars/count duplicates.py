def duplicate_count(text):
    text = text.lower()
    
    letters = {}
    duplicates = 0
    for i in text:
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
            
    for i in letters:
        if letters[i]>1:
            duplicates+=1
        else:
            pass
    
    return duplicates
    