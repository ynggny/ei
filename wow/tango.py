import csv
import random

def mark():##ドットを追加
    dotli = ['     ■  ■']
    underd = ['        ■']
    return dotli,underd

def oono0 ():##日本語
    voc = []
    with open ('japanese.csv','r') as e :
        csvv = csv.reader(e)
        for o in csvv :
            voc.append(o)
    return voc
    pass
def oono ():##英語
    ass = []
    with open ('chinko.csv','r') as f :
        a = csv.reader(f)
        for i in a :
            ass.append(i)
    return ass
def choiceng():##ランダムに英単語を抽出
    jcon = []
    engg =[]
    engli = oono0()
    japo = oono()
    eng = random.sample(engli,20)
    return eng
def addjap():##対応する日本語訳を追加
    ull =[]
    eigo1=[]
    eigo = oono0()
    engliq = choiceng()
    japo = oono()
    for d in range(len(engliq)):
        che = engliq[d]
        sar = japo.index(che)
        jap = eigo[sar]
        yyc = jap + list("")
        are = che + list("     ⓪①")
        eigo1.append(are)
        ull.append(yyc)
    return eigo1 , ull

##整形してリストに追加
def fusion():
    levels = []
    er,re = mark()
    ae = oono()
    aw = oono0()
    a,b = addjap()
    c,d = addjap()
    levels.extend(list(er))
    levels.extend(a)
    levels.extend(list(re))
    levels.extend(list(er))
    levels.extend(c)
    levels.extend(list(re))
    levels.extend(list(er))
    levels.extend(b)
    levels.extend(list(re))
    levels.extend(list(er))
    levels.extend(d)
    levels.extend(list(re))
    return levels
