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
scales = read_input('everybody_codes_e2024_q02_p3.txt')
#scales = read_input('test_e2024_q02_p3.txt')

words = scales[0].split(':', 1)[1].split(',')
text = scales[2:]

number = 0
s = set()
for lineno, line in enumerate(text):

    for word in words:
        augline = line + line[:len(word)-1]
        for w in (word, word[::-1]):
            start = 0
            while True:
                n = augline.find(w, start)
                if n < 0:
                    break
                else:
                    s.update(set((lineno, m % len(line)) for m in range(n, n+len(w))))
                    start = n + 1
for k in range(len(text[0])):
    for word in words:
        augline = ''.join(line[k] for line in text)
        for w in (word, word[::-1]):
            start = 0
            while True:
                n = augline.find(w, start)
                if n < 0:
                    break
                else:
                    s.update(set((r, k) for r in range(n, n + len(w)) ))
                    start = n + 1
print(len(s))
#print(s)