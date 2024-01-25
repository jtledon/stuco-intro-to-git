def main():
    print("Running...")
    word = input("Input text to reverse: ")
    reverse(word)
    return

def reverse(word):
    print(word[::-1])

if __name__ == "__main__":
    main()
