def analyze_sentence(sentence):
    words = sentence.split()
    total_words = len(words)
    unique_words = set(words)
    word_count = {word: words.count(word) for word in unique_words}
    repeated_words = {word: count for word, count in word_count.items() if count > 1}
    print(f"มีคำรวมทั้งหมด {total_words} คำ")
    print(f"มีคำที่ซ้ำกันรวม {len(repeated_words)} คำคือ {', '.join(repeated_words)}")

    for word, count in repeated_words.items():
        print(f"คำว่า {word} ซ้ำกัน {count} ครั้ง")

user_sentence = input("ป้อนข้อความ: ")
analyze_sentence(user_sentence)