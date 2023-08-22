# Nama : Marsello Ormanda
# :))))

data_udin = [78, 95, 1.69, 1.88]
data_nanang = [92, 85, 1.95, 1.76]

udin1 = data_udin[0] / (data_udin[2]**2)
bmi_udin1 = round(udin1,1)
udin2 = data_udin[1] / (data_udin[3]**2)
bmi_udin2 = round(udin2,1)

nanang1 = data_nanang[0] // (data_nanang[2]**2)
bmi_nanang1 = round(nanang1,1)
nanang2 = data_nanang[1] // (data_nanang[3]**2)
bmi_nanang2 = round(nanang2,1)

tinggi_udin1 = data_udin[2]
tinggi_udin2 = data_udin[3]

tinggi_nanang1 = data_nanang[2]
tinggi_nanang2 = data_nanang[3]

banding_bmi1 = bmi_udin1 > bmi_nanang1
banding_bmi2 = bmi_udin2 > bmi_nanang2

print("========================================================")
print("Hasil Perbandingan Data 1 : ")
if banding_bmi1 == True:
    print("BMI Udin ", "(", bmi_udin1,")"," lebih tinggi dari Nanang ","(",bmi_nanang1,")")
else:
    print("BMI Udin ", "(", bmi_udin1,")"," lebih rendah dari Nanang ","(",bmi_nanang1,")")

print("-------------------------------------------")

print("Hasil Perbandingan Data 2 : ")
if banding_bmi2 == True:
    print("BMI Udin ", "(", bmi_udin2,")"," lebih tinggi dari Nanang ","(",bmi_nanang2,")")
else:
    print("BMI Udin ", "(", bmi_udin2,")"," lebih rendah dari Nanang ","(",bmi_nanang2,")")


print("========================================================")
    
    
    
    
    