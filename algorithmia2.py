words = 'THE,OWE,MES,ROD,HER'.split(',')
text = 'AWAKEN THE POWER ADORNED WITH THE FLAMES BRIGHT IRE'.split(' ')

#WORDS:LOR,LL,SI,OR,DO,OL,AL
words = 'LOR,LL,SI,OR,DO,OL,AL'.split(',')

rawtext = 'LOREM IPSUM DOLOR SIT AMET, CONSECTETUR ADIPISCING ELIT, SED DO EIUSMOD TEMPOR INCIDIDUNT UT LABORE ET DOLORE MAGNA ALIQUA. UT ENIM AD MINIM VENIAM, QUIS NOSTRUD EXERCITATION ULLAMCO LABORIS NISI UT ALIQUIP EX EA COMMODO CONSEQUAT. DUIS AUTE IRURE DOLOR IN REPREHENDERIT IN VOLUPTATE VELIT ESSE CILLUM DOLORE EU FUGIAT NULLA PARIATUR. EXCEPTEUR SINT OCCAECAT CUPIDATAT NON PROIDENT, SUNT IN CULPA QUI OFFICIA DESERUNT MOLLIT ANIM ID EST LABORUM.'
text = rawtext.translate(str.maketrans("","",".,")).strip().split(' ')


# Part I
print(sum([rw in w for w in text].count(True) for rw in words))


#Part II
def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]
shield = read_input('shield.txt')
"""
shield = '''WORDS:THE,OWE,MES,ROD,HER,QAQ

AWAKEN THE POWE ADORNED WITH THE FLAMES BRIGHT IRE
THE FLAME SHIELDED THE HEART OF THE KINGS
POWE PO WER P OWE R
THERE IS THE END
QAQAQ'''.splitlines()
"""

#print(shield)

words = shield[0].split(':', 1)[1].split(',')
text = shield[2:]

number = 0
for line in text:
    s = set()

    for word in words:
        for w in (word, word[::-1]):
            start = 0
            while True:
                n = line.find(w, start)
                if n < 0:
                    break
                else:
                    s.update(set(range(n, n+len(w))))
                    start = n + 1
    number += len(s)

print(number)

# Part III
'''
Fortsättning följer
'''