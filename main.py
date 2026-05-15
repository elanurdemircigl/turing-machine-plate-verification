class TuringPlaka:
    def __init__(self, input_string):
        self.tape = list(input_string)
        self.state = "q0"
        self.pos = 0

    def is_digit(self, c):
        return c.isdigit()

    def is_upper(self, c):
        return c.isalpha() and c.isupper()

    def step(self):

        if self.pos < len(self.tape):
            c = self.tape[self.pos]
            print(f"Durum {self.state}, Okunan: {c}")

        else:
            c = "boşluk"
            print(f"Durum {self.state}, Okunan: boşluk")

        if self.state == "q0":
            self.state = "q1" if self.is_digit(c) else "REJECT"

        elif self.state == "q1":
            self.state = "q2" if self.is_digit(c) else "REJECT"

        elif self.state == "q2":
            self.state = "q3" if self.is_upper(c) else "REJECT"

        elif self.state == "q3":
            self.state = "q4" if self.is_upper(c) else "REJECT"

        elif self.state == "q4":
            self.state = "q5" if self.is_digit(c) else "REJECT"

        elif self.state == "q5":
            self.state = "q6" if self.is_digit(c) else "REJECT"

        elif self.state == "q6":
            self.state = "q7" if self.is_digit(c) else "REJECT"

        self.pos += 1

    def run(self):
        print(f"Girdi: {''.join(self.tape)}")
        while self.state not in ["REJECT", "q7"]:
            self.step()

        if self.state == "q7":
            print("Durum q7, Okunan: boşluk")
            return "KABUL"
        return "RED"
plaka = input("plaka giriniz: ")

main = TuringPlaka(plaka)
sonuc = main.run()
print("Sonuç:", sonuc)