# TableResponsivePyQt6

TableResponsivePyQt6 é um projeto em Python que utiliza PyQt6 e Pandas para criar uma interface de tabela responsiva. Esta tabela pode exibir e atualizar informações dinamicamente a partir de um arquivo CSV com base em diferentes status.

## Funcionalidades

- **Design Responsivo**: A tabela ajusta sua aparência com base no conteúdo e no tamanho da janela.
- **Filtros de Status**: Botões para filtrar e exibir dados com base em vários status, como "Em Aberto", "Em Produção", "Em Separação", "Em Trânsito", "Entregue" e "Cancelado".
- **Estilo Dinâmico**: As linhas na tabela são estilizadas dinamicamente para melhor legibilidade.

## Requisitos

- Python 3.x
- PyQt6
- Pandas

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/L30NARDO-N0GU31RA/TableResponsivePyQt6.git
    cd TableResponsivePyQt6
    ```

2. Crie um ambiente virtual e ative-o (opcional, mas recomendado):
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale os pacotes necessários:
    ```sh
    pip install pyqt6 pandas
    ```

## Uso

1. Certifique-se de que você tem seu arquivo de dados CSV (`DADOS.csv`) e seu arquivo de estilos JSON (`STYLESHEETS_BUTTONS.json`) no mesmo diretório do seu script.

2. Execute a aplicação:
    ```sh
    python main.py
    ```

3. A janela da aplicação será aberta, exibindo a tabela com os dados filtrados pelo status padrão ("Em Aberto").

## Estrutura de Arquivos

- **main.py**: O ponto de entrada principal da aplicação.
- **GIT_TABLE.ui**: O arquivo de interface gerado pelo Qt Designer.
- **DADOS.csv**: O arquivo CSV contendo os dados a serem exibidos.
- **STYLESHEETS_BUTTONS.json**: O arquivo JSON contendo os estilos para os botões.