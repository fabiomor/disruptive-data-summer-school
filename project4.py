import io_data


def execute():
    words = io_data.read_words_from_csv()
    words_number = len(words)
    total_chars = 0
    for word in words:
        total_chars += len(str(word))
    words_avg_length = float(total_chars)/float(words_number)
    words.sort()
    print("Words number: " + str(words_number))
    print("Words average length: " + str(words_avg_length))
    io_data.write_to_csv(words, "project4_output.csv")