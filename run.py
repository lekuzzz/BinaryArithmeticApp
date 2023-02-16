from flask import Flask,request,render_template
import random,clr,os
pathDLL = os.getcwd() + "/BinNum3.dll"
clr.AddReference(pathDLL)
import BinaryNumbers
from BinaryNumbers import *

rezult = 0
A = 0
B = 0
surname = None
name = None    
otch = None
grup = None
time = None
translation = False
arithmetic = False
mulanddiv = False
rezultArithmet = 0
rezultTranslat = 0
rezultMulAndDiv = 0





def toBinCode(i):
    b = bin(i)
    b = b.split('b')
    if b[0] == '0':
        rez ='0.'
    else:
        rez = '1.'
    for j in range(7-len(b[1])):
        rez = rez + '0'
    rez = rez + b[1]
    return rez

def mulAndDiv(A,B):
    A = toBinCode(A)
    B = toBinCode(B)
    fa = ForwardCode (A)
    fb = ForwardCode (B)
    ra = ReverseCode (fa)
    rb = ReverseCode (fb)
    aa = AdditionalCode (fa)
    ab = AdditionalCode (fb)

    fcm = str(fa * fb)
    fcd = str(fa / fb)
    rc = str(ra * rb)
    ac = str(aa * ab)
    
    rezult = {"fa":str(fa),"fb":str(fb),"ra":str(ra),"rb":str(rb),"aa":str(aa),"ab":str(ab),"fcm":fcm,"rc":rc,"ac":ac,"fcd":fcd}
    return rezult

def translat(A,B):
    A = toBinCode(A)
    B = toBinCode(B)
    fa = ForwardCode (A)
    fb = ForwardCode (B)
    ra = ReverseCode (fa)
    rb = ReverseCode (fb)
    aa = AdditionalCode (fa)
    ab = AdditionalCode (fb)

    fam = str(-fa)
    fbm = str(-fb)
    ram = str(-ra)
    rbm = str(-rb)
    aam = str(-aa)
    abm = str(-ab)

    fam2 = str(fa>>2)
    fbm2 = str(fb>>2)
    ram2 = str(ra>>2)
    rbm2 = str(rb>>2)
    aam2 = str(aa>>2)
    abm2 = str(ab>>2)

    fam3 = str(fa>>3)
    fbm3 = str(fb>>3)
    ram3 = str(ra>>3)
    rbm3 = str(rb>>3)
    aam3 = str(aa>>3)
    abm3 = str(ab>>3)

    fa3 = str(fa<<3)
    fb3 = str(fb<<3)
    ra3 = str(ra<<3)
    rb3 = str(rb<<3)
    aa3 = str(aa<<3)
    ab3 = str(ab>>3)

    fa4 = str(fa<<4)
    fb4 = str(fb<<4)
    ra4 = str(ra<<4)
    rb4 = str(rb<<4)
    aa4 = str(aa<<4)
    ab4 = str(ab>>4)
    
    rezult = {"fa":str(fa),"fb":str(fb),"ra":str(ra),"rb":str(rb),"aa":str(aa),"ab":str(ab),"fam":fam,"fbm":fbm,
    "ram":ram,"rbm":rbm,"aam":aam,"abm":abm,"fam2":fam2,"fbm2":fbm2,"ram2":ram2,"rbm2":rbm2,"aam2":aam2,"abm2":abm2,
    "fam3":fam3,"fbm3":fbm3,"ram3":ram3,"rbm3":rbm3,"aam3":aam3,"abm3":abm3,
    "fa3":fa3,"fb3":fb3,"ra3":ra3,"rb3":rb3,"aa3":aa3,"ab3":ab3,
    "fa4":fa4,"fb4":fb4,"ra4":ra4,"rb4":rb4,"aa4":aa4,"ab4":ab4}
    return rezult

def arithmet(A,B):
    A = toBinCode(A)
    B = toBinCode(B)
    fa = ForwardCode (A)
    fb = ForwardCode (B)
    ra = ReverseCode (fa)
    rb = ReverseCode (fb)
    aa = AdditionalCode (fa)
    ab = AdditionalCode (fb)

    fam = (-fa)
    ram = (-ra)
    aam = (-aa)

    fcs = str(fa - fb)
    fcp = str(fa + fb)
    rcs = str(ra - rb)
    rcp = str(ra + rb)
    acs = str(aa - ab)
    acp = str(aa + ab)

    fcsm = str(fam - fb)
    fcpm= str(fam + fb)
    rcsm = str(ram - rb)
    rcpm = str(ram + rb)
    acsm = str(aam - ab)
    acpm = str(aam + ab)
    
    
    rezult = {"fa":str(fa),"fb":str(fb),"ra":str(ra),"rb":str(rb),"aa":str(aa),"ab":str(ab),
    "fam":str(fam),"ram":str(ram),"aam":str(aam),
    "fcs":fcs,"fcp":fcp,"rcs":rcs,"rcp":rcp,"acs":acs,"acp":acp,
    "fcsm":fcsm,"fcpm":fcpm,"rcsm":rcsm,"rcpm":rcpm,"acsm":acsm,"acpm":acpm}
    return rezult


app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/main', methods=['GET', 'POST'])
def index():
    global A,B,rezultArithmet,rezultTranslat,rezultMulAndDiv,surname,name,otch,grup,time,translation,arithmetic,mulanddiv
    A = random.randint(8, 15)
    B = random.randint(-10, -1)

    rezultArithmet =arithmet(A,B)
    rezultTranslat = translat(A,B)
    rezultMulAndDiv = mulAndDiv(A,B) 
    
    
    if request.method == 'POST':
        try:
            surname = request.form['surname'].strip()
            name = request.form['name'].strip()
            otch = request.form['otch'].strip()
            grup = request.form['grup'].strip()
            time = request.form['time'].strip()
            if request.form.get('translation'):
                rezultTranslat = translat(A,B)
                translation = True
            if request.form.get('arithmetic'):
                rezultArithmet =arithmet(A,B)
                arithmetic = True
            if request.form.get('mulanddiv'):
                rezultMulAndDiv = mulAndDiv(A,B)
                mulanddiv = True
        except:
            file = None
    return render_template('index.html', surname = surname, name = name, otch = otch, grup = grup, time = time, translation = translation, arithmetic = arithmetic, mulanddiv = mulanddiv, A= A, B = B,)

@app.route('/end', methods=['POST'])
def end():

    AP = None
    AO = None
    AD = None
    BP = None
    BO = None
    BD = None
    APM = None
    AOM = None
    ADM = None
    BPM = None
    BOM = None
    BDM = None
    APM2 = None
    AOM2 = None
    ADM2 = None
    APM3 = None
    AOM3 = None
    ADM3 = None
    AP3 = None
    AO3 = None
    AD3 = None
    AP4 = None
    AO4 = None
    AD4 = None
    BPM2 = None
    BOM2 = None
    BDM2 = None
    BPM3 = None
    BOM3 = None
    BDM3 = None
    BP3 = None
    BO3 = None
    BD3 = None
    BP4 = None
    BO4 = None
    BD4 = None
    AOP = None
    BOP = None
    COP = None
    COPP = None
    ADP = None
    BDP = None
    CDP = None
    CDPP = None
    AOS = None
    BOS = None
    COS = None
    COPS = None
    ADS = None
    BDS = None
    CDS = None
    CDPS = None
    MAOP = None
    MBOP = None
    MCOP = None
    MCOPP = None
    MADP = None
    MBDP = None
    MCDP = None
    MAOP = None
    MBOP = None
    MCOP = None
    MCOPP = None
    MADP = None
    MBDP = None
    MCDP = None
    MCDPP1 = None
    MAOM = None
    MBOM = None
    MCOM = None
    MCOPM = None
    MADM = None
    MBDM = None
    MCDM = None
    MCDPM = None
    CPPMUL = None
    AOMUL = None
    BOMUL = None
    COMUL = None
    COPMUL = None
    ADMUL = None
    BDMUL = None
    CDMUL = None
    CDPMUL = None
    APDIV = None
    BPDIV = None
    CPDIV = None


    APMUL = None
    BPMUL = None
    CPPMUL = None
    AOMUL = None
    BOMUL = None
    COMUL = None
    COPMUL = None
    ADMUL = None
    BDMUL = None
    CDMUL = None
    CDPMUL = None
    APDIV = None
    BPDIV = None
    CPDIV = None
    isEnd = True
    countTranslat = 0
    countArithmet = 0
    countMulAndDiv = 0
    if request.method == 'POST':
        if translation:
            print(rezultTranslat)
            AP = request.form['AP'].replace(" ", "")
            
            if AP == rezultTranslat["fa"]:
                print(rezultTranslat["fa"])
                countTranslat += 1
                AP ="bg-success"
            else:
                print(AP)
                AP ="bg-danger"
            BP = request.form['BP'].replace(" ", "")
            print(rezultTranslat["fb"])
            print(BP)
            if BP == rezultTranslat["fb"]:
                countTranslat += 1
                BP ="bg-success"
            else:
                BP ="bg-danger"
            AO = request.form['AO'].replace(" ", "")
            if AO == rezultTranslat["ra"]:
                countTranslat += 1
                AO ="bg-success"
            else:
                print("APMUL")
                AO ="bg-danger"
            BO = request.form['BO'].replace(" ", "")
            if BO == rezultTranslat["rb"]:
                countTranslat += 1
                BO ="bg-success"
            else:
                BO ="bg-danger"
            AD = request.form['AD'].replace(" ", "")
            if AD == rezultTranslat["aa"]:
                countTranslat += 1
                AD ="bg-success"
            else:
                AD ="bg-danger"
            BD = request.form['BD'].replace(" ", "")
            if BD == rezultTranslat["ab"]:
                countTranslat += 1
                BD ="bg-success"
            else:
                BD ="bg-danger"
            APM = request.form['APM'].replace(" ", "")
            if APM == rezultTranslat["fam"]:
                print(rezultTranslat["fam"])
                countTranslat += 1
                APM ="bg-success"
            else:
                print(APM)
                APM ="bg-danger"
            BPM = request.form['BPM'].replace(" ", "")
            if BPM == rezultTranslat["fbm"]:
                countTranslat += 1
                BPM ="bg-success"
            else:
                BPM ="bg-danger"
            AOM = request.form['AOM'].replace(" ", "")
            if AOM == rezultTranslat["ram"]:
                countTranslat += 1
                AOM ="bg-success"
            else:
                print("APMUL")
                AOM ="bg-danger"
            BOM = request.form['BOM'].replace(" ", "")
            if BOM == rezultTranslat["rbm"]:
                countTranslat += 1
                BOM ="bg-success"
            else:
                BOM ="bg-danger"
            ADM = request.form['ADM'].replace(" ", "")
            if ADM == rezultTranslat["aam"]:
                countTranslat += 1
                ADM ="bg-success"
            else:
                ADM ="bg-danger"
            BDM = request.form['BD'].replace(" ", "")
            if BDM == rezultTranslat["abm"]:
                countTranslat += 1
                BDM ="bg-success"
            else:
                BDM ="bg-danger"
            APM2 = request.form['APM2'].replace(" ", "")
            if APM2 == rezultTranslat["fam2"]:
                print(rezultTranslat["fam2"])
                countTranslat += 1
                APM2 ="bg-success"
            else:
                print(APM2)
                APM2 ="bg-danger"
            BPM2 = request.form['BPM2'].replace(" ", "")
            if BPM2 == rezultTranslat["fbm2"]:
                countTranslat += 1
                BPM2 ="bg-success"
            else:
                BPM2 ="bg-danger"
            AOM2 = request.form['AOM2'].replace(" ", "")
            if AOM2 == rezultTranslat["ram2"]:
                countTranslat += 1
                AOM2 ="bg-success"
            else:
                print("APMUL")
                AOM2 ="bg-danger"
            BOM2 = request.form['BOM2'].replace(" ", "")
            if BOM2 == rezultTranslat["rbm2"]:
                countTranslat += 1
                BOM2 ="bg-success"
            else:
                BOM2 ="bg-danger"
            ADM2 = request.form['ADM2'].replace(" ", "")
            if ADM2 == rezultTranslat["aam2"]:
                countTranslat += 1
                ADM2 ="bg-success"
            else:
                ADM2 ="bg-danger"
            BDM2 = request.form['BDM2'].replace(" ", "")
            if BDM2 == rezultTranslat["abm2"]:
                countTranslat += 1
                BDM2 ="bg-success"
            else:
                BDM2 ="bg-danger"
            APM3 = request.form['APM3'].replace(" ", "")
            if APM3 == rezultTranslat["fam3"]:
                print(rezultTranslat["fam3"])
                countTranslat += 1
                APM3 ="bg-success"
            else:
                print(APM3)
                APM3 ="bg-danger"
            BPM3 = request.form['BPM3'].replace(" ", "")
            if BPM3 == rezultTranslat["fbm3"]:
                countTranslat += 1
                BPM3 ="bg-success"
            else:
                BPM3 ="bg-danger"
            AOM3 = request.form['AOM3'].replace(" ", "")
            if AOM3 == rezultTranslat["ram3"]:
                countTranslat += 1
                AOM3 ="bg-success"
            else:
                AOM3 ="bg-danger"
            BOM3 = request.form['BOM3'].replace(" ", "")
            if BOM3 == rezultTranslat["rbm3"]:
                countTranslat += 1
                BOM3 ="bg-success"
            else:
                BOM3 ="bg-danger"
            ADM3 = request.form['ADM3'].replace(" ", "")
            if ADM3 == rezultTranslat["aam3"]:
                countTranslat += 1
                ADM3 ="bg-success"
            else:
                ADM3 ="bg-danger"
            BDM3 = request.form['BD3'].replace(" ", "")
            if BDM3 == rezultTranslat["abm3"]:
                countTranslat += 1
                BDM3 ="bg-success"
            else:
                BDM3 ="bg-danger"
            AP3 = request.form['AP3'].replace(" ", "")
            if AP3 == rezultTranslat["fa3"]:
                print(rezultTranslat["fa3"])
                countTranslat += 1
                AP3 ="bg-success"
            else:
                AP3 ="bg-danger"
            BP3 = request.form['BP3'].replace(" ", "")
            if BP3 == rezultTranslat["fb3"]:
                countTranslat += 1
                BP3 ="bg-success"
            else:
                BP3 ="bg-danger"
            AO3 = request.form['AO3'].replace(" ", "")
            if AO3 == rezultTranslat["ra3"]:
                countTranslat += 1
                AO3 ="bg-success"
            else:
                
                AO3 ="bg-danger"
            BO3 = request.form['BO3'].replace(" ", "")
            if BO3 == rezultTranslat["rb3"]:
                countTranslat += 1
                BO3 ="bg-success"
            else:
                BO3 ="bg-danger"
            AD3 = request.form['AD3'].replace(" ", "")
            if AD3 == rezultTranslat["aa3"]:
                countTranslat += 1
                AD3 ="bg-success"
            else:
                AD3 ="bg-danger"
            BD3 = request.form['BD3'].replace(" ", "")
            if BD3 == rezultTranslat["ab3"]:
                countTranslat += 1
                BD3 ="bg-success"
            else:
                BD3 ="bg-danger"



            AP4 = request.form['AP4'].replace(" ", "")
            if AP4 == rezultTranslat["fa4"]:
                print(rezultTranslat["fa4"])
                countTranslat += 1
                AP4 ="bg-success"
            else:
                AP4 ="bg-danger"
            BP4 = request.form['BP4'].replace(" ", "")
            if BP4 == rezultTranslat["fb4"]:
                countTranslat += 1
                BP4 ="bg-success"
            else:
                BP4 ="bg-danger"
            AO4 = request.form['AO4'].replace(" ", "")
            if AO4 == rezultTranslat["ra4"]:
                countTranslat += 1
                AO4 ="bg-success"
            else:
           
                AO4 ="bg-danger"
            BO4 = request.form['BO4'].replace(" ", "")
            if BO4 == rezultTranslat["rb4"]:
                countTranslat += 1
                BO4 ="bg-success"
            else:
                BO4 ="bg-danger"
            AD4 = request.form['AD4'].replace(" ", "")
            if AD4 == rezultTranslat["aa4"]:
                countTranslat += 1
                AD4 ="bg-success"
            else:
                AD4 ="bg-danger"
            BD4 = request.form['BD4'].replace(" ", "")
            if BD4 == rezultTranslat["ab4"]:
                countTranslat += 1
                BD4 ="bg-success"
            else:
                BD4 ="bg-danger"    

        if arithmetic:
            print(rezultArithmet)
            AOP = request.form['AOP'].replace(" ", "")
            if AOP == rezultArithmet["ra"]:
                countArithmet += 1
                AOP ="bg-success"
            else:
                AOP ="bg-danger"
            BOP = request.form['BOP'].replace(" ", "")
            if BOP == rezultArithmet["rb"]:
                countArithmet += 1
                BOP ="bg-success"
            else:
                BOP ="bg-danger"
            COP = request.form['COP'].replace(" ", "")
            if COP == rezultArithmet["rcp"]:
                countArithmet += 1
                COP ="bg-success"
            else:
                COP ="bg-danger"
            COPP = request.form['COPP'].replace(" ", "")
            if COPP == rezultArithmet["fcp"]:
                countArithmet += 1
                COPP ="bg-success"
            else:
                COPP ="bg-danger"

            ADP = request.form['AOP'].replace(" ", "")
            if ADP == rezultArithmet["aa"]:
                countArithmet += 1
                ADP ="bg-success"
            else:
                ADP ="bg-danger"
            BDP = request.form['BDP'].replace(" ", "")
            if BDP == rezultArithmet["ab"]:
                countArithmet += 1
                BDP ="bg-success"
            else:
                BDP ="bg-danger"
            CDP = request.form['CDP'].replace(" ", "")
            if CDP == rezultArithmet["acp"]:
                countArithmet += 1
                CDP ="bg-success"
            else:
                CDP ="bg-danger"
            CDPP = request.form['CDPP'].replace(" ", "")
            if CDPP == rezultArithmet["fcp"]:
                countArithmet += 1
                CDPP ="bg-success"
            else:
                CDPP ="bg-danger"

            AOS = request.form['AOS'].replace(" ", "")
            if AOS == rezultArithmet["ra"]:
                countArithmet += 1
                AOS ="bg-success"
            else:
                AOS ="bg-danger"
            BOS = request.form['BOP'].replace(" ", "")
            if BOS == rezultArithmet["rb"]:
                countArithmet += 1
                BOS ="bg-success"
            else:
                BOS ="bg-danger"
            COS = request.form['COS'].replace(" ", "")
            if COS == rezultArithmet["rcs"]:
                countArithmet += 1
                COS ="bg-success"
            else:
                COS ="bg-danger"
            COPS = request.form['COPS'].replace(" ", "")
            if COPS == rezultArithmet["fcs"]: 
                countArithmet += 1
                COPS ="bg-success"
            else:
                COPS ="bg-danger"

            ADS = request.form['AOS'].replace(" ", "")
            if ADS == rezultArithmet["aa"]:
                countArithmet += 1
                ADS ="bg-success"
            else:
                ADS ="bg-danger"
            BDS = request.form['BDP'].replace(" ", "")
            if BDS == rezultArithmet["ab"]:
                countArithmet += 1
                BDS ="bg-success"
            else:
                BDS ="bg-danger"
            CDS = request.form['CDS'].replace(" ", "")
            if CDS == rezultArithmet["acs"]:
                countArithmet += 1
                CDS ="bg-success"
            else:
                CDS ="bg-danger"
            CDPS = request.form['CDPS'].replace(" ", "")
            if CDPS == rezultArithmet["fcs"]:
                countArithmet += 1
                CDPS ="bg-success"
            else:
                CDPS ="bg-danger"


            MAOP = request.form['MAOP'].replace(" ", "")
            if MAOP == rezultArithmet["ram"]:
                countArithmet += 1
                MAOP ="bg-success"
            else:
                MAOP ="bg-danger"
            MBOP = request.form['MBOP'].replace(" ", "")
            if MBOP == rezultArithmet["rb"]:
                countArithmet += 1
                MBOP ="bg-success"
            else:
                MBOP ="bg-danger"
            MCOP = request.form['MCOP'].replace(" ", "")
            if MCOP == rezultArithmet["rcpm"]:
                countArithmet += 1
                MCOP ="bg-success"
            else:
                MCOP ="bg-danger"
            MCOPP = request.form['MCOPP'].replace(" ", "")
            if MCOPP == rezultArithmet["fcpm"]:
                countArithmet += 1
                MCOPP ="bg-success"
            else:
                MCOPP ="bg-danger"

            MADP = request.form['MAOP'].replace(" ", "")
            if MADP == rezultArithmet["aam"]:
                countArithmet += 1
                MADP ="bg-success"
            else:
                MADP ="bg-danger"
            MBDP = request.form['MBDP'].replace(" ", "")
            if MBDP == rezultArithmet["ab"]:
                countArithmet += 1
                MBDP ="bg-success"
            else:
                MBDP ="bg-danger"
            MCDP = request.form['MCDP'].replace(" ", "")
            if MCDP == rezultArithmet["acpm"]:
                countArithmet += 1
                MCDP ="bg-success"
            else:
                MCDP ="bg-danger"
            MCDPP1 = request.form['MCDPP1'].replace(" ", "")
            if MCDPP1 == rezultArithmet["fcpm"]:
                countArithmet += 1
                MCDPP1 ="bg-success"
            else:
                MCDPP1 ="bg-danger"

            MAOM = request.form['MAOM'].replace(" ", "")
            if MAOM == rezultArithmet["ram"]:
                countArithmet += 1
                MAOM ="bg-success"
            else:
                MAOM ="bg-danger"
            MBOM = request.form['MBOM'].replace(" ", "")
            if MBOM == rezultArithmet["rb"]:
                countArithmet += 1
                MBOM ="bg-success"
            else:
                MBOM ="bg-danger"
            MCOM = request.form['MCOM'].replace(" ", "")
            if MCOM == rezultArithmet["rcsm"]:
                countArithmet += 1
                MCOM ="bg-success"
            else:
                MCOM ="bg-danger"
            MCOPM = request.form['MCOPM'].replace(" ", "")
            if MCOPM == rezultArithmet["fcs"]:
                countArithmet += 1
                MCOPM ="bg-success"
            else:
                MCOPM ="bg-danger"

            MADM = request.form['MAOM'].replace(" ", "")
            if MADM == rezultArithmet["aam"]:
                countArithmet += 1
                MADM ="bg-success"
            else:
                MADM ="bg-danger"
            MBDM = request.form['MBDM'].replace(" ", "")
            if MBDM == rezultArithmet["ab"]:
                countArithmet += 1
                MBDM ="bg-success"
            else:
                MBDM ="bg-danger"
            MCDM = request.form['MCDM'].replace(" ", "")
            if MCDM == rezultArithmet["acsm"]:
                countArithmet += 1
                MCDM ="bg-success"
            else:
                MCDM ="bg-danger"
            MCDPM = request.form['MCDPM'].replace(" ", "")
            if MCDPM == rezultArithmet["fcs"]:
                countArithmet += 1
                MCDPM ="bg-success"
            else:
                MCDPM ="bg-danger"

        

        if mulanddiv:
            print(rezultMulAndDiv)
            APMUL = request.form['APMUL'].replace(" ", "")
            print(APMUL)
            if APMUL == rezultMulAndDiv["fa"]:
                print(rezultMulAndDiv["fa"])
                countMulAndDiv += 1
                APMUL ="bg-success"
            else:
                print(APMUL)
                APMUL ="bg-danger"
            BPMUL = request.form['BPMUL'].replace(" ", "")
            if BPMUL == rezult["fb"]:
                count += 1
                BPMUL ="bg-success"
            else:
                BPMUL ="bg-danger"
            CPPMUL = request.form['CPPMUL'].replace(" ", "")
            if CPPMUL == rezult["fcm"]:
                count += 1
                CPPMUL ="bg-success"
            else:
                CPPMUL ="bg-danger"
            AOMUL = request.form['AOMUL'].replace(" ", "")
            if AOMUL == rezult["ra"]:
                count += 1
                AOMUL ="bg-success"
            else:
                print("APMUL")
                AOMUL ="bg-danger"
            BOMUL = request.form['BOMUL'].replace(" ", "")
            if BOMUL == rezult["rb"]:
                count += 1
                BOMUL ="bg-success"
            else:
                BOMUL ="bg-danger"
            COMUL = request.form['COMUL'].replace(" ", "")
            if COMUL == rezult["rc"]:
                count += 1
                COMUL ="bg-success"
            else:
                COMUL ="bg-danger"
            COPMUL = request.form['COPMUL'].replace(" ", "")
            if COPMUL == rezult["fcm"]:
                count += 1
                COPMUL ="bg-success"
            else:
                COPMUL ="bg-danger"
            ADMUL = request.form['ADMUL'].replace(" ", "")
            if ADMUL == rezult["aa"]:
                count += 1
                ADMUL ="bg-success"
            else:
                ADMUL ="bg-danger"
            BDMUL = request.form['BDMUL'].replace(" ", "")
            if BDMUL == rezult["ab"]:
                count += 1
                BDMUL ="bg-success"
            else:
                BDMUL ="bg-danger"
            CDMUL = request.form['CDMUL'].replace(" ", "")
            if CDMUL == rezult["ac"]:
                count += 1
                CDMUL ="bg-success"
            else:
                CDMUL ="bg-danger"
            CDPMUL = request.form['CDPMUL'].replace(" ", "")
            if CDPMUL == rezult["fcm"]:
                count += 1
                CDPMUL ="bg-success"
            else:
                CDPMUL ="bg-danger"
            APDIV = request.form['APDIV'].replace(" ", "")
            if APDIV == rezult["fa"]:
                count += 1
                APDIV ="bg-success"
            else:
                APDIV ="bg-danger"
            BPDIV = request.form['BPDIV'].replace(" ", "")
            if BPDIV == rezult["fb"]:
                count += 1
                BPDIV ="bg-success"
            else:
                BPDIV ="bg-danger"
            CPDIV = request.form['CPDIV'].replace(" ", "")
            if CPDIV == rezult["fcd"]:
                count += 1
                CPDIV ="bg-success"
            else:
                CPDIV ="bg-danger"
            
        
        print("shlyapa")
        file = None
    return render_template('index.html', surname = surname, name = name, otch = otch, grup = grup, time = time, translation = translation, arithmetic = arithmetic, mulanddiv = mulanddiv, A= A, B = B,
 APMUL = APMUL, BPMUL = BPMUL, CPPMUL = CPPMUL, AOMUL = AOMUL, BOMUL = BOMUL, COMUL = COMUL, COPMUL = COPMUL,
 ADMUL = ADMUL, BDMUL = BDMUL, CDMUL = CDMUL, CDPMUL = CDPMUL, APDIV = APDIV, BPDIV=BPDIV, CPDIV = CPDIV, countTranslat = countTranslat, countArithmet = countArithmet, countMulAndDiv = countMulAndDiv,
 AP =AP, AO = AO, AD = AD, BP = BP, BO = BO, BD = BD, APM = APM, AOM = AOM, ADM = ADM, BPM = BPM, BOM = BOM,
 BDM = BDM, APM2 = APM2, AOM2 = AOM2, ADM2 = ADM2, APM3 = APM3, AOM3 = AOM3, ADM3 = ADM3, AP3 = AP3, AO3 = AO3,
 AD3 = AD3, AP4 = AP4, AO4 = AO4, AD4 = AD4, BPM2 = BPM2, BOM2 = BOM2, BDM2 = BDM2, BPM3 = BPM3, BOM3 = BOM3,
 BDM3 = BDM3, BP3 = BP3, BO3 = BO3, BD3 = BD3, BP4 = BP4, BO4 = BO4, BD4 = BD4, 
 AOP = AOP, BOP = BOP, COP = COP, COPP = COPP, ADP = ADP, BDP = BDP, CDP = CDP, CDPP = CDPP, AOS = AOS,
 BOS = BOS, COS = COS, COPS = COPS, ADS = ADS, BDS = BDS, CDS = CDS, CDPS = CDPS, MAOP = MAOP, MBOP = MBOP,
 MCOP = MCOP, MCOPP = MCOPP, MADP = MADP, MBDP = MBDP, MCDP = MCDP, MCDPP1 = MCDPP1, MAOM = MAOM, MBOM = MBOM,
 MCOM = MCOM, MCOPM = MCOPM, MADM = MADM, MBDM = MBDM, MCDM = MCDM, MCDPM = MCDPM, isEnd = isEnd)

   

  
if __name__ == '__main__':
    app.run(debug=True) 