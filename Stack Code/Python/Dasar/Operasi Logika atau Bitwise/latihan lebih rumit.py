'''
    Pada program ini saya akan melakukan latihan logika dan komperasi sederhana 
    yang akan memngasah kemampuan anda.

    lathanya adalah:
    membuat Correct pada aturanberikut:
    ++++++3-----6++++++9-----12+++++ and
    ------3+++++6------9+++++12-----  
'''

# baik pertama adalah   ++++++3-----6++++++9-----12+++++ 
Nominal = float(input('Masukan Nominal kurang dari 3 \n atau lebih dari 12 \n dan lebih dari 6 dan \n kurang dari 9 :'))

# +++++3-----
Kurang_3 = Nominal < 3
# -----12+++++
Lebih_dari_12 = Nominal > 12
# -----6+++++
Lebih_dari_6 = Nominal > 6
# +++++9-----
Kurang_9 = Nominal < 9
# Mari kita gabungkan
Correct_1 = Kurang_3 or Lebih_dari_12
Correct_2 = Lebih_dari_6 and Kurang_9

Correct_total = Correct_1 or Correct_2

#Mari print
print (f'Nominal yang anda masukan sangat ', Correct_total )

print ('-' * 10 + 'Masuk ke soal 2' + 10 * '-')

# baik yang kedua adalah ------3+++++6------9+++++12-----
Nominal = float(input('Masukan Nominal kurang dari 3 \n atau lebih dari 12 \n dan lebih dari 6 dan \n kurang dari 9 :'))

# +++++3-----
lebih_dari_3 = Nominal > 3
# -----12+++++
Kurang_6 = Nominal < 6
# -----6+++++
Lebih_dari_9 = Nominal > 9
# +++++9-----
Kurang_12 = Nominal < 12
# Mari kita gabungkan
Correct_1 = lebih_dari_3 and Kurang_6
Correct_2 = Lebih_dari_9 and Kurang_12

Correct_total = Correct_1 or Correct_2

#Mari print
print (f'Nominal yang anda masukan sangat ', Correct_total )

