def main():
    print("Running...")
    word = input("Input text to reverse: ").lower()
    reverse(word)
    unique(word)
    return

def reverse(word):
    print(word[::-1])

def unique(word):
    chars = {*word}
    print(len(chars))

if __name__ == "__main__":
    main()
