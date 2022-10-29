import tkinter as tk

symbols = ["7", "8", "9", "/", "\u21BA", "C", "4", "5", "6", "*", "(", ")", "1", "2", "3", "-", "x^2", "\u221A", "0", ",", "%", "+",]

COLOR = "#f2f4f7"

def calculate(field_for_data, screen, info):
    def isLastCharCorrect(text):
        i = 1

        while text[-i] == ")":
            i += 1

        return text[-i].isdigit()

    def isMultipleOperators(text):

        for i in range(len(text)):
            if not text[i].isdigit() and not text[i + 1].isdigit():
                return True

        return False

    def replacePowChar(text):

        for i in range(len(text)):
            if text[i] == "^":
                text = text[:i] + "**" + text[i + 1 :]

        return text

    def f():
        text = field_for_data.get()

        if not isLastCharCorrect(text) or isMultipleOperators(text):
            info["text"] = "Błędne wyrażenie"

        else:
            info["text"] = ""
            for i in range(1, len(screen)):
                if screen[i]["text"]:
                    screen[i - 1]["text"] = screen[i]["text"]

            if "^" in text:
                phrase = replacePowChar(text)
                screen[-1]["text"] = text + " = " + str(eval(phrase))

            else:
                screen[-1]["text"] = text + " = " + str(eval(text))
        field_for_data.delete(0, tk.END)

    return f

def initScreen(root):

    screen = [
        tk.Label(root, bg="#C0CBCB", width=55, anchor="w", borderwidth=2)
        for i in range(3)
    ]

    for i in range(len(screen)):
        screen[i].grid(row=i, columnspan=6, ipady=15, ipadx=1)

    return screen


def initWindow():
    root = tk.Tk()
    root.configure(bg=COLOR)
    root.geometry("470x430")
    root.title("Kalkulator")

    return root


def initFieldForData(root, screen):

    field_for_data = tk.Entry(
        root, borderwidth=0, highlightcolor="white", highlightbackground="white"
    )
    field_for_data.grid(row=len(screen), columnspan=6, ipadx=142, ipady=10)

    info = tk.Label(root, bg="white", width=55, anchor="w", borderwidth=2)
    info.grid(row=len(screen) + 1, columnspan=6, ipady=15, ipadx=1)

    return field_for_data, info


def buttonClick(field_for_data, symbol):
    def f():
        if symbol == "\u21BA":
            bufor = field_for_data.get()[:-1]
            field_for_data.delete(0, tk.END)
            field_for_data.insert(0, bufor)

        elif symbol == "C":
            field_for_data.delete(0, tk.END)

        else:
            text = symbol if symbol != "x^2" else "^2"
            field_for_data.insert(tk.END, text)

    return f


def initButtons(root, screen, info):
    buttons = [
        tk.Button(root, text=symbol, bg=COLOR, borderwidth=0) for symbol in symbols
    ]

    j = len(screen) + 2
    for i in range(len(buttons)):
        if i % 6 == 0:
            j += 1

        margin = 21 if len(symbols[i]) == 1 else 10
        buttons[i].grid(row=j, column=i % 6, ipady=5, ipadx=margin)
        buttons[i].configure(command=buttonClick(field_for_data, buttons[i]["text"]))

    equal_sign = tk.Button(
        root,
        text="=",
        bg="#00BFFF",
        borderwidth=0,
        command=calculate(field_for_data, screen, info),
    )

    equal_sign.grid(row=len(screen) + 6, column=4, columnspan=2, ipady=5, ipadx=50)

    return buttons


if __name__ == "__main__":

    root = initWindow()

    screen = initScreen(root)

    field_for_data, info = initFieldForData(root, screen)

    buttons = initButtons(root, screen, info)

    root.mainloop()
