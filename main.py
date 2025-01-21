import json

class Student:
    def __init__(self, jmeno, vek, trida):
        self.jmeno = jmeno
        self.vek = vek
        self.trida = trida

    def __repr__(self):
        return f"Student(jméno: {self.jmeno}, věk: {self.vek}, třída: {self.trida})"


class databaze_studentu:
    def __init__(self, soubor):
        self.soubor = soubor
        self.studenti = []
        self.nacti_studenty()

    def nacti_studenty(self):
        with open(self.soubor, "r", encoding="utf-8") as f:
            data = json.load(f)
            for student in data:
                self.studenti.append(Student(**student))



    def uloz_studenty(self):
        with open(self.soubor, "w", encoding="utf-8") as f:
            studenti_data = []
            for student in self.studenti:
                studenti_data.append(student.__dict__)
            json.dump(studenti_data, f, ensure_ascii=False)

    def pridej_studenta(self, jmeno, vek, trida):
        novy_student = Student(jmeno, vek, trida)
        self.studenti.append(novy_student)
        self.uloz_studenty()

    def vyhledej_studenta(self, jmeno):
        vysledky = []
        reseni = False
        for student in self.studenti:
            if student.jmeno == jmeno:
                vysledky.append("✦✦✦"f"  jméno: {student.jmeno}, věk: {student.vek}, třída: {student.trida}  " "✦✦✦")
                reseni = True

        if reseni == True:
            return print(vysledky)
        else: 
            return print(f"Student {jmeno} nebyl nalezen v databázi.")

    def vymaz_studenta(self, jmeno):
        nova_seznamka = []
        for student in self.studenti:
            if student.jmeno != jmeno:
                nova_seznamka.append(student)
        self.studenti = nova_seznamka
        self.uloz_studenty()

    def prumerny_vek(self):
        if not self.studenti:
            return 0
        celkovy_vek = 0
        for student in self.studenti:
            celkovy_vek += student.vek
        return celkovy_vek / len(self.studenti)


# Použití
databaze = databaze_studentu("studenti.json")
# databaze.pridej_studenta("Jan Novak", 18, "4A")
# databaze.pridej_studenta("Petr Svoboda", 17, "3B")
databaze.vyhledej_studenta("Jan Novak")
# print(f"Průměrný věk: {databaze.prumerny_vek()}")
# databaze.vymaz_studenta("Jan Novak")