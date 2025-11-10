📝 Lista de Tarefas (To-Do List)

![ScreenShot do programa](Captura de tela 2025-11-19 101919.png)

Uma aplicação de desktop simples e moderna para gerenciamento de tarefas, desenvolvida em Python. Este projeto utiliza o CustomTkinter para garantir uma interface visual limpa e a capacidade de alternar entre temas claro/escuro (embora o tema escuro esteja definido por padrão).

O aplicativo salva automaticamente suas tarefas em um arquivo local, garantindo que você nunca perca seu progresso.

✨ Funcionalidades Principais

Adicionar Tarefa: Insira novas tarefas na lista com um clique.

Excluir Tarefa: Selecione e remova tarefas concluídas ou indesejadas.

Persistência de Dados: Todas as tarefas são salvas automaticamente no arquivo lista.txt ao fechar o aplicativo e recarregadas ao iniciar.

Design Moderno: Interface de usuário construída com CustomTkinter, oferecendo uma estética aprimorada em relação ao Tkinter padrão.

Alertas: Uso de caixas de diálogo (messagebox) para feedback imediato ao usuário (sucesso na adição/exclusão).

🛠️ Tecnologias Utilizadas

Python 3.x

CustomTkinter: Biblioteca GUI moderna baseada em Tkinter.

Execução (Versão Final)

Esta aplicação foi empacotada em um executável autônomo. Não é necessário ter o Python instalado no seu computador para rodá-lo.

Baixe o executável (app.exe ou app) fornecido.

Navegue até o local onde o arquivo foi baixado.

Clique duas vezes no executável para iniciar o aplicativo.

Nota sobre o Ícone: O aplicativo tenta carregar um ícone chamado RatDev.ico. Se você não tiver este arquivo na mesma pasta do executável, ele será executado, mas com o ícone padrão do sistema operacional.

🚀 Como Usar a Lista

Adicionar: Digite a tarefa no campo de entrada e clique no botão "Adicionar Tarefa".

Excluir: Clique em uma tarefa na lista para selecioná-la. Em seguida, clique no botão "Excluir Tarefa".

Salvar: O aplicativo salva automaticamente o estado da lista sempre que você fecha a janela.

📦 Para Desenvolvedores: Criação do Executável

Se você deseja gerar a sua própria versão executável a partir do código fonte, siga estes passos:

Instale o PyInstaller:

pip install pyinstaller


Execute este comando na pasta raiz do projeto. Ele criará um executável de arquivo único e incluirá os arquivos de dados necessários:

pyinstaller --noconsole --onefile --icon=RatDev.ico --add-data "lista.txt:." RatList.py


O arquivo executável final (ex: app.exe ou app) será gerado dentro da pasta dist.

⚙️ Estrutura do Código

O projeto está contido em um único arquivo Python, o que facilita a distribuição e o entendimento.

Arquivo

Descrição

RatList.py

Contém toda a lógica da GUI (CustomTkinter), as funções de persistência de arquivo e o controle da aplicação.

lista.txt

Arquivo gerado automaticamente que armazena as tarefas.

RatDev.ico

Arquivo de ícone referenciado.

🤝 Contribuições

Sinta-se à vontade para sugerir melhorias, como a adição de datas de vencimento ou um sistema de prioridades!

Feito com 💙 por [rataria-dev/GitHub User]
