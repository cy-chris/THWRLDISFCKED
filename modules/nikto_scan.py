import subprocess

def run(url):
    print(f"[+] Executando Nikto em {url}...")
    comando = f"nikito -h {url}"
    resultado = subprocess.getoutput(comando)
    
    with open("output/resultado.txt", "a") as f:
        f.write("\n\n--- Nikito ---\n")
        f.write(resultado)
        
    print(resultado)
    input("\n[+] Nikito concluido. Pressione Enter para continuar...")
    