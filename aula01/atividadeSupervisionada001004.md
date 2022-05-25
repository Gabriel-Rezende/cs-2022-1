
### Semana 1 - Dia 25/05/2022 - Aulas 001a004 - Atividade Supervisionada


1. Elaborar uma pesquisa sobre o tema "_Rest API_".
2. Elaborar um texto de pelo menos uma página, descrito com suas próprias palavras, destacando:
* As definições dos conceitos envolvidos;
* As principais características deste conceito (pelo menos umas cinco).

### Texto:
Para ser definido o que é uma API REST é necessário primeiro definir o que é uma API (_Application Programming Interface_). Uma API é um agregado de padrões e normas documentados que tem como objetivo otimizar a comunicação entre softwares permitindo que um software faça consumo, após autenticado, de informações vindas da API. Entre os benefícios estão a abstração do código, a facilidade de operação conjunta de um ou mais softwares e a padronização de informações.
Tratando especificamente de uma API REST, as requisições são HTTP e como resposta às requisições se tem dados estruturados em estrutura padrão como JSON, por exemplo. 
Para que uma API seja considerada RESTful é necessário que ela esteja de acordo com essas características:

1. **Cliente/Servidor:** ter uma estrutura de cliente, servidor e recursos, de modo que todas as solicitações são gerenciadas por HTTP; 
2. **Stateless:** numa comunicação _stateless_ nenhuma informação do cliente é armazenada em requisições GET, além de que as requisições não tem nenhum vínculo entre si;
3. **Cache:** dados armazenados em cache para otimizar a comunicação entre cliente e servidor;
4. **Uniformidade:** ter interface uniforme de modo que as informações sejam transferidas em um formato padronizado;
5. **Camadas:** ter um sistema em camadas, para que servidores responsáveis por diferentes tarefas sejam separados, mas organizados. Tudo isso não visível ao cliente.

### Tipos de API REST:

1. **Privadas:** são APIs que certamente tratam sobre dados extremamente sigilosos de uma empresa, onde a API deve ser usada apenas internamente. O acesso externo é bloqueado através de uso de servidor Proxy e autenticação de alto nível;
2.  **Parceiras:** quando a API vai ser utilizada entre softwares da mesma empresa ou softwares de parceiros. Nesse caso é feita uma autenticação comum.
3.  **Públicas:** APIs REST públicas são aquelas que podem ser acessadas por qualquer software. Geralmente são aceitas requisições HTTP GET.

Fontes de Pesquisa:
https://blog.betrybe.com/desenvolvimento-web/api-rest-tudo-sobre/
https://www.redhat.com/pt-br/topics/api/what-is-a-rest-api