def word_count(path):
    with open(path) as f:
        read_content = f.read()
    
    content_list = read_content.split()
    word_count = len(content_list)
    return word_count


def character_count(path):
    char_count = {}
    with open(path) as file:
        for line in file:
            line = line.lower()
            for char in line:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 0
    return(char_count)


def sort_character_count(path):
    result_from_count = character_count(path)   #First we Fatch the result fromthe character counting as normal
    
    def sort_on(dict):
        return dict["num"]

    #then we convert the dictionary into multiple dictionaries 
    multiple_dicts = [{"char" : key, "num": value} for key, value in result_from_count.items() if key.isalpha()]

    # now we sort the dictionary by num
    multiple_dicts.sort(reverse=True, key=sort_on)

    return multiple_dicts


def book_report(path):
    # We will first fetch all the needed results
    counted_words = word_count(path)
    sorted_characters = sort_character_count(path)

    # then we print out the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {counted_words} total words")
    print("--------- Character Count -------")
    for character in sorted_characters:
        print(f"{character["char"]}: {character["num"]+1}")
    print("============= END ===============")
    return ""

    
