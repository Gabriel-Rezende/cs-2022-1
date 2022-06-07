### Tarefa 004: Git Branching - 03/06/2021

1. Qual o nome do branch padrão do Git?
*R: O nome da branch padrão pode ter pequenas variações, mas geralmente é main. Pode ser master ou origin também.*

2. O que o comando **<code>git branch nome</code>** realiza?
*R: Cria uma branch com o nome especificado.*

3. Como criar um branch a partir de um commit específico?
*R: Pode ser feito com o seguinte comando: git branch branchname <sha1-do-commit>.*

4. Em um repositório, qual o efeito do comando **<code>git checkout -b bugfix/234</code>**?
*R: Cria uma nova branch com o nome bugfix/234 e alterna para essa nova branch.*

5. Qual o comando para se alternar para um branch de nome **experimento2**?
*R: git checkout experimento2*

6. Em um repositório com dois branches, **b1** e **b2**, onde b1 é o corrente, qual o efeito do comando **<code>git branch</code>**?
*R: Irá mostrar as branches do repositório, destacando a branch atual (b1, no caso).*

7. O que o comando **<code>git checkout -b</code>** nome faz?
*R: Cria uma branch que deverá ser passado o nome como parâmetro e alterna para a branch criada.*

8. Qual a função do <code>**comando git branch -d teste</code>**?
*R: Deleta a branch passada como parâmetro, no caso, deleta a branch teste.

9. Durante o desenvolvimento de um software é comum, por exemplo, utilizar um novo recurso por meio de experimentação. Talvez uma nova tecnologia, uma nova biblioteca que pode ser útil ao que está em desenvolvimento, ou até mesmo uma nova versão de um produto já empregado. Para que o uso deste novo recurso não interfira com o que é considerado pronto, um branch pode ser criado para a experimentação. Código que for criado para a experimentação existirá apenas no branch criado. Se eventualmente o experimento demonstrar um resultado satisfatório, as alterações realizadas no branch poderão ser incorporadas no que é considerado pronto, ou seja, no branch principal (master). Esta última ação é conhecida por merge. Neste item, crie uma sequência de comandos que simula um caso simples de criação e uso seguido de merge empregando um branch para ilustrar uma experimentação conforme acima. A sequência deve incluir, obrigatoriamente: (a) criação de um ou mais branches; (b) chaveamento para pelo menos dois branches e (c) merge.
*R:
git branch novorecurso
git checkout novorecurso
git add .
git commit -m "Novo recurso"
git checkout master
git merge novorecurso*