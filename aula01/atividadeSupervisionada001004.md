

### Semana 1 - Dia 25/05/2022 - Aulas 001a004 - Atividade Supervisionada


1. Elaborar uma pesquisa sobre o tema "_Rest API_".
2. Elaborar um texto de pelo menos uma página, descrito com suas próprias palavras, destacando:
* As definições dos conceitos envolvidos;
* As principais características deste conceito (pelo menos umas cinco).

### Introdução
Para ser definido o que é uma API REST é necessário primeiro definir o que é uma API (_Application Programming Interface_). Uma API é um agregado de padrões e normas documentados que tem como objetivo otimizar a comunicação entre softwares permitindo que um software faça consumo, após autenticado, de informações vindas da API. Entre os benefícios estão a abstração do código, a facilidade de operação conjunta de um ou mais softwares e a padronização de informações.
Tratando especificamente de uma API REST, as requisições são HTTP e como resposta às requisições se tem dados estruturados em estrutura padrão como JSON, por exemplo. 
### Características de uma API REST

1. **Cliente/Servidor:** ter uma estrutura de cliente, servidor e recursos, de modo que todas as solicitações são gerenciadas por HTTP. É feita uma separação entre as responsabilidades da UI (_User Interface_) do banco de dados e/ou back-end. Desse  modo é possível que cada um evolua separadamente, diminuindo conflitos e garantindo uma escalabilidade e trabalho em equipe mais simplificados;
2. **Stateless:** numa comunicação _stateless_ nenhuma informação do cliente é armazenada em requisições GET, além de que as requisições não tem nenhum vínculo entre si. Cada requisição deve conter todos os dados necessários para que ela seja processada;
3. **Cache:** dados armazenados em cache para otimizar a comunicação entre cliente e servidor. O cache é controlado do lado do servidor através de cabeçalhos HTTP;
4. **Uniformidade:** ter interface uniforme de modo que as informações sejam transferidas em um formato padronizado. Além disso, serve para garantir a interoperabilidade entre o cliente e servidor, já que ambos farão uso da mesma interface é necessário separar as comunicações por alguns pontos:
	- é necessário que os recursos solicitados via API sejam identificáveis e estejam separados do recurso consumido pelo cliente;
	- as mensagens autodescritivas retornadas ao cliente devem ser suficientes para direcionar o próximo passo que o cliente deve tomar;
	- Representação dos recursos;
	- Uso do componente HATEOAS (_Hypermedia As the Engine Of Application State_) que permite ao cliente maior dinamicidade no consumo da API, conseguindo navegar na API mesmo sem conhecimento prévio através de hyperlinks contidos nas respostas de requisições.
6. **Camadas:** ter um sistema em camadas, para que servidores responsáveis por diferentes tarefas sejam separados, mas organizados. Tudo isso não visível ao cliente.

### Tipos de API REST

1. **Privadas:** são APIs que certamente tratam sobre dados extremamente sigilosos de uma empresa, onde a API deve ser usada apenas internamente. O acesso externo é bloqueado através de uso de servidor Proxy e autenticação de alto nível;
2.  **Parceiras:** quando a API vai ser utilizada entre softwares da mesma empresa ou softwares de parceiros. Nesse caso é feita uma autenticação comum.
3.  **Públicas:** APIs REST públicas são aquelas que podem ser acessadas por qualquer software. Geralmente são aceitas requisições HTTP GET.

Fontes de Pesquisa:
- https://blog.betrybe.com/desenvolvimento-web/api-rest-tudo-sobre/
- https://www.redhat.com/pt-br/topics/api/what-is-a-rest-api