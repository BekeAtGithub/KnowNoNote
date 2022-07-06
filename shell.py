from data.lexer import Lexer

def main():
    print("Know No Note... Not A Single One.")
    for x in count():
        usr_inp = input(f"Note({x})> ")
        result, error = run(usr_inp)

        if error: print(error)
        else: print(result)

def run(text):

if __name__ == "__main__":
    main()