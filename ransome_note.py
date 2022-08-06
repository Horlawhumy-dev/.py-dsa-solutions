

def ransome_note(magazine, note):
    """
        This checks whether all note words are present in magazine."
        @params: magazine contains all words, note has all words to check for
        @return: True or False
    """
    mag_dict = {}
        
        for i in range(len(magazine)):
            if magazine[i] in mag_dict:
                mag_dict[magazine[i]] += 1 
            else:
                mag_dict[magazine[i]] = 1

        for i in range(len(ransomNote)):
            if mag_dict.get(ransomNote[i], 0) < 1:
                return False
            else:
                mag_dict[ransomNote[i]] -= 1
            
        return True
    
print(ransome_note("The man was captured by bandit", "The man was captured yesterday"))
