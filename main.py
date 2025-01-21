import json

class Student:
    def __init__(self, jmeno, vek, trida):
        self.jmeno = jmeno
        self.vek = vek
        self.trida = trida
# každý student má vlastní jméno (obsahuje i přijmení), věk a třídu 

    def __repr__(self):
        return f"jméno: {self.jmeno}, věk: {self.vek}, třída: {self.trida}" #výpis informací o studentovi


class databaze_studentu:
    def __init__(self, soubor):
        self.soubor = soubor
        self.studenti = []
        self.nacti_studenty()

    def nacti_studenty(self):
        with open(self.soubor, "r", encoding="utf-8") as f:
            data = json.load(f)
            for student in data:
                self.studenti.append(Student(**student)) #



    def uloz_studenty(self):
        with open(self.soubor, "w", encoding="utf-8") as f:
            studenti_data = []
            for student in self.studenti:
                studenti_data.append(student.__dict__) # __dict__ je slovník takže se nám to přemění do tohoto typu: {"jmeno": "Petr Svoboda", "vek": 17, "trida": "3B"}
            json.dump(studenti_data, f, ensure_ascii=False)

    def pridej_studenta(self, jmeno, vek, trida):
        novy_student = Student(jmeno, vek, trida)
        self.studenti.append(novy_student)
        self.uloz_studenty()

    def vyhledej_studenta(self, jmeno):
        vysledky = []
        reseni = False #udělal jsem to zde způsobem že pokud se podmínka splní tak se přepne na True protože se mi libí možnost že vím pokud se daná podmínka splnila při případném debugingu 
        for student in self.studenti:
            if student.jmeno == jmeno:
                vysledky.append("✦✦✦"f"  jméno: {student.jmeno}, věk: {student.vek}, třída: {student.trida}  " "✦✦✦") # zde jsem se snažil to nějak rozumně oddělit od sebe tak jsem přidal "✦✦✦"
                reseni = True

        if reseni == True:
            return print(vysledky)
        else: 
            return print(f"Student {jmeno} nebyl nalezen v databázi.")

    def vymaz_studenta(self, jmeno):
        nova_seznamka = [] #přepíše seznam studentů bez toho, kterýho chci smazat
        for student in self.studenti:
            if student.jmeno != jmeno: # tady to porovná s inputem
                nova_seznamka.append(student)
        self.studenti = nova_seznamka
        self.uloz_studenty()

    def prumerny_vek(self):
        if not self.studenti:
            return 0
        else:    
            celkovy_vek = 0
            for student in self.studenti:
                celkovy_vek += student.vek
            return print(f"Průměrný věk je zhruba {celkovy_vek / len(self.studenti) } let(roků).") # aritmetický průměr nic víc


# Použití
databaze = databaze_studentu("studenti.json") # nacteni souboru, ze kterého následně čerpáme

# databaze.pridej_studenta("Jan Novak", 18, "4A") # tento řádek jsem myslel :-)
databaze.vyhledej_studenta("Jan Novak") # projde soubor studenti.json při naleznutí zadaného jména v parametru napíše údaje. Pokud ho to nenajde, tak nám to řekne že student s daným jmenem neexisutje.
databaze.prumerny_vek()
# databaze.vymaz_studenta("Jan Novak") # <- funguje to akorát byste ho museli pak přidat znovu na řádku o 3 výše. 