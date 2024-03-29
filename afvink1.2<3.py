# Naam: Tijs
# Datum: 2045
# Versie: miljoen

def main():
    bestand = "alpaca.fna"
    headers, seqs = lees_inhoud(bestand)
    zoekwoord = input("Geef een zoekwoord op: ")
    for i in range(len(headers)):
        if zoekwoord in headers[i]:
            print("Header:",headers[i])
            check_is_dna = is_dna(seqs[i])
            if check_is_dna:
                print("Sequentie is DNA")
                knipt(seqs[i])
            else:
                print("Sequentie is geen DNA. Er is iets fout gegaan.")       
    

def lees_inhoud(bestands_naam):
    try:
        bestand = open(bestands_naam)
    except FileNotFoundError:
        print("File niet gevonden!")
        quit()

    headers = []
    seqs = []
    seq = ""

    for line in bestand:
        line=line.strip()
        if ">" in line:
            if seq != "":
                seqs.append(seq)
                seq = ""
            headers.append(line)
        else:
            seq += line.strip()
    seqs.append(seq)
    return headers, seqs

    
def is_dna(seq):
    dna = False
    a = seq.count("A")
    t = seq.count("T")
    c = seq.count("C")
    g = seq.count("G")
    total = a + t + c + g
    if total == len(seq):
        dna = True
    
    return dna


def knipt(alpaca_seq):
    try:
        bestand = open("enzymen.txt")
    except FileNotFoundError:
        print("Enzym file niet gevonden")
        quit()

    for line in bestand:
        naam, seq = line.split(" ")
        seq = seq.strip().replace("^","")
        if seq in alpaca_seq:
            print(naam, "knipt in sequentie")
    
    


main()
