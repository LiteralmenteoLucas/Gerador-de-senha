from datetime import datetime
import os

def export_output(output):
    # Define o diretório onde os arquivos serão salvos
    directory = "Senhas_geradas"
    
    # Cria o diretório se ele não existir
    os.makedirs(directory, exist_ok=True)
    
    # Gera um nome de arquivo com timestamp para evitar sobrescrita
    filename = os.path.join(directory, f"output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
    
    # Salva o conteúdo do output no arquivo
    with open(filename, "w") as file:
        file.write(str(output))
    
    print(f"Output salvo em: {filename}")
