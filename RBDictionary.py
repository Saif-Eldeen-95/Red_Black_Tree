#
# from RBTree import print_tree_size, insert, print_tree_height, print_tree_black_height, search, create_tree
#
# DICT_FILE = "Dictionary.txt"
#
# def load_dictionary(tree):
#
#     print("Loading dictionary...")
#     try:
#         with open(DICT_FILE, "r") as f:
#             for line in f:
#                 word = line.strip().lower()  # remove whitespace + normalize to lowercase
#                 if word:
#                     insert(tree, word)
#         print(f"Done! {print_tree_size(tree)} words loaded.\n")
#     except FileNotFoundError:
#         print(f"ERROR: '{DICT_FILE}' not found. Starting with empty dictionary.\n")
#
#
# def insert_word(tree, word):
#
#     word = word.strip().lower()
#     success = insert(tree, word)
#
#     if not success:
#         print("ERROR: Word already in the dictionary!")
#     else:
#         # Append the new word to the file so it is saved permanently
#         with open(DICT_FILE, "a") as f:
#             f.write(word + "\n")
#         print(f"'{word}' inserted successfully.")
#
#     # Always print these stats after every insertion attempt
#     print(f"  Size         : {print_tree_size(tree)}")
#     print(f"  Height       : {print_tree_height(tree)}")
#     print(f"  Black Height : {print_tree_black_height(tree)}")
#
#
# def lookup_word(tree, word):
#     """Print YES or NO depending on whether the word exists."""
#     word = word.strip().lower()  # normalize to lowercase
#     result = search(tree, word)
#     if result != tree["NIL"]:
#         print("YES")
#     else:
#         print("NO")
#
#
# # ──────────────────────────────────────────────────────────────
# #  MAIN MENU
# # ──────────────────────────────────────────────────────────────
#
# def main():
#     tree = create_tree()
#     load_dictionary(tree)
#
#     while True:
#         print("=" * 35)
#         print("     English Dictionary Menu")
#         print("=" * 35)
#         print("1. Insert a word")
#         print("2. Look up a word")
#         print("3. Print tree info")
#         print("4. Exit")
#         print("-" * 35)
#
#         choice = input("Choose (1-4): ").strip()
#
#         if choice == "1":
#             word = input("Enter word to insert: ")
#             insert_word(tree, word)
#
#         elif choice == "2":
#             word = input("Enter word to look up: ")
#             lookup_word(tree, word)
#
#         elif choice == "3":
#             print(f"  Size         : {print_tree_size(tree)}")
#             print(f"  Height       : {print_tree_height(tree)}")
#             print(f"  Black Height : {print_tree_black_height(tree)}")
#
#         elif choice == "4":
#             print("Goodbye!")
#             break
#
#         else:
#             print("Invalid choice. Enter 1, 2, 3, or 4.")
#
#         print()
#
#
# if __name__ == "__main__":
#     main()
from RBTree import RBTree

# ──────────────────────────────────────────────
#  SECTION 3 – Dictionary Application
# ──────────────────────────────────────────────

DICT_FILE = "dictionary.txt"   # ← change this path if needed

def load_dictionary(tree):
    """Read every word from the file and insert it into the tree."""
    print("Loading dictionary... (this may take a moment)")
    try:
        with open(DICT_FILE, "r") as f:
            for line in f:
                word = line.strip().lower()     # remove \n and \r
                if word:                # skip empty lines
                    tree.insert(word)   # duplicates are ignored automatically
        print(f"Done! {tree.get_size()} words loaded.\n")
    except FileNotFoundError:
        print(f"ERROR: '{DICT_FILE}' not found. Starting with an empty dictionary.\n")


def insert_word(tree, word):
    """
    Insert a word into the tree AND append it to the file.
    Print size, height, and black-height after every insertion.
    """
    word = word.strip().lower()

    if tree.search(word):
        print(f"ERROR: Word already in the dictionary!")
    else:
        tree.insert(word)

        # Append the new word to the file so it is saved permanently
        with open(DICT_FILE, "a") as f:
            f.write(word + "\n")

        print(f"'{word}' inserted successfully.")

    # Always print these three stats (even on failure, per assignment note)
    print(f"  Size         : {tree.get_size()}")
    print(f"  Height       : {tree.get_height()}")
    print(f"  Black Height : {tree.get_black_height()}")


def lookup_word(tree, word):
    """Print YES or NO depending on whether the word exists."""
    word = word.strip().lower()
    if tree.search(word):
        print("YES")
    else:
        print("NO")


# ──────────────────────────────────────────────
#  SECTION 4 – Main Menu
# ──────────────────────────────────────────────

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

        print()   # blank line for readability


if __name__ == "__main__":
    main()