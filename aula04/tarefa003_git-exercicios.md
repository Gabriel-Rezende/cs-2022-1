### Tarefa 003: Git Exercícios - 03/06/2021.

Responda as questões abaixo (exercite os comandos do git correspondentes). Lembre-se de que o “interessante” não é exatamente o conjunto de respostas, mas o processo de obtê-las e a experiência obtida com a execução dos comandos.


1. Qual o comando para obter a versão instalada do Git?
*R: git --version*
2. Qual o efeito da execução de cada um dos comandos abaixo?
  a. git help
*R: Faz a listagem de comandos que podem ser executados pelo git.*
  b. git help checkout
  *R: Abre um arquivo local .html com instruções detalhadas sobre o comando checkout* 
  c. git help merge
  *R: Abre um arquivo local .html com instruções detalhadas sobre o comando merge*
  d. git init
  *R: Cria uma pasta no diretório atual chamada ".git" indicando que foi inicializado um repositório git naquele diretório*
  e. git add --all
  *R: Adiciona ao git todos os arquivos dentro do diretório que não estão com versionamento.*
  f. git add -u
  *R: Atualiza (-u) todos os arquivos do diretório sem adicionar novos arquivos não versionados ao versionamento, apenas atualizando aqueles que já estão sendo versionados.*
  g. git config -l
  *R: Lista todas as variáveis contidas no arquivo de configurações do git, além de também listar os valores de cada uma.*
  h. git mv a.txt b.txt
  *R: Renomeia o arquivo a.txt para b.txt no controle de versionamento.*
  i. git reset --hard
  *R: Reseta todo o histórico de alterações para um determinado commit passado como parâmetro ou, caso não tenha parâmetros, reseta para o primeiro controle de versionamento estabelecido.*
  j. git log -27
  *R: Mostra o histórico de commits feitos com dados sobre os commits (branches, autor, data). O parâmetro -27 passado limita o resultado dos logs a no máximo 27 commits.*

3. O fluxo “clássico” de interação com o Git é algo como “alterar um ou mais arquivos”, “acrescentar essas mudanças para serem contemplados no próximo commit” e, finalmente, executar um “commit”. Quais os comandos necessários para realizar os dois últimos “passos” desse fluxo?
*R: Para acrescentar as mudanças para serem contempladas no próximo commit usa-se 'git add' e para efetuar o commit se usa o 'git commit'.*
4. Qual o comando deve ser executado para identificar o que foi alterado desde o último “commit”?
*R: Deve se usar o git diff.*
5. Em um dado repositório, arquivos simplesmente copiados para lá, ou seja, _untracked_, podem ser exibidos/identificados com que comando?
*R: Deve se usar o git status.*
6. Qual o comando para efetuar um _commit_?
*R: O comando: git commit -m "mensagem do commit"*

7. Qual o comando que devemos empregar para descartar mudanças ocorridas no arquivo teste.txt, por exemplo?
*R: Comando: git checkout [commit ID] -- nome_do_arquivo*
8. O que deve ser feito para que um determinado diretório do seu repositório seja ignorado pelo Git? Faça uma busca por **.gitignore**.
*R: Deve ser incluído no repositório um arquivo de nome '.gitignore' contendo quais arquivos e/ou diretórios devem ser ignorados pelo git. Por exemplo, uma entrada '*.log' no .gitignore irá ignorar nos commits todos os arquivos que terminem com .log.*
9. O que acontece se o seu repositório local for acidentalmente removido?
*R: Se seu repositório local for removido ele pode ser recuperado até as alterações feitas no repositório remoto (Github, por exemplo). Então poderia ser feito apenas um git clone no repositório remoto.*
10. Como clonar um repositório remoto?
*R: O comando é: git clone <<endereco_do_repositorio>>. Exemplo: git clone https://github.com/Gabriel-Rezende/cs-2022-1.git*

11. Em alguns cenários **git log** pode produzir extensos resultados. Se houver interesse em visualizar o histórico de um repositório, onde cada mudança é fornecida exatamente em uma única linha, qual o comando que deve ser empregado?
*R: Comando: "git log --oneline"*

12. Em qual arquivo o Git armazena informações de configuração empregadas por usuário?
*R: Empregadas por um usuário específico, as configurações ficam empregadas no arquivo: /.config/git/config*
13. Qual o comando para criar um repositório local?
*R: Comando: git init*

14. Qual o nome do diretório criado pelo Git quando se executa o comando **git init**?
*R: É criada uma pasta ".git".* 

15. Qual o comando para adicionar todos os arquivos modificados? (Aqueles para os quais **git status** identificam como **modified**?)
*R: Comando: git add .*

16. O Git faz uso do valor de hash conhecido por SHA1. O que isto significa? Qual o propósito? O que é SHA1?
*R: SHA significa Secure Hash Algoritm e o SHA1 é usado para gerar um hash de um determinado arquivo de modo que qualquer alteração nele gera um novo hash. A vantagem de usar o SHA1 é a segurança trazida, já que os arquivos estão criptografados.*

17. Qual a palavra para indicar o último _commit_ em vez do valor de hash SHA1 correspondente?
*R: HEAD~1*

18. Quando se cria dois arquivos usando um editor de texto qualquer e, na sequência, executamos o comando **git add -u**, os dois arquivos criados passam de _untracked_ para _new file_?
*R: Não.*

19. Qual o efeito da execução dos dois comandos abaixo, nesta ordem, em um dado repositório?
**git reset --soft HEAD~1**
**git reset --hard**
*R: O primeiro comando elimina o commit anterior, sem eliminar as alterações que foram feitas no commit. O segundo comando reseta a branch atual para o commit anterior (no caso, o penúltimo commit já que o último foi removido).* 

20. Após o emprego de um ambiente integrado de desenvolvimento (IDE), é comum a criação de arquivos e diretórios. Qual o comando que podemos empregar para remover arquivos e diretórios _untracked_?
*R: Caso queira que os arquivos entrem para o versionamento, pode ser dado um "git add .". Entretanto, caso não queira que os arquivos e pastas entrem para o versionamento, mas deixem de constar como untracked, pode ser feito um .gitignore para ignorar esses arquivos no versionamento.*

21. Qual o nome do arquivo no qual podemos inserir a indicação para o Git de arquivos e diretórios a serem ignorados?
*R: .gitignore*

22. Quando se cria o arquivo _MinhaClasse.class_ em um dado diretório e desejamos que arquivos com a extensão .class, como neste caso, sejam ignorados por todos os membros de uma equipe que estão contribuindo com um dado projeto, como devemos proceder?
R: Devemos colocar "*.class" no arquivo .gitignore.

23. jQuery é uma famosa biblioteca em JavaScript. Consulte detalhes em [jQuery](http://jquery.com). O repositório correspondente encontra-se em [gitRep](https://github.com/jquery/jquery.git). Faça o clone deste repositório.
*R: Feito.*

24. No repositório **jqueryrepo**, criado no passo anterior, qual o efeito do comando
**git shortlog -sne**?
*R: Mostra a quantidade de commits por autor, nome e email de cada.*

25. No repositório **jqueryrepo**, qual o efeito de **git remote -v**?
*R: Mostra a branch atual, além de mostrar a url para a branch.*

26. Um repositório Git pode ser etiquetado ao longo do tempo. Ou seja, _commits_ específicos podem ser “marcados” ou “etiquetados” para facilitar referências posteriores. Para listar todas as “etiquetas” (_tags_) estabelecidas para um dado repositório, qual comando deve ser executado?
*R: git tag.*

27. Caso um dato repositório retorne muitas “marcas” ou “etiquetas” para o comando **git tag**, como retornar apenas aquelas que atendem a determinado padrão, por exemplo, iniciadas por 2.0?
R: Comando: git tag -l 2.0*

28. Qual o efeito do comando **git tag -a 3.4-gold -m “minha versão ouro”**?
*R: Esse comando é dado para criar a tag, adicionando a mensagem "minha versão ouro".*

29. Após executado o comando acima, qual o efeito de **git show 3.4-gold**?
*R: Será exibido os commits dados com a tag, além de também mostrar dados referentes a tag.* 

30. O que o comando **git push origin 3.4-gold** teria como efeito?
*R: Vai transferir a tag em questão ao repositório remoto, caso ela já não esteja lá.*

31. Após executar um commit, qual o efeito de **git commit --amend**?
*R: Emenda as alterações atuais ao último commit. É usado para corrigir commits, alterar mensagens de commits e feitos do gênero.*

32. Após executar **git add x.txt**, qual o efeito de **git reset HEAD x.txt**?
*R: Irá fazer o reset das alterações no arquivo x.txt para conciliar o arquivo com o último registro salvo da branch atual. Se o comando git add x.txt for executado e logo após for dado o reset nesse arquivo ele irá voltar como arquivo não adicionado ao próximo commit, sendo necessário dar outro git add no arquivo.*

33. Após alterar o conteúdo de um arquivo committed em passo anterior, qual o efeito do comando **git checkout -- a.txt**?
*R: As mudanças feitas no arquivo são desconsideradas.*

34. Qual a diferença entre os comandos **git reset HEAD a.txt** e **git checkout -- a.txt**?
*R: Enquanto o git checkout apenas descarta as alterações feitas, o git reset tira aquele arquivo do git add.*

35. Veja como interpretar o resultado de git diff [aqui](https://medium.com/therobinkim/how-to-read-a-git-diff-6c87a9dc47c5). Execute, em um dos seus projetos, o comando **git diff HEAD~1 HEAD** e certifique-se de que entende o resultado apresentado.
*R: Feito.*