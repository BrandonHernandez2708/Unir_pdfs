import os 
import fitz
def unir_pdf(carpeta_entrada,archivo_salida):
    pdf_unido = fitz.open()
    for nombre_archivo in os.listdir(carpeta_entrada):
        if nombre_archivo.endswith('.pdf'):
            ruta_archivo = os.path.join(carpeta_entrada, nombre_archivo)
            pdf = fitz.open(ruta_archivo)
            pdf_unido.insert_pdf(pdf)
            pdf.close()

#Guardar el pdf
    pdf_unido.save(archivo_salida)
    pdf_unido.close()

carpeta_entrada = "pdf"

archivo_salida=input("Ingrese el nombre del archivo de salida (con extensión .pdf): ")
unir_pdf(carpeta_entrada,archivo_salida)
print("Los PDF han sido unidos correctamente")