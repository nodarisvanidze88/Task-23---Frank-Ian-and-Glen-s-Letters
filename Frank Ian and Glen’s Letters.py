from pyfiglet import Figlet
import sys
import random

def main():
    admin = sys.argv
    user = input("input: ")
    font = Figlet().getFonts()
    try:
        if check_specified_Font(admin) == 1:
            print(f"Output:\n {text_Selected_Font(user,admin)}")
        elif check_specified_Font(admin) == 2:
            print(f"Output:\n {text_random_Font(user,rand_font(font))}")
    except:
        sys.exit

def argv_len(a):
    return len(a)

def check_specified_Font(b):
    if argv_len(b) == 3 and "-f" in b or "--f" in b:
        return 1
    elif argv_len(b) == 1:
        return 2
    else:
        return False

def rand_font(fonts):
    return random.choice(fonts)

def text_Selected_Font(txt,ad):
    font1 = str(ad[2])
    return Figlet(font=font1).renderText(txt)

def text_random_Font(txt,fn):
    return Figlet(font=fn).renderText(txt)

if __name__ == "__main__":
    main()
