import matplotlib.pyplot as plt

# ==========================================================
# Passo 1: Definir a classe Livro
# ==========================================================
class Livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

    def __str__(self):
        return f"Título: {self.titulo} | Autor: {self.autor} | Gênero: {self.genero} | Qtd: {self.quantidade}"


# ==========================================================
# Passo 2: Criar a lista de livros
# ==========================================================
biblioteca = []


# ==========================================================
# Passo 3: Implementar funções para gerenciar os livros
# ==========================================================

def cadastrar_livro(titulo, autor, genero, quantidade):
    """Cadastra um novo livro na lista da biblioteca."""
    novo_livro = Livro(titulo, autor, genero, quantidade)
    biblioteca.append(novo_livro)
    print(f"Livro '{titulo}' cadastrado com sucesso!")

def listar_livros():
    """Lista todos os livros disponíveis na biblioteca."""
    if not biblioteca:
        print("Nenhum livro cadastrado na biblioteca.")
        return
    
    print("\n--- LISTA DE LIVROS ---")
    for livro in biblioteca:
        print(livro)
    print("-----------------------\n")

def buscar_livro_por_titulo(titulo_busca):
    """Busca um livro pelo seu título (não sensível a maiúsculas/minúsculas)."""
    encontrados = [livro for livro in biblioteca if titulo_busca.lower() in livro.titulo.lower()]
    
    if encontrados:
        print(f"\n--- Livros encontrados com '{titulo_busca}' ---")
        for livro in encontrados:
            print(livro)
        print("--------------------------------------------------\n")
    else:
        print(f"\nNenhum livro encontrado com o título: '{titulo_busca}'\n")


# ==========================================================
# Passo 4: Utilizar a biblioteca Matplotlib para gerar um gráfico
# ==========================================================

def gerar_grafico_genero():
    """Gera um gráfico de barras com a quantidade total de livros por gênero."""
    if not biblioteca:
        print("Não há livros cadastrados para gerar o gráfico.")
        return
    
    # Agrupando as quantidades por gênero
    qtd_por_genero = {}
    for livro in biblioteca:
        genero = livro.genero
        qtd_por_genero[genero] = qtd_por_genero.get(genero, 0) + livro.quantidade

    generos = list(qtd_por_genero.keys())
    quantidades = list(qtd_por_genero.values())

    # Criando o gráfico de barras
    plt.figure(figsize=(8, 5))
    plt.bar(generos, quantidades, color='skyblue', edgecolor='black')
    plt.title('Quantidade Total de Livros por Gênero')
    plt.xlabel('Gênero')
    plt.ylabel('Quantidade de Livros')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Exibe o gráfico
    plt.show()


# ==========================================================
# Passo 5: Testar o sistema
# ==========================================================

if __name__ == "__main__":
    # 1. Cadastrando livros de teste
    cadastrar_livro("Dom Casmurro", "Machado de Assis", "Romance", 5)
    cadastrar_livro("O Hobbit", "J.R.R. Tolkien", "Fantasia", 8)
    cadastrar_livro("1984", "George Orwell", "Ficção Científica", 4)
    cadastrar_livro("Orgulho e Preconceito", "Jane Austen", "Romance", 3)
    cadastrar_livro("Duna", "Frank Herbert", "Ficção Científica", 6)

    # 2. Listando todos os livros
    listar_livros()

    # 3. Buscando um livro
    buscar_livro_por_titulo("1984")

    # 4. Gerando o gráfico por gênero
    gerar_grafico_genero()
