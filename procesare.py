import json
cal = 1800
fbf = open('bf.json')
dict_bf = json.load(fbf)
flun = open('lunch.json')
dict_lun = json.load(flun)
fdin = open('dinner.json')
dict_din = json.load(fdin)
d_fin_bf = []
d_fin_lun = []
d_fin_din = []
rez = ''
lis_rez = []


def elim_elem_goale(dictvechi, dictnou):
    for i in range(len(dictvechi)):
        if len(dictvechi[i]['info']) != 0:
            dictnou.append(dictvechi[i])


def pregatire():
    elim_elem_goale(dict_bf, d_fin_bf)
    elim_elem_goale(dict_lun, d_fin_lun)
    elim_elem_goale(dict_din, d_fin_din)


def valoare(segment):
    val = ''
    for let in segment:
        if ord(let) != 103:
            val += let
    return int(val)


def verificare_proportii(total, prot, carb, fat):
    prot *= 100
    carb *= 100
    fat *= 100
    if (carb/total in range(45, 65)) & (prot/total in range(10, 35)) & (fat/total in range(20, 60)):
        return True
    else:
        return False
      


def gasire_combinatii(cal):
    pregatire()
    contor = 0
    for i in range(len(d_fin_bf)):
        for j in range(len(d_fin_lun)):
            for k in range(len(d_fin_din)):
                suma_cal_elem = (int(d_fin_bf[i]['info'][0]) + int(d_fin_lun[j]['info'][0]) + int(d_fin_din[k]['info'][0]))
                p_tot = (valoare(d_fin_bf[i]['info'][6]) + valoare(d_fin_lun[j]['info'][6]) + valoare(d_fin_din[k]['info'][6]))
                f_tot = (valoare(d_fin_bf[i]['info'][2]) + valoare(d_fin_lun[j]['info'][2]) + valoare(d_fin_din[k]['info'][2]))
                c_tot = (valoare(d_fin_bf[i]['info'][4]) + valoare(d_fin_lun[j]['info'][4]) + valoare(d_fin_din[k]['info'][4]))
                cal_p = p_tot * 4
                cal_f = f_tot * 9
                cal_c = c_tot * 4
                tot = cal_c + cal_f + cal_p
                if verificare_proportii(tot, cal_p, cal_c, cal_f):
                    lis_rez.append(d_fin_bf[i]['url'])
                    lis_rez.append(d_fin_lun[j]['url'])
                    lis_rez.append(d_fin_din[k]['url'])
                    if cal - suma_cal_elem > 75:
                        lis_rez.append(cal / suma_cal_elem)
    return(formatare_raspuns(rez))
    
    

def formatare_raspuns(rez):
    cont = 1
    for nr in range(len(lis_rez)):
        if (nr+1)%4 == 0:
            rez += "\n(Inmultiti cu "
            rez += str(lis_rez[nr])
            rez += " pentru caloriile dorite.)\n\n\n\n\n"
        elif (nr+1)%4 == 1:
            rez += "\n                                     Optiune "
            rez += str(cont)
            rez += ":                               \n\nMic dejun: "
            rez += lis_rez[nr]
            rez+= "\n"
            cont += 1
        elif(nr+1)%4 == 2:
            rez += '\nPranz: '
            rez += lis_rez[nr]
            rez += '\n'
        elif(nr+1)%4 == 3:
            rez += '\nCina: '
            rez += str(lis_rez[nr])
            rez += '\n'
    return(rez)    


  

def main():
    gasire_combinatii(cal)



if __name__ == '__main__':
    main()
