voted = {}

voted['Jim'] = 6
voted['Pam'] = 12
voted['Mike'] = 7
voted['Mindy'] = 8
voted['Bj'] = 11

def check_voter(name):
    if voted.get(name):
        print("Kick them out")
    else:
        voted[name] = True
        print("Let the person vote")

check_voter("Mlondi")
check_voter("Mchunu")
check_voter("Mlondi")