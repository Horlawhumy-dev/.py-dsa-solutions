

def ransome_note(magazine, note):
    """
        This checks whether all note words are present in magazine."
        @params: magazine contains all words, note has all words to check for
        @return: True or False
    """
    
    mag_list = magazine.split(" ")
    note_list = note.split(" ")
    mag_dict = {mag_word: "stored" for mag_word in mag_list}
    for note_word in note_list:
        if note_word not in mag_dict:
            return False
    return True
    
print(ransome_note("The man was captured by bandit", "The man was captured yesterday"))
