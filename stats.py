def get_book_text(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occured: {e}")
    return None

def count_words(text):
    return len(text.split())

def count_characters(text: str) -> dict:
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(char_dict):
    return char_dict["num"]

def sort_character_counts(char_count: dict) -> list:
    char_list = [
        {"char": ch, "num": count}
        for ch, count in char_count.items()
        if ch.isalpha()
    ]
    char_list.sort(reverse=True, key=sort_on)

    return char_list
