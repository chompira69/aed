beneficiario = str(input("Ingrese su nombre completo: "))
codigo = str(input("Ingrese su código ICD10, en el formato ´X##.##´: "))
codigo_nro = int(codigo[1] + codigo[2])
porcentaje = int(codigo[4] + codigo[5])
monto_base = int(10000)
monto_fijo = int(25000)
monto_adicional = int()
if codigo[0] == "B" and codigo_nro < 99:
    monto_adicional += 25000
    capitulo = "I. Ciertas enfermedades infecciosas y parasitarias"
elif codigo[0] == "C" and codigo_nro >= 00:
    if codigo[0] == "D" and codigo_nro <= 48:
        monto_adicional += 25000
        capitulo = "II. Tumores [neoplasias]."
elif codigo[0] == "D" and codigo_nro >= 50:
    if codigo[0] == "D" and codigo_nro <= 89:
        monto_adicional += 25000
        capitulo = "III. Enfermedades de la sangre y de los órganos hematopoyéticos, y ciertos trastornos que afectan el mecanismo de la inmunidad."
elif codigo[0] == "E" and codigo_nro >= 00:
    if codigo[0] == "E" and codigo_nro <= 90:
        monto_adicional += 25000
        capitulo = "IV. Enfermedades endocrinas, nutricionales y metabólicas."
elif codigo[0] == "F" and codigo_nro >= 00:
    if codigo[0] == "F" and codigo_nro <= 99:
        monto_adicional += 25000
        capitulo = "V. Trastornos mentales y del comportamiento."
elif codigo[0] == "G" and codigo_nro >= 00:
    if codigo[0] == "G" and codigo_nro <= 99:
        monto_adicional += 25000
        capitulo = "VI. Enfermedades del sistema nervioso."
elif codigo[0] == "H" and codigo_nro >= 00:
    if codigo[0] == "H" and codigo_nro <= 59:
        monto_adicional += 25000
        capitulo = "VII. Enfermedades del ojo y sus anexos."
elif codigo[0] == "H" and codigo_nro >= 60:
    if codigo[0] == "H" and codigo_nro <= 65:
        monto_adicional += 25000
        capitulo = "VIII. Enfermedades del oído y de la apófisis mastoides."
elif codigo[0] == "I" and codigo_nro >= 00:
    if codigo[0] == "I" and codigo_nro <= 99:
        monto_adicional += 25000
        capitulo = "IX. Enfermedades del sistema circulatorio."
elif codigo[0] == "J" and codigo_nro >= 00:
    if codigo[0] == "J" and codigo_nro <= 99:
        monto_adicional += 25000
        capitulo = "X. Enfermedades del sistema respiratorio."
elif codigo[0] == "K" and codigo_nro >= 00:
    if codigo[0] == "K" and codigo_nro <= 93:
        monto_adicional += 25000
        capitulo = "XI. Enfermedades del sistema digestivo."
elif codigo[0] == "L" and codigo_nro >= 00:
    if codigo[0] == "L" and codigo_nro <= 93:
        monto_adicional += 25000
        capitulo = "XII. Enfermedades de la piel y del tejido subcutáneo."
elif codigo[0] == "M" and codigo_nro >= 00:
    if codigo[0] == "M" and codigo_nro <= 99:
        monto_adicional += 40000
        capitulo = "XIII. Enfermedades del sistema osteomuscular y del tejido conjuntivo."
elif codigo[0] == "N" and codigo_nro >= 00:
    if codigo[0] == "N" and codigo_nro <= 99:
        monto_adicional += 40000
        capitulo = "XIV. Enfermedades del sistema genitourinario."
elif codigo[0] == "O" and codigo_nro >= 00:
    if codigo[0] == "O" and codigo_nro <= 99:
        monto_adicional += 40000
        capitulo = "XV. Embarazo, parto y puerperio."
elif codigo[0] == "P" and codigo_nro >= 00:
    if codigo[0] == "P" and codigo_nro <= 96:
        monto_adicional += 40000
        capitulo = "XVI. Ciertas afecciones originadas en el período perinatal."
elif codigo[0] == "Q" and codigo_nro >= 00:
    if codigo[0] == "Q" and codigo_nro <= 99:
        monto_adicional += 40000
        capitulo = "XVII. Malformaciones congénitas, deformidades y anomalías cromosómicas."
elif codigo[0] == "R" and codigo_nro >= 00:
    if codigo[0] == "R" and codigo_nro <= 99:
        monto_adicional += 40000
        capitulo = "XVIII. Síntomas, signos y hallazgos anormales clínicos y de laboratorio, no clasificados en otra parte."
elif codigo[0] == "S" and codigo_nro >= 00:
    if codigo[0] == "T" and codigo_nro <= 98:
        monto_adicional += 40000
        capitulo = "XIX. Traumatismos, envenenamientos y algunas otras consecuencias de causas externas."
elif codigo[0] == "V" and codigo_nro >= 1:
    if codigo[0] == "Y" and codigo_nro <= 98:
        monto_adicional += 40000
        capitulo = "XX. Causas externas de morbilidad y de mortalidad."
elif codigo[0] == "Z" and codigo_nro >= 00:
    if codigo[0] == "Z" and codigo_nro <= 99:
        monto_adicional += 40000
        capitulo = "XXI. Factores que influyen en el estado de salud y contacto con los servicios de salud."
elif codigo[0] == "U" and codigo_nro >= 00:
    if codigo[0] == "U" and codigo_nro <= 99:
        monto_adicional += 100000
        capitulo = "XXII. Códigos para propósitos especiales."
monto_a_pagar = int(input("Ingrese el monto base a pagar por el tratamiento: "))
monto_final = (monto_adicional + monto_base + monto_fijo + monto_a_pagar)
monto_final += (monto_final*porcentaje)/100
print("Beneficiario:", beneficiario)
print("Codigo:", codigo)
print("Capitulo:", capitulo)
print("Monto a pagar:", monto_final)
