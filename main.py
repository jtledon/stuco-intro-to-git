def main():
    print("Running...")
    word = input("Input text to reverse: ").lower()
    print("Reversing...")
    reverse(word)
    unique(word)
    return

def reverse(word):
    print(word[::-1])

def unique(word):
    chars = {*word}
    print("Number of unique characters: " + str(len(chars)))

if __name__ == "__main__":
    main()
