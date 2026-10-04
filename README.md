📚 Sistema de Gerenciamento de Biblioteca em Python



Este projeto é uma aplicação simples desenvolvida em Python 3 para o gerenciamento de acervo de uma biblioteca e visualização gráfica de dados de estoque por gênero utilizando a biblioteca Matplotlib.



Proposto como atividade prática de programação, o sistema abrange conceitos de Orientação a Objetos (POO), manipulação de estruturas de dados (listas e dicionários) e geração de gráficos estatísticos.



🚀 Funcionalidades



Cadastrar Livro: Permite adicionar novos livros ao sistema informando Título, Autor, Gênero e Quantidade disponível.



Listar Livros: Exibe todos os livros cadastrados e suas respectivas informações de estoque.



Buscar por Título: Busca no acervo livros cujo título coincida parcialmente ou totalmente com o termo pesquisado.



Gráfico por Gênero: Gera um gráfico de barras dinâmico com a quantidade acumulada de livros cadastrados por gênero.



🛠️ Tecnologias Utilizadas



Linguagem: Python 3



Visualização de Dados: Matplotlib



Ambiente de Execução: Google Colab / VS Code



📁 Estrutura do Código



O projeto está contido no arquivo main.py e organizado da seguinte forma:



Classe Livro: Define a estrutura e os atributos dos livros (titulo, autor, genero, quantidade).



Lista biblioteca: Estrutura global para armazenamento dinâmico das instâncias.



Funções Principais:



cadastrar\_livro()



listar\_livros()



buscar\_livro\_por\_titulo()



gerar\_grafico\_genero()



Execução de Testes: Bloco principal com inserção de dados de exemplo e execução das funcionalidades.



💻 Como Executar o Projeto Localmente



Pré-requisitos



Certifique-se de ter o Python 3 e a biblioteca Matplotlib instalados em sua máquina:



pip install matplotlib





Passo a passo



Clone o repositório:



git clone https://github.com/patricia661/gerenciamento-biblioteca-python.git





Acesse a pasta do projeto:



cd gerenciamento-biblioteca-python





Execute o arquivo principal:



python main.py





📊 Exemplo de Saída (Gráfico de Barras)

![Gráfico por Gênero](grafico.png)

O gráfico gerado pelo Matplotlib exibe no eixo X os gêneros literários cadastrados e no eixo Y o volume total de exemplares disponíveis em estoque.



👤 Autora



Desenvolvido por Patrícia



🔗 GitHub Profile

