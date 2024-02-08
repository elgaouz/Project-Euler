def comptes_lettre(ch):
    c=0
    for e in ch :
        if (e!="-" and e!=" "):
            c+=1
    return c
ch1="one two three four five six seven eight nine"
ch2="ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen "
ch3="twenty"
ch4="thirty"
ch5="forty"
ch6="fifty"
ch7="sixty"
ch8="seventy"
ch9="eighty"
ch10="ninety"
ch11="one hundred"
ch12="two hundred"
ch13="three hundred"
ch14="four hundred"
ch15="five hundred"
ch16="six hundred"
ch17="seven hundred"
ch18="eight hundred"
ch19="nine hundred"
ch20="and"
r1=comptes_lettre(ch1)+comptes_lettre(ch2)+10*comptes_lettre(ch3)+8*comptes_lettre(ch1)+10*comptes_lettre(ch4)+10*comptes_lettre(ch5)+10*comptes_lettre(ch6)+10*comptes_lettre(ch7)+10*comptes_lettre(ch8)+10*comptes_lettre(ch9)+10*comptes_lettre(ch10)
print(r1)
r2=100*comptes_lettre(ch11)+r1+99*comptes_lettre(ch20)
print(r2)
r3=100*comptes_lettre(ch12)+r1+99*comptes_lettre(ch20)
print(r3)
r4=100*comptes_lettre(ch13)+r1+99*comptes_lettre(ch20)
print(r4)
r5=100*comptes_lettre(ch14)+r1+99*comptes_lettre(ch20)
print(r5)
r6=100*comptes_lettre(ch15)+r1+99*comptes_lettre(ch20)
print(r6)
r7=100*comptes_lettre(ch16)+r1+99*comptes_lettre(ch20)
print(r7)
r8=100*comptes_lettre(ch17)+r1+99*comptes_lettre(ch20)
print(r8)
r9=100*comptes_lettre(ch18)+r1+99*comptes_lettre(ch20)
print(r9)
r10=100*comptes_lettre(ch19)+r1+99*comptes_lettre(ch20)
print(r10)
r11=comptes_lettre("one thousand")
print(r11)
print(r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11)
print(comptes_lettre("one two three four five"))
