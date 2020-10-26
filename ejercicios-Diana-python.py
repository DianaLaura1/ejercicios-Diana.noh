import re

texto=""" En 1945 en Estados unidos un grupo de jovenes conformado por  lunga1212@aplica.com aristeo@mogurl.com "desarrollaron"
una aplicación llamada radax el cual seria para la marina , el desarrollo de esta aplicación fueron implementadas direcciones 
ips como son las 225.225.225.225 , que son para pc al igual que Mchos otros como 192.168.12.1 192.168.11.34  asi mismo se dice
que fue dado a conocer en una zona Mlitar   https://zonaz.com alrededor de 12:45 Am a 2:30 pm , en la "conferencia" con el 
secretario de defensa se dio a conocer la pagina oficial  https://radax.copaninli.com   al termino de la conferencia los jovenes
proporcionaron sus numeros telefonicos 985-234-34-54 985-543-54-12  y su codigo postal 76543 76543  """



print("--------------1-TODAS LAS PALABRAS QUE TENGAN UNA LONGUITUD DE 7 O MÁS LETRAS-------------------")
longitud=r"\b[a-zA-Z]{7,}\b"                    
buscar=re.findall(longitud,texto)
print(buscar)


print("--------------2-EXPRESIONES QUE NO FINALICEN EN UNA VOCAL-----------------------")
expresiones= r"[a-zA-Záéíóú]{1,}[^aeiouAEIOU\s/W]\b"  
exp=re.findall(expresiones,texto)
print(exp)


print("--------------3-PALABRAS QUE INICIEN CON M DONDE LA SEGUNDA PALABRA NO SEA VOCAL-----------------------")
palabras= r"[M][^aeiouáéíóú]\w{1,}"  
pal=re.findall(palabras,texto)
print(pal)


print("--------------4.EXPRESIONES ENCERRADAS ENTRE COMILLAS-----------------------")
encerradas= r"(\"[\w\s]+\")"  
encerra=re.findall(encerradas,texto)
print(encerra)


print("--------------5-IP´S-----------------------")
encerradas= r"[0-9]{1,}\.[0-9]{1,}\.[0-9]{1,}\.[0-9]{1,}"  
encerra=re.findall(encerradas,texto)
print(encerra)


print("--------------6-HORAS-----------------------")
horas= r"[0-9]{1,}\:[0-9]{1,}\s[aA|Pp][Mm]"  
hor=re.findall(horas,texto)
print(hor)


print("--------------7-TELEFONOS-------------------")
telefono = r"\d{3}[\s-]\d{3}[\s-]\d{2}[\s-]\d{2}"
coincidencia=re.findall(telefono,texto)
print(coincidencia)


print("-----------------------8-CORREOS ELECTRONICOS-----------------------------")
correo=r"[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}"
encontrar=re.findall(correo,texto)
print(encontrar)


print("--------------9-URL´S-----------------------")
urls= r"https://+\w+[.]\w+"  
ur=re.findall(urls,texto)
print(ur)


print("--------------1O-CÓDIGO POSTAL-------------------")
postal = r"\d{5}"
busc=re.findall(postal,texto)
print(busc)
