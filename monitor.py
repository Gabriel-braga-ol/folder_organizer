import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from organizador import organizar_arquivo, EXTENSOES_TEMPORARIAS

class OrganizadorHandler(FileSystemEventHandler):
    def __init__(self, pasta_principal):
        super().__init__()
        self.pasta_principal = pasta_principal


    def on_created(self, event):
        if event.is_directory:
            return

        arquivo = Path(event.src_path)

        extensao = arquivo.suffix.lower()
        if extensao in EXTENSOES_TEMPORARIAS:
            print(f"O Arquivo temporário {arquivo.name} será ignorado")
            return

        if not aguardar_arquivo_estavel(arquivo):
            print(f"Arquivo ainda não está disponível: {arquivo.name}")
            return
            
        destino = organizar_arquivo(arquivo, self.pasta_principal)

        if destino is not None:
            print(f'{arquivo.name} organizado em : {destino}')


    def on_moved(self, event):
        if event.is_directory:
            return

        arquivo = Path(event.dest_path)

        if arquivo.parent != self.pasta_principal:
            return

        if arquivo.suffix.lower() in EXTENSOES_TEMPORARIAS:
            return
        
        if not aguardar_arquivo_estavel(arquivo):
            print(f"Não foi possível processar {arquivo.name}")
            return

        destino = organizar_arquivo(arquivo, self.pasta_principal)

        if destino is not None:
            print(f"Arquivo movido com sucesso: {arquivo.name} -> {destino}")


def monitorar_pasta(pasta_principal):
    handler = OrganizadorHandler(pasta_principal)

    observer = Observer()

    observer.schedule(handler, path=str(pasta_principal), recursive=False)

    observer.start()
    print(f'A pasta {pasta_principal} está sendo monitorada. Pressione Ctrl + C para encerrar o programa.')

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print('Encerrando o programa')

    finally:
        observer.stop()
        observer.join()
        print('Monitoramento finalizado.')


def aguardar_arquivo_estavel(arquivo, tentativas=30, intervalo=1):

    caminho = Path(arquivo)

    tamanho_anterior = None
    qtd_verificacoes_estaveis = 0

    for _ in range(tentativas):
        if not caminho.exists():
            return False

        try:
            tamanho_atual = caminho.stat().st_size
        except OSError:
            time.sleep(intervalo)
            continue

        if tamanho_atual == tamanho_anterior:
            qtd_verificacoes_estaveis += 1
        else:
            qtd_verificacoes_estaveis = 0
            tamanho_anterior = tamanho_atual

        if qtd_verificacoes_estaveis >= 3:
            return True

        time.sleep(intervalo)

    return False