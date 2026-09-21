from pathlib import Path
from watchdog.events import FileSystemEventHandler
from organizador import organizar_arquivo
import time
from watchdog.observers import Observer

EXTENSOES_TEMPORARIAS = (
    '.crdownload', 
    '.part',
    '.tmp',
    '.download',
)

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
            
        organizar_arquivo(arquivo, self.pasta_principal)

        print(f'Novo arquivo detectado: {arquivo}')

    def on_moved(self, event):
        if event.is_directory:
            return

        arquivo = Path(event.dest_path)

        if arquivo.parent != self.pasta_principal:
            return

        if arquivo.suffix.lower() not in EXTENSOES_TEMPORARIAS:
            organizar_arquivo(arquivo, self.pasta_principal)


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

        