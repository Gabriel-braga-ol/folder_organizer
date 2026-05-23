import os
from tkinter.filedialog import askdirectory

"""Abrindo o pop-up e selecionando a pasta"""

caminho = askdirectory(title='Selecione uma pasta') # Pop-up

lista_arquivos = os.listdir(caminho) # Quais arquivos tem no caminho

"""
Criando um dicionário de arquivos
"""

categorias = {
    "PDFs":       [".pdf"],
    "Imagens":    [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Videos":     [".mp4", ".mov", ".avi", ".mkv"],
    "Audios":     [".mp3", ".wav", ".flac", ".aac", ".ogg"],
    "Documentos": [".docx", ".xlsx", ".pptx", ".doc", ".xls", ".odt", ".pptm", ".ppt"],
    "Comprimidos":[".zip", ".rar", ".tar", ".gz", ".7z"],
    "Codigo":     [".py", ".js", ".html", ".css", ".json", ".ts"],
    "Outros":     [".exe", ".csv", ".txt", ".xml", ".kmz", ".m4a", ".ris", ".msi", ".bmp", ".bib"]
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f'{caminho}/{arquivo}') # Extraindo a extensão do arquivo
    for pasta in categorias:
        if extensao in categorias[pasta]: # Se a extensão estiver dentro de alguma pasta em categorias, faça algo
            if not os.path.exists(f'{caminho}/{pasta}'): # Se a pasta não existe no caminho
                os.mkdir(f'{caminho}/{pasta}') # Criando a pasta
            os.rename(f'{caminho}/{arquivo}', f'{caminho}/{pasta}/{arquivo}') # Renomeando pasta

