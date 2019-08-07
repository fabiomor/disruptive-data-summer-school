import io_data
import re

DELIMITERS = "-", "/"
REGEX_PATTERN = '|'.join(map(re.escape, DELIMITERS))
WORD_LENGTH_FILTER = 2

def execute():
    l1, l2 = io_data.read_uris_from_csv()
    matching_map_total = []
    for i in range(0,len(l1)):
        matching_current_keywords = []
        for j in range(0, len(l2)):
            matching_count = find_uris_matching(l1[i], l2[j])
            #print("matching " + l1[i] + " with " + l2[j] + "  matching count = " + str(matching_count))
            matching_current_keywords.append(matching_count)
        max_occurrences = max(matching_current_keywords)
        if max_occurrences > 0:
            matching_map_total.append([l1[i], l2[matching_current_keywords.index(max_occurrences)]])
        else:
            matching_map_total.append([l1[i], 'ND'])
    io_data.write_to_csv(matching_map_total, "project2_output.csv")

def find_uris_matching(string1, string2):
    keywords1 = list(filter(None, re.split(REGEX_PATTERN, string1)))
    keywords2 = list(filter(None, re.split(REGEX_PATTERN, string2)))
    counter = 0
    for i in range(0, len(keywords1)):
        for j in range(0,len(keywords2)):
            # simple matching criteria: every keyword of the first list is compared with all keywords contained in
            # second keyword, checking if it's partially or fully contained in another keyword. A filter on length word
            # is used in order to avoid matching with connective words
            if (len(keywords1[i]) > WORD_LENGTH_FILTER and keywords1[i] in keywords2[j]) \
                    or (len(keywords2[j]) > WORD_LENGTH_FILTER and keywords2[j] in keywords1[i]):
                counter += 1
    return counter

