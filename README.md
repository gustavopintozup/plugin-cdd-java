# plugin-cdd-java

Plugin que avalia código Java usando a abordagem do CDD

## Utilização

![Plugin do CDD na StackSpot](https://github.com/gustavopintozup/stk-dev-java/blob/main/cdd/cdd.gif)


Para utilizar esse plugin, você precisa primeiro ter o o `stk` da StackSpot funcionando no seu computador. Para baixar o `stk`, siga as instruções [aqui](https://stackspot.com/).

Após download e instalação do `stk`, você precisa primeiro criar uma stack pelo `stk`. Acesse [aqui o guia oficial para criação de stacks](https://docs.stackspot.com/v3.6.0/docs/creators-guide/creator-tutorials/howto-create-stack/). 

Após criar uma stack, basta adicionar o plugin do cdd na stack:

```
stk add stack git@github.com:gustavopintozup/plugin-cdd-java.git

> Verifying "git@github.com:gustavopintozup/plugin-cdd-java.git" plugin git repository...
- Plugin repository is valid.
> Adding "git@github.com:gustavopintozup/plugin-cdd-java.git" plugin to stack...
- "git@github.com:gustavopintozup/plugin-cdd-java.git" added to stack.
```

Para garantir que o plugin foi importado corretamente, execute os comandos:

```
git push          # para enviar as modificações na stack para o repo remoto
stk update stack  # para atualizar o stk com as modificações remotas
stk list plugin   # para listar os plugins atuais

#...

+-----------------+---------------------------------------------------------+---------+-----------------+
| name            | description                                             | types   | version(latest) |
+-----------------+---------------------------------------------------------+---------+-----------------+
| plugin-cdd-java | Plugin que avalia código Java usando a abordagem do CDD | ['app'] | no release      |
+-----------------+---------------------------------------------------------+---------+-----------------+
```

Caso você receba uma saída similar a de cima, você está pronto para começar a usar o plugin!

Para executar plugin, basta roda-lo *dentro* do diretório do projeto que você deseja realizar a análise de código.

```
cd <nome-do-meu-projeto>
stk apply plugin <sua-stack>/plugin-cdd-java
```

## Documentação

Para saber mais como configurar e utilizar o plugin do cdd, leia esta [documentação](documentacao-plugin-cdd.md).


## Limitações conhecidas

- O plugin não funciona na plataforma Windows.

## Dúvidas

Caso você tenha alguma dúvida ou dificuldade no uso, abra uma issue nesse repositório para que possamos auxilia-lo.
