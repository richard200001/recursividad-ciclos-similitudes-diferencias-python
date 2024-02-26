def longitud_recursividad(num):
  if num>9:
    resultado=num/10
    return 1+longitud_recursividad(resultado)
  else:
    return 1
    
def longitud(num):
  contador=1
  for i in range(num):
    if num>9:
      num=num/10
      contador+=1
  return contador
  
print(longitud_recursividad(10), " longitud_recursividad")
print(longitud(10), " longitud normal")
