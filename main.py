# Returns the file's contents
def read_file(path_to_file: str) -> str:
    with open(path_to_file) as f:
        return f.read()

# Returns the number of words in a body of text
def get_word_count(contents: str) -> int:
    return len(contents.split())

# Returns a dictionary of string -> int containing the number of times
#   each character appears in the body of text
def get_character_counts(contents: str) -> dict[str, int]:
    character_counts = {}
    contents = contents.lower()

    for c in contents:
        if c.isalpha(): # only consider alphabetical characters
            if c in character_counts:
                character_counts[c] += 1
            else:
                character_counts[c] = 1

    return character_counts

def sort_on(dictionary):
    return dictionary["num"]

def sort(dictionary):
    sorted_list = []
    for entry in dictionary:
        sorted_list.append({
            "character": entry,
            "num": dictionary[entry]
        })

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def print_report(path_to_file: str) -> None:
    file_contents = None
    try:
        file_contents = read_file(path_to_file)
    except Exception as e:
        print(e)
        return

    word_count = get_word_count(file_contents)
    character_counts = get_character_counts(file_contents)
    sorted_character_counts = sort(character_counts)

    # Organize data and print
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{word_count} words found in the document")
    print()

    for i in range(0, len(sorted_character_counts)):
        c = sorted_character_counts[i]["character"]
        n = sorted_character_counts[i]["num"]
        print(f"The '{c}' character was found {n} times")

    print("--- End report ---")


def main():
    print_report("books/frankenstein.txt")

main()
