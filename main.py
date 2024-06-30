# generate_report() generates a report based on the word and character counts
def generate_report(word_count, char_count):
    print("Generating report...")
    
    # Convert the character count to a list of dictionaries
    char_count_list = []
    for char, count in char_count.items():
        # check if the character is alphabet(a-z)
        if char.isalpha():
            # add the character and its count as a dictionary
            char_count_list.append({"char": char, "count": count })
        print("char_count_list:", char_count_list)
        
        # Sort the list of character counts in descending order
        sorted_char_counts = sorted(char_count_list, key=lambda item:['count'], reverse=True)
        print("\nCharacter counts sorted (top 5):", sorted_char_counts[:5])
        
        # Create the report header
        report = "--Begin report of books/frankenstein.txt--\n"
        report += f"{word_count} words found in the document\n\n"
        
        # Add character count information to the report
        for item in sorted_char_counts:
            char = item["char"]
            count = item["count"]
            f"The '{char}' character was found {count} times\n"
        
        
        
        report += "-- End of report --\n"
    
    print("\nReturning report: ")
    return report
        


# count_characters() counts the number of characters in a given text
def count_characters(text):
    print("Counting characters in the text...")
    
    # keep track of character counts using dictionary
    # where key is the character and value is the count
    char_counts = {}
    print("Initialized char_counts: dictionary:", char_counts)
    
    # convert the text to lower case
    text = text.lower()
    # print first 50 characters for visually confirming
    print("\nText converted to lower case:", text[:50]) 
    
    # and iterate over each character
    print("\nIterating through characters:")
    for char in text:
        print(f" - Processing character: 'char'")
        
        
        # Counting and storing in dictionary
        if char in char_counts: # if character is already present in the dictionary
            #  increment the count
            char_counts[char] += 1
            print(f" - Incremented count of '{char}' with count: 1")
        else:
            #  add the new character to the dictionary initial count of 1
            char_counts[char] = 1
            print(f" - Added new  character '{char}' with count: 1")
            
    
    print("\nReturning character counts: ")
    print(char_counts)
    return char_counts
    

# count_words() counts the number of words in a given text
def count_words(text):
    print("Counting words in the text...")
    
    # split Text into words
    words = text.split()
    print("Words after splitting: ", words)
    
    # count the number of words
    word_count = len(words)
    print("Total word count:", word_count)
    
    return word_count 


def main():
    
    # defining the fiel path
    file_path = "books/frankenstein.txt"
    print(f"Attemping to read from file: {file_path}")
    
    # open the file in read mode
    with open(file_path, "r") as f:
        # read the file
        file_contents = f.read()
        print(file_contents)
        
    word_count = count_words(file_contents)
    print("Word count:", word_count)
    
    char_count = count_characters(file_contents)
    print("Character counts:", char_count)
    
    report  = generate_report(word_count, char_count)
    print("Report generated successfully!", report)
    
    


# standard practice to ensure the main function is executed only when the script is run directly
if __name__ == "__main__":
    main()