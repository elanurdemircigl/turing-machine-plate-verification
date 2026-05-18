class TuringMachine:

    def __init__(self, tape_input):

        self.tape = list(tape_input) + ["_"]
        self.head = 0
        self.state = "q0"
        self.accept_state = "qa"
        self.reject_state = "qr"
        self.digits = "0123456789"
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.transitions = {}
        self.build_transitions()
    def build_transitions(self):
        for N in self.digits:
            self.transitions[("q0", N)] = ("q1", "X", "R")
        for N in self.digits:
            self.transitions[("q1", N)] = ("q2", "X", "R")
        for L in self.letters:
            self.transitions[("q2", L)] = ("q3", "Y", "R")

        for L in self.letters:
            self.transitions[("q3", L)] = ("q4", "Y", "R")
        for N in self.digits:
            self.transitions[("q4", N)] = ("q5", "Z", "R")

        for N in self.digits:
            self.transitions[("q5", N)] = ("q6", "Z", "R")

        for N in self.digits:
            self.transitions[("q6", N)] = ("q7", "Z", "R")
        self.transitions[("q7", "_")] = ("qa", "_", "R")

    def read(self):
        return self.tape[self.head]

    def write(self, char):
        self.tape[self.head] = char

    def move(self, direction):

        if direction == "R":
            self.head += 1

            if self.head >= len(self.tape):
                self.tape.append("_")

        elif direction == "L":

            if self.head == 0:
                self.tape.insert(0, "_")
            else:
                self.head -= 1

    def step(self):
        symbol = self.read()
        print(f"Durum: {self.state}, Okunan: {symbol}")

        key = (self.state, symbol)

        if key not in self.transitions:
            self.state = self.reject_state
            return

        new_state, write_symbol, direction = self.transitions[key]

        self.write(write_symbol)
        self.move(direction)
        self.state = new_state

    def run(self):
        while self.state not in [self.accept_state, self.reject_state]:
            self.step()
        if self.state == self.accept_state:
            print("Sonuç: KABUL")
        else:
            print("Sonuç: RED")
plaka = input("Plaka giriniz: ")
main = TuringMachine(plaka)
main.run()
