import openpyxl

# crear un nuevo libro de trabajo
workbook = openpyxl.Workbook()

# seleccionar la hoja de trabajo activa
worksheet = workbook.active

# agregar datos a la hoja de trabajo
worksheet['A1'] = 'Nombre'
worksheet['B1'] = 'Edad'
worksheet['A2'] = 'Juan'
worksheet['B2'] = 25

# guardar el libro de trabajo como un archivo xlsx
workbook.save('ejemplo.xlsx')