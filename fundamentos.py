#variables 
# name = "josefino"

# last_name = "primero"

# #print (last_name)


# #operatores matemáticos 

# num1 = 10

# num2 = 5

# suma = num1 + num2

# resta = num1 - num2

# multiplicacion = num1 * num2

# division = num1 / num2


#print (suma)

#print (resta)

#print (multiplicacion)

#print (division)


#print (f "El resultado de la suma es: {suma}")

#print (f "El resultado de la resta es: {resta}")

#print (f "El resultado {multiplicacion}")

#print (f "El resultado  {division}")





#operaores de comparación

#mayor que >

#menor que <

#mayor o igual que >=

#menor o igual que <=

#igual? ==

#diferente? !=


3>2

# print(num1>num2)

# print(num1<=num2)

# print(num1==num2)

# print(num1!=num2)


#condicionales 


# if num1 > num2:

#     print(f"{num1} es mayor que {num2}")

#     if num2 > num1:

#     print(f"{num1} es mayor que {num2}")

# else:

#     print(f"{num2} es menor que {num1}")    

#condisionles anidados

# edad = 19
# genero = "mujer"
# dia = "jueves"

# if edad >= 18:

#     if genero == "muejer":
         
#          if dia == "jueves ":
              
#         print("puedes pasar")
    
#             else:
    
#             if genero == "mujer":

#         print("puedes pasar")

#     else:

#         print("no puedes pasar solo mujeres")
# else:
#     print("no puedes pasar")


# if edad > 18 and(genero == "mujer" ) and ((dia == "jueves") or (dia == "sabado")): 

#     print("puedes pasar")
# else:
#     print("no puedes pasar")    


#condicionales encadenados, para idnetificar le fin de semana 

# priedra papel o tijera

# player1 = "tijera"
# player2 = " papel"
# player3 = "piedra"

# if player1 == "tijera" and player2 == "papel":

#     print ("player1 gana")

# elif player1 == "papel" and player2 == "piedra":

#     print ("player1 gana")

# elif player1 == "piedra" and player2 == "tijera":

#     print ("player1 gana")

# elif player1 == "tijera" and player2 == "piedra":

#     print ("player2 gana")

# else: 
    
#     print("empate")

#es estructura de datos
name_list = ["josefino", "primero", " segundo", "tersero ", "cuarto"]
age_list = [19, 20, 21, 22, 23]
weight_list = [6.0, 7.0, 8.0, 90, 10.0]

name_list2 = [
                "josefino",
                "primero",
                " segndo ",
                " tersero ",
            ]


# #agregar elementos a la lista

# # name_list.append("cuarto")

# # print(len(name_list))

# print(name_list[-1])

# # cambiar el vaalor de el primer valor de la laista
# name_list[0] = "ruperto "

# #tuplas 
#             name_tuple = ("josefino", 
#                           "primero", 
#                           "segundo", 
#                           "tercero", 
#                           "cuarto",
#                           )

# print(name_tuple[0]) 
#discdionario 

name_dict = {
    
    "name": "josefino",
    "last_name": "primero",
    "age": 19,
    "weight": 6.0,
    "favorite_foods": ["pizza", "hamburguesa", "tacos"],
    "adress": {
        "street": "calle 123",
        "city": "lecheria",
        "country": " venezuela",
    }
}

# print(name_dict["adress"][city]) #lecheria
#print[name_dict["favorite_foods"][0]) #pizza

#BUCLES 
# for name in name_list:

#     if name == "segundo":
#         print(f"hola {name}")



for i in range(len (name_list)):
    print(f"hola {name_list[i]}")
