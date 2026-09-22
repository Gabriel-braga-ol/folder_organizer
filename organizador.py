from pathlib import Path

EXTENSOES_TEMPORARIAS = (
    '.crdownload', 
    '.part',
    '.tmp',
    '.download',
)

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
    if not arquivo.is_file():
        return None
    
    extensao_arquivo = arquivo.suffix.lower()

    if extensao_arquivo in EXTENSOES_TEMPORARIAS:
        return None
    
    categoria = encontrar_categoria(extensao_arquivo)

    pasta_destino = pasta_principal / categoria

    try:
        pasta_destino.mkdir(parents=True, exist_ok=True)
        caminho_final = pasta_destino / arquivo.name
        caminho_disponivel = gerar_caminho_disponivel(caminho_final)
        arquivo.rename(caminho_disponivel)

        return caminho_disponivel

    except OSError as erro:
        print(f"Não foi possível organizar {arquivo.name}: {erro}")
        return None

        
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

