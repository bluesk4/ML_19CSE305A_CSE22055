def main():
    word = input("Enter word: ")
    letter_occurences(word)
def letter_occurences(word: str):
    occur = {}
    flag = 0
    for letter in word:
        if letter not in occur:
            occur[letter] = 1
        else:
            occur[letter] += 1
    max = 0
    key = ""
    for letter in occur:
        if occur[letter] > max:
            max = occur[letter]
            key = letter
        else:
            continue
     
    for letter in occur:
        if occur[letter] == max and letter != key:
            flag = 1
            break
    if flag == 0:
        print(f"Letter which occurs the most is {key} and number of occurence is {max}")
    else:
        print("Tie")           
main()