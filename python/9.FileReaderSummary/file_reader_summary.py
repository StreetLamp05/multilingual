"""
9. File Reader Summary
- [x] Open and read a `.txt` file
- [x] Print number of lines, words, and characters (write to output file too)
- [x] Handle file exceptions with `try`/`except`
"""

import os

def main():
    print(os.listdir(os.getcwd()))
    file_dir = input("Enter a directory path (input.txt is provided): ")
    try:
        with open(os.path.join(os.getcwd(), file_dir), "r") as file:
            content = file.read()
        num_lines = content.count("\n") + 1 if content else 0
        num_words = len(content.split())if content else 0
        num_chars = len(content)if content else 0
        summary = (
            f"Summary for: {file_dir}\n"
            f"Number of lines: {num_lines}\n"
            f"Number of words: {num_words}\n"
            f"Number of characters: {num_chars}\n"
        ) # summary
        print(summary)
        with open(os.path.join(os.getcwd(), "output.txt"), "w") as file:
            file.write(summary)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(e)




if __name__ == "__main__":
    main()