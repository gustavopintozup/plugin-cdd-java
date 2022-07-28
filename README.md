# plugin-cdd-java

Plugin que avalia código Java usando a abordagem do CDD

![Plugin do CDD na StackSpot](https://github.com/gustavopintozup/stk-dev-java/blob/main/cdd/cdd.gif)

## Utilização

Para utilizar esse plugin, você precisa primeiro ter o o `stk` da StackSpot funcionando no seu computador. Para baixar o `stk`, siga as instruções [aqui](https://stackspot.com/).

<!-- Usando o `stk`, você pode usar o plugin de maneira isolada, ou associado a uma stack. 

### Usando o plugin de maneira isolada

Para usar o plugin isoladamente, primeiro baixe o fonte desse repositório na sua máquina local.

```
git clone git@github.com:gustavopintozup/plugin-cdd-java.git
```

Depois de baixar, para rodar o plugin em um repositório, basta rodar o seguinte comando. 

```
```
-->

### Adicionando o plugin a uma stack

Após download e instalação do `stk`, você precisa primeiro criar uma stack pelo `stk`. Acesse [aqui o guia oficial para criação de stacks](https://docs.stackspot.com/v3.6.0/docs/creators-guide/creator-tutorials/howto-create-stack/). 

Após criar uma stack, basta adicionar o plugin do cdd na stack. Para isso, entre na pasta da sua stack e rode o comando abaixo:

```
stk add plugin git@github.com:gustavopintozup/plugin-cdd-java.git

> Verifying "git@github.com:gustavopintozup/plugin-cdd-java.git" plugin git repository...
- Plugin repository is valid.
> Adding "git@github.com:gustavopintozup/plugin-cdd-java.git" plugin to stack...
- "git@github.com:gustavopintozup/plugin-cdd-java.git" added to stack.
```

### Verificando se o plugin foi adicionando corretamente

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

### Rodando o plugin

Para executar plugin, basta roda-lo *dentro* do diretório do projeto que você deseja realizar a análise de código.

```
cd <nome-do-meu-projeto>
stk apply plugin <sua-stack>/plugin-cdd-java
```

### Examinando a saída do plugin

O plugin irá ansalisar todas as classes do projeto e irá imprimir somente as classes em que o valor de ICP seja maior do que 10 (este limite pode ser definido no arquivo de configuração `cdd.json`). 

Um exemplo de saída está abaixo: 

```
br.com.zup.lms.admin.LearningTaskTest[acoplamento=11,ICP=11]
br.com.zup.lms.admin.DescricaoTreinamentoParserVisitor[if=6,condicao=6,acoplamento=3,ICP=15]
br.com.zup.lms.admin.partials.learningtask.LearningTask[acoplamento=15,ICP=15]
br.com.zup.lms.admin.TaskClassTest[acoplamento=10,ICP=10]
```

Essa saída lista quatro classes com ICP maior do que o limite definido (no caso, 10). Para cada classe, também é listado (entre colchetes) os ICPs individuais. Por exemplo, a classe `br.com.zup.lms.admin.DescricaoTreinamentoParserVisitor` utiliza 6 `if`s, com 6 condicionais e está acoplada com 3 outras classes.

## Documentação

Para saber mais como configurar o plugin do cdd, leia esta [documentação](documentacao-plugin-cdd.md).


## Limitações conhecidas

- O plugin não funciona na plataforma Windows.
- O plugin não funciona em projetos com submódulos; [essa é uma limitação da ferramenta spoon, que usamos como base](https://stackoverflow.com/questions/43313161/how-do-we-deal-with-the-type-xxx-is-already-defined-in-spoons-source-code-ana).

## Dúvidas

Caso você tenha alguma dúvida ou dificuldade, abra uma issue nesse repositório para que possamos auxilia-lo.

## Licensa

O plugin está licenciado com MIT