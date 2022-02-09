import pdfplumber


def parsear_pdf(archivo_pdf: str) -> set:
    """
    Recibe un .pdf (su path) y se queda solo con las líneas que contienen alguna
    palabra dentro de la variable "DICCIO"

    Args:
        archivo_pdf (str): path del archivo pdf

    Returns:
        set: líneas importantes a interpretar posteriormente
    """

    DICCIO = ['registró', 'registra', 'caso importado', 'confirmado',
              'confirmados', 'nuevos casos']

    with pdfplumber.open(archivo_pdf) as pdf:

        for page in pdf.pages:
            text = page.extract_text()

            lineas = text.strip().split('\n')
            lineas_utiles = {
                linea for linea in lineas for palabra in DICCIO if palabra in linea}

    return lineas_utiles


if __name__ == '__main__':

    archivo_pdf = 'Data/5-03-2020-nuevo-coronavirus-covid-19-reporte-diario_1.pdf'
    datos = parsear_pdf(archivo_pdf)
    print(datos)
