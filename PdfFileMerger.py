
# Instructions:
    #1- Paste the scrip in the folder where are the files to be merged
    #2- Paste the folder's link in the funtion



import PyPDF2
import os


def merge_PDF(folder):
    
    # Get names from files
    lista=[]
    
    directorio = folder
    archivos = os.listdir(directorio)
    for archivo in archivos:
        lista.append(archivo)
    lista=lista[:len(lista)-1]
    print(lista)
    
    # Merged files  
    nombre_salida = 'merged_PDF.pdf'
    pdf_final = PyPDF2.PdfMerger()
    for nombre_archivo in lista:
         pdf_final.append(nombre_archivo)

    pdf_final.write(nombre_salida)


# Ingresa el path donde esten los archivos
# Funtion:
merge_PDF(r'C:\Users\hp\Documents\Certificados\DataCamp')

