  
#count function

def get_num_words(text):
    result = text.split()
    num = len(result)
    return num

#counting the number of characters
def get_char_dict(text):
    dictionary = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
        
    return dictionary

#sorting dictionary by characters amounts
def sort_dict(dictionary):

    sorted_dict = []
    
    for key in dictionary:
        value = dictionary[key]
        sorted_dict.append({"char": key, "num": value})
        
    sorted_list = sorted(sorted_dict, key=lambda d: d["num"], reverse=True)

    return sorted_list