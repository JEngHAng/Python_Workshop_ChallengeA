def analyze_sentence(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Count the total number of words
    total_words = len(words)

    # Create a set to find unique words
    unique_words = set(words)

    # Count the occurrences of each unique word
    word_count = {word: words.count(word) for word in unique_words}

    # Find words that occur more than once
    repeated_words = {word: count for word, count in word_count.items() if count > 1}

    # Display the results
    print(f"มีคำรวมทั้งหมด {total_words} คำ")
    print(f"มีคำที่ซ้ำกันรวม {len(repeated_words)} คำคือ {', '.join(repeated_words)}")

    for word, count in repeated_words.items():
        print(f"คำว่า {word} ซ้ำกัน {count} ครั้ง")


# Get user input
user_sentence = input("ป้อนข้อความ: ")

# Analyze the sentence
analyze_sentence(user_sentence)