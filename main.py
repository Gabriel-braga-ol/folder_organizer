import os
from pathlib import Path

# Define o caminha da pasta
caminho = Path.home() / "Downloads"

# Percorre os itens diretamente dentro da pasta Downloads
for item in caminho.iterdir():
    if item.is_file(): 
        extensao = item.suffix.lower()
        print(extensao)

def encontrar_categoria(extensao):

    extensao_lower = extensao.lower() 

    categorias = {
        "PDFs":       [".pdf"],
        "Imagens":    [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
        "Videos":     [".mp4", ".mov", ".avi", ".mkv"],
        "Audios":     [".mp3", ".wav", ".flac", ".aac", ".ogg"],
        "Documentos": [".docx", ".xlsx", ".pptx", ".doc", ".xls", ".odt", ".pptm", ".ppt"],
        "Comprimidos":[".zip", ".rar", ".tar", ".gz", ".7z"],
        "Codigo":     [".py", ".js", ".html", ".css", ".json", ".ts"],
    }

    for categoria, extensoes in categorias.items():
        if extensao_lower in extensoes:
            return categoria

    return "Outros"

def organizar_arquivo(arquivo, pasta_principal):
    if arquivo.is_file():
        extensao_arquivo = arquivo.suffix.lower()

        categoria = encontrar_categoria(extensao_arquivo)

        pasta_destino = pasta_principal / categoria

        pasta_destino.mkdir(parents=True, exist_ok=True)

        caminho_final = pasta_destino / arquivo.name

        caminho_disponivel = gerar_caminho_disponivel(caminho_final)
        
        arquivo.rename(caminho_disponivel)

def gerar_caminho_disponivel(caminho):
    if not caminho.exists():
        return caminho
    
    cont = 1
    
    while True:
        novo_nome = f"{caminho.stem} ({cont}){caminho.suffix}"
        candidato = caminho.parent / novo_nome

        if not candidato.exists():
            return candidato
        
        cont += 1

def organizar_pasta(pasta_principal):
    for item in pasta_principal.iterdir():
        if item.is_file():
            organizar_arquivo(item, pasta_principal)




# for arquivo in lista_arquivos:
#     nome, extensao = os.path.splitext(f'{caminho}/{arquivo}') # Extraindo a extensão do arquivo
#     for pasta in categorias:
#         if extensao in categorias[pasta]: # Se a extensão estiver dentro de alguma pasta em categorias, faça algo
#             if not os.path.exists(f'{caminho}/{pasta}'): # Se a pasta não existe no caminho
#                 os.mkdir(f'{caminho}/{pasta}') # Criando a pasta
#             os.rename(f'{caminho}/{arquivo}', f'{caminho}/{pasta}/{arquivo}') # Renomeando pasta

