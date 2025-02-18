'''Mari kita coba casting yang benar'''
#ini adalah tipe data String
print ('====STRING====')
Data_str = '10'
print ('Data:', Data_str)
print('Tipe:', type(Data_str))

Data_int     = int (Data_str) # Variabel Data_str tidak bisa di casting ke tipe Interger
Data_float   = float (Data_str) # Variabel Data_str tidak bisa di casting ke tipe float 
Data_boolean = bool (Data_str)

print ('Data:', Data_int, 'type:', type(Data_int))
print ('Data:', Data_float, 'type:', type(Data_float))
print ('Data:', Data_boolean, 'type:', type(Data_boolean))


#ini adalah tipe data Interger
print ('====INTERGER====')
Data_int = 10
print ('Data:', Data_int)
print ('Tipe:', type(Data_int))

Data_STR     = str (Data_int)
Data_float   = float (Data_int)
Data_boolean = bool (Data_int)

print ('Data:', Data_str, 'type:', type(Data_str))
print ('Data:', Data_float, 'type:', type(Data_float))
print ('Data:', Data_boolean, 'type:', type(Data_boolean))

#ini adalah tipe data float
print ('====FLOAT====')
Data_float = 1.6
print ('Data:', Data_float)
print ('Tipe:', type(Data_float))

Data_str     = str (Data_float)
Data_int     = int (Data_float)
Data_boolean = bool (Data_float)

print ('Data:', Data_str, 'type:', type(Data_str))
print ('Data:', Data_int, 'type:', type(Data_int))
print ('Data:', Data_boolean, 'type:', type(Data_boolean))

#ini adalah tipe data Boolean
print ('====BOOLEAN====')
Data_Boolean = True
print ('Data:', Data_Boolean)
print ('Tipe:', type(Data_Boolean))

Data_str     = str (Data_Boolean)
Data_int     = int (Data_Boolean)
Data_float   = float (Data_Boolean)

print ('Data:', Data_str, 'type:', type(Data_str))
print ('Data:', Data_int, 'type:', type(Data_int))
print ('Data:', Data_float, 'type:', type(Data_float))
