'''
Dengan hint memudahkan dalam mendefenisikan input tanpa emrubah 
sipat data sehingga kita tak melupakan
'''
def string (nama:str)->str: # ini adalah hint
    return nama[::-1]
namanya = 'milaS ruN'
print (string (namanya))
