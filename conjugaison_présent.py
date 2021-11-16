def trouve_groupe(verbe: str) -> int:
    g1 = ["aa", "ää", "ea", "eä", "ia", "iä", "oa", "ua", "yä"]
    g2 = ["da", "dä"]
    g3 = ["na", "nä", "la", "lä", "ra", "rä", "ta", "tä"]
    g4 = ["ata", "ätä", "ota", "ötä", "uta", "ytä"]
    g5 = ["ita", "itä"]
    g6 = ["eta", "etä"]
    
    if verbe[-2:] in g1:
        return 1
    
    if verbe[-2:] in g2:
        return 2

    if verbe[-3:] in g4:
        return 4   
    
    if verbe[-3:] in g5:
        return 5
    
    if verbe[-3:] in g6:
        return 6
    
    if verbe[-2:] in g3:
        return 3
    
def trouve_radical(verbe: str, groupe: int) -> str:
    if groupe == 1:
        return verbe[:-1]
    
    if groupe == 2:
        return verbe[:-2]
    
    if groupe == 3:
        return verbe[:-2] + "e"
    
    if groupe == 4:
        return verbe[:-2] + verbe[-1]
    
    if groupe == 5:
        return verbe[:-1] + "se"
    
    if groupe == 6:
        return verbe[:-2] + "ne"
        
def harmonie_vocalique(verbe: str) -> bool:
    if verbe[-1] == "ä":
        return True
    elif verbe[-1] == "a":
        return False

def affaibli_rad(radical: str) -> str:
    
    lettres = radical[-3:-1]
    
    radical = radical.split()
    
    if lettres == "kk" or lettres == "pp" or lettres == "tt":
        r = []
        r.append(radical[:-2])
        
        r.append(radical[-1])
        print("".join(r))
        return "".join(r)
    
    if "nt" == lettres:
        radical[-2] = "n"
        return "".join(radical)
        
    if "nk" == lettres:
        radical[-2] = "g"
        return "".join(radical)
    
    if "mp" == lettres:
        radical[-2] = "m"
        return "".join(radical)
        
    if "lt" == lettres:
        radical[-2] = "l"
        return "".join(radical)
        
    if "rt" == lettres:
        radical[-2] = "r"
        return "".join(radical)
        
    lettres = radical[-4:-1]
    
    if "lke" in radical:
        radical[-2] = "j"
        return "".join(radical)
    
    if "rke" in radical:
        radical[-2] = "j"
        return "".join(radical)
        
    lettre = radical[-2]
    
    if lettre == "t":
        radical[-2] = d
        return "".join(radical)
    
    if lettre == "k":
        radical[:-2] + radical[-1]
        return "".join(radical)
        
    if lettre == "p":
        radical[-2] = "v"
        return "".join(radical)
    
    
def gradation_consonnantique(radical: str, groupe: int) -> list:
    
    radicals = ["" for _ in range(6)]
    
    radical_weak = affaibli_rad(radical)
    print(radical_weak)
    radical_strong = radical
    
    if groupe == 1:
        for i in range(6):
            if i == 2 or i == 5:          # il et ils
                radicals[i] = radical_strong
            else:
                radicals[i] = radical_weak
    
    # elif trouve_groupe(verbe) == 2:
    #     return radical
    
    # elif trouve_groupe(verbe) == 3:
    #     return
    
    # elif trouve_groupe(verbe) == 4:
    #     if radical[-3] == 'k':
    #         radical[-3] == 'kk'
    #     elif radical[-3] == 'p':
    #         radical[-3] == 'pp'
    #     elif radical[-3] == 't':
    #         radical[-3] == 'tt'
    #     elif radical[-3] == 'd':
    #         radical[-3] == 't'
    #     else : #si non mono consonantique our si sans possibilité de gradation
    #         if radical[-4:-2] == 'nn':
    #             radical[-3] == 'nt'
    return radicals

verbe = input()
groupe = trouve_groupe(verbe)
print(groupe)
radical = trouve_radical(verbe, groupe)
radicals = gradation_consonnantique(radical, groupe)
# print(radical, radical_grad)

terminaisons = ["n", "t", "", "mme", "tte", "vat"]

if groupe != 2:
    terminaisons[2] = radical[-1]
    if radical[-2] == radical[-1]:
        terminaisons[2] = ""
    
if harmonie_vocalique(verbe): #determine la terminaison du 3PP que doit porter le verbe
    terminaisons[5] = "vät"
    
for terminaison, radical1 in zip(terminaisons, radicals):
    print(radical1, terminaison, sep="")
    
# https://uusikielemme.fi/finnish-grammar/consonant-gradation/verbtype-1-consonant-gradation