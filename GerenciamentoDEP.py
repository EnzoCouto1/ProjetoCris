import subprocess
import sys

def instalar_dependencias():
    # Lê o arquivo requirements.txt
    try:
        with open('requirements.txt', 'r') as f:
            dependencias = f.readlines()
        
        # Limpa as dependências removendo espaços em branco extras
        dependencias = [dep.strip() for dep in dependencias if dep.strip()]
        
        if not dependencias:
            print("Não há dependências listadas no arquivo.")
            return
        
        # Instala as dependências utilizando pip
        for dependencia in dependencias:
            print(f"Instalando: {dependencia}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", dependencia])
        
        print("Todas as dependências foram instaladas com sucesso!")

    except FileNotFoundError:
        print("Arquivo requirements.txt não encontrado!")
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao instalar as dependências: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Chama a função para instalar as dependências
if __name__ == "__main__":
    instalar_dependencias()
