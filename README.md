Group Members:
- Ricardo Furbino (2020420630) | Git: fubininho
- Thiago Miarelli

Escopo (Objetivo):
- Estamos fazendo um sistema similar ao IMDb (Internet Move Database).

Funcionalidades:
  <ul>
    <li>Registro de Usuário e criação de perfil</li>
    <li>Possibilidade de cadastro de filmes e de avaliá-los, bem como avaliar os dos demais.</li>
    <li>Fornecer informações gerais (como atores, diretores, duração, etc).</li>
    <li>Permitir que o usuário procure por filmes específicos ou filtre por gênero.</li>
    <li>Possibilidade de criação de uma lista de favoritos</li>
  </ul>

Tecnologias Principais:
  Flask

Histórias de Usuário:
- Como um usuário da Web, quero me cadastrar. (Ricardo) OK.
    - Criar uma Classe Usuário.
    - Fazer uma Tela de Cadastro.
    - Fazer criptografia senha.
    - Validação email e nome do usuário.
- Como um usuário da Web, quero fazer o login. (Ricardo) OK.
    - Fazer uma Tela de Login.
    - Verificar o Email e Senha.
    - Deixar o Usuário Logado.
- Como um administrador, quero cadastrar um novo filme.(Diane) OK.
    - Fazer uma tela para cadastro.
    - Verificar se é um administrador fazendo aquela ação.
    - Fazer a classe Filme.
- Como um administrador, quero ver a listagem de todos os filmes. (Rafael) OK.
    - Tabela mostrando todos os filmes.
    - Ter acesso a botão para realizar ações de editar e excluir.
    - Ter um filtro de filmes.
- Como um administrador, quero editar um filme. (Rafael) OK.
    - Mostrar tela para editar com as infos do filme.
- Como um administrador, quero deletar um filme. (Rafael) OK.
    - Aparecer um modal para confirmar a ação.
- Como um usuário, quero avaliar um filme. (Rafael) OK.
    - Cadastrar a Classe de Avaliação
    - Ver a página do filme.
    - Enviar comentário e nota.
    - Proibir comentário de não-logados.
- Como um usuário da Web, quero encontrar um filme.(Diane) OK.
    - Página dos gêneros. (Não ok)
    - Fazer uma busca.
- Como um usuário da Web, quero visualizar um filme. (Diane)
    - Fazer página de Visualização do filme
    - Ver nota média do filme
    - Ver comentário do filme com nota
- Como um usuário da Web, quero ver informações sobre o site. (Rafael)
    - Fazer a página home.
- Tarefa extra:
    - Fazer a base do sistema. (Ricardo) Completo.


Obs: Todos os desenvolvedores serão full-stack de suas respectivas tarefas.
