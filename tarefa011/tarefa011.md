# Padrões de Codificação
Um código fonte organizado é um facilitador de todos os processos do desenvolvimento como retirada de bugs, atividades de validação e manutenção de código.

Uma vez que se usa um padrão de codificação também é aumentada a produtividade num projeto, dado que toda a equipe fica mais ciente do código e facilita a comunicação entre integrantes da mesma equipe.

Padrões de codificação incluem padrões em comentários, espaços em branco, identação, etc. Tudo que tange um código, como declarar uma classe, uma função, etc, pode ser incluído em um padrão de codificação.

Por exemplo, no python existe um padrão de codificação definido pela PEP8 que coloca regras sobre tamanho de linhas de código, identação, onde colocar espaços em branco, entre outros.

Exemplos da PEP8: se uma classe é criada, necessariamente antes dela tem que ter duas linhas em branco. Se um método é criado, antes da definição desse método tem que ter uma linha em branco de código.


# Reflexão
Reflexão na programação é um meio utilizado para examinar ou modificar o comportamento de métodos, classes e interfaces em tempo de execução. Pode ser usado para ter informações dos métodos, dos contrutores e da definição de uma classe.

Geralmente é implementado através de uma API de reflexão de código que permite inspecionar o código e saber mais sobre o código daquela classe em tempo de execução.

Por exemplo, no Java, uma classe com método protegido ou privado não pode ter seus métodos acessados arbitrariamente. Na hora de implementar os testes unitários e de integração isso pode ser problema.
Para quem usa reflexão, isso pode ser resolvido em tempo de execução tornando a classe pública apenas para a execução daqueles testes em específico.

# Programação Defensiva

Geralmente se espera que um software funcione com entradas e saídas de dados de uma determinada maneira. Nem sempre as coisas fluem do jeito que o desenvolvedor pensou, muitas vezes a entrada de dados vêm com um dado formatado diferente do planejado e erros do tipo.

Pensando nisso e, para proteger o software dos possíveis erros do usuário e dos desenvolvedores, se usa a programação defensiva.

A programação defensiva define algumas regras, dentre elas a principal:

- Nunca confie nos dados inseridos pelo usuário: todos os dados enviados por fontes externas têm que passar por um forte critério de formatação caso seja necessário que esse dado possua determinado formato pré-definido.

A tratativa de erros causados por entradas falhas de dados do usuário pode ser feita de diversas maneiras. Se um usuário deve inserir uma data de nascimento no formato DD/MM/AAAA e insere AAAA-MM-DD o software deve: reconhecer o erro e corrigir automaticamente; ou retornar um valor padrão caso seja identificado que a entrada foi errada; ou lançar uma exceção que interrompa o fluxo da aplicação no momento do erro. 