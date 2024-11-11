# Paletra Ciep 117

## Instalação
- Instale o python
- Abra o terminal, no Windows, PowerShell

** Todos os comandos devem ser feitos no terminal **

- Crie uma pasta para adcionar todos os projetos.
  - ```shell
        # No windows 
        mkdir c:\workspace      
    ```
     
- Dentro da pasta workspace baixe o projeto no link https://github.com/wt3c/palestra_117 
  - ```shell
        cd c:\workspace 
        git clone https://github.com/wt3c/palestra_117.git
        cd palestra_117
    ```
- crie um ambiente virtual para as bibliotecas do projeto. 
  - https://docs.python.org/pt-br/dev/library/venv.html
    - ```shell
          python -m venv .venv
      ```
- Instale todas as dependencies
  - ```shell
        # Ainda no terminal Windows
        .\.venv\Scripts\activate.bat
        pip install -r requirements.txt        
    ```
- Execute
  - ```shell
        # Ainda no terminal Windows
        cd .\ia_youtube\
        streamlit run .\front.py        
    ```

# Links

- https://github.com/wt3c/palestra_117  
- https://github.com/lucasgrosso/Space
- https://git-scm.com/book/en/v2
- https://docs.python.org/3/
- https://docs.djangoproject.com/en/5.1/
