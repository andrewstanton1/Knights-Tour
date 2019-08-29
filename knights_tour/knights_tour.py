from tkinter import Frame, Canvas, Button, Tk


class BoardGame(Frame):
    """
    """
    def __init__(self, master, n):
        Frame.__init__(self, master)
        self.boardsize = 400
        self.sqsize = self.boardsize // n
        self.master.title("Knight's Tour")
        self.knights_tour(n)
        self.grid(row=0, column=0)
        self.counter = 0
        self.s = set()

    def action(self, button, coords, clicked, finalGridColor, n, buttons):
        """
        """
        move = False
        if self.counter > 0:
            # possible moves from current position
            b = [
                (self.s[0] + i, self.s[1] + j)
                for i in range(-2, 3, 4)
                for j in range(-1, 2, 2)
            ]
            b += [
                (self.s[0] + j, self.s[1] + i)
                for i in range(-2, 3, 4)
                for j in range(-1, 2, 2)
            ]
            for x in b:
                if (
                    coords[button] == x
                ):  # if player moves matches one of the possible moves
                    move = True

        if move is True or self.counter == 0:  # change color of occupied spaces
            if clicked[0]:
                clicked[0]["bg"] = "steelblue1"
                clicked[0]["activebackground"] = "steelblue1"
            button["bg"] = "orange"
            button["activebackground"] = "orange"
            clicked[0] = button
            finalGridColor[button] = "red"
            self.counter += 1
            self.s = coords[button]

            gameCompleted = False  # end game flashy stuff
            for key in finalGridColor:
                if finalGridColor[key] != "red":
                    gameCompleted = False
                    break
                else:
                    gameCompleted = True

            if gameCompleted is True:
                print(
                    "Congratulations, you beat the game in "
                    + str(self.counter)
                    + " moves!"
                )
                self.winner(buttons, n, "pink")
                tk.after(5000, tk.destroy)

    def winner(self, buttons, n, color):  # you win endgame
        tk.after(500)
        for x in buttons:
            x["bg"] = color
            x.config(text="You Win!")

    def showGrid(self, button, coords, row, column):  # get coordinates of buttons
        coords[button] = (row, column)

    def knights_tour(self, n):  # create board
        mainframe = Frame(self, padx=5, pady=5)
        mainframe.grid(column=0, row=0, sticky="n,e,s,w")

        self.board = Canvas(
            mainframe,
            width=self.boardsize,
            height=self.boardsize,
            borderwidth=0,
            highlightthickness=0,
            bg="white",
        )
        self.board.grid(row=1, column=0)

        clicked = [None]
        gcolor = {0: "brown3", 1: "saddle brown"}
        coords = {}
        finalGridColor = {}
        buttons = []
        for row in range(n):
            for col in range(n):
                button = Button(self.board)
                button.grid(
                    column=col,
                    row=row,
                    sticky="n,e,s,w",
                    command=self.showGrid(button, coords, row, col),
                )
                button.config(
                    width=int(self.boardsize / (10 * n)),
                    height=int(self.boardsize / (20 * n)),
                    bg=gcolor[(row + col) % 2],
                )
                button["command"] = lambda button=button: self.action(
                    button, coords, clicked, finalGridColor, n, buttons
                )
                finalGridColor[button] = button.cget("bg")
                buttons.append(button)


if __name__ == "__main__":
    n = 0
    while n < 1:
        print("What dimension board would you like?")
        n = int(input())
        if n < 1:
            print("Sorry the dimension has to be at least 1\n")

    tk = Tk()
    ls = BoardGame(tk, n)
    tk.lift()
    tk.mainloop()
