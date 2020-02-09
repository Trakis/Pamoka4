produktai=['Agurotis','Burokas','Duona','Citrina']
print('Produktai pries rusiavima: ',produktai)

temp=produktai[2]
produktai[2]=produktai[3]

produktai[3]=temp

print('Produktai pries rusiavima: ',produktai)