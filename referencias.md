## Remover diretorio criado antes do gitignore mas que está declarado no gitignore

O diretorio .idea tinha sido criado antes do gitignore e já estava no repositorio remoto (GitHub).

### Comando utilizado para remover o diretorio .idea do projeto local:

```console
git rm -r --cached .idea
```

O que acredito que o comando faça:

* ```-r``` possivelmente tem relacao com recursividade, para poder varrer todo o diretorio, excluir seus itens e voltar.

* ```--cached``` acredito que "tira a referencia ou alguma conexão" que o git faz para dizer que aquele arquivo pertence ao repositorio. 

Para alterar o repositorio remoto é só seguiir o fluxo padrão de alterações:

```console
git add .
git commit -m "Removido arquivo .idea"
git push
```

### Fontes:

[[Git] Removendo Arquivos de um Repositório](https://medium.com/@andgomes/git-removendo-arquivos-de-um-reposit%C3%B3rio-7eed699a035f)

## [Excluir commit de um branch](https://pt.stackoverflow.com/questions/128578/como-excluir-commit-de-um-branch-no-git)

## [Padrões do Git ignore](https://www.atlassian.com/br/git/tutorials/saving-changes/gitignore)