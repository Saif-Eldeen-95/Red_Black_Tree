from RBTree import RBTree

DICT_FILE = "Dictionary.txt"


def load_dictionary(tree):
    print("Loading dictionary... (this may take a moment)")
    try:
        with open(DICT_FILE, "r") as f:
            for line in f:
                word = line.strip().lower()
                if word:
                    tree.insert(word)
        print(f"Done! {tree.get_size()} words loaded.\n")
    except FileNotFoundError:
        print(f"ERROR: '{DICT_FILE}' not found. Starting with an empty dictionary.\n")


def insert_word(tree, word):
    word = word.strip().lower()

    if tree.search(word):
        print("ERROR: Word already in the dictionary!")
    else:
        tree.insert(word)
        with open(DICT_FILE, "a") as f:
            f.write(word + "\n")
        print(f"'{word}' inserted successfully.")

    print(f"  Size         : {tree.get_size()}")
    print(f"  Height       : {tree.get_height()}")
    print(f"  Black Height : {tree.get_black_height()}")


def lookup_word(tree, word):
    word = word.strip().lower()
    if tree.search(word):
        print("YES")
    else:
        print("NO")


def main():
    tree = RBTree()
    load_dictionary(tree)

    while True:
        print("=" * 35)
        print("     English Dictionary Menu")
        print("=" * 35)
        print("1. Insert a word")
        print("2. Look up a word")
        print("3. Print tree info (size / height / black-height)")
        print("4. Exit")
        print("-" * 35)

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            word = input("Enter word to insert: ")
            insert_word(tree, word)

        elif choice == "2":
            word = input("Enter word to look up: ")
            lookup_word(tree, word)

        elif choice == "3":
            print(f"  Size         : {tree.get_size()}")
            print(f"  Height       : {tree.get_height()}")
            print(f"  Black Height : {tree.get_black_height()}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please enter 1, 2, 3, or 4.")

        print()


if __name__ == "__main__":
    main()