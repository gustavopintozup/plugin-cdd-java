<<<<<<< HEAD
# plugin-cdd-java

Plugin que avalia código Java usando a abordagem do CDD

## Utilização

![Plugin do CDD na StackSpot](https://github.com/gustavopintozup/stk-dev-java/blob/main/cdd/cdd.gif)


Para utilizar esse plugin, você precisa primeiro ter o o `stk` da StackSpot funcionando no seu computador. Para baixar o `stk`, siga as instruções [aqui](https://stackspot.com/).

Após download e instalação do `stk`, você precisa importar essa stack deste repositório na sua instalação do `stk`:

```
stk import stack git@github.com:gustavopintozup/plugin-cdd-java.git
```

Para garantir que o plugin foi importado corretamente, execute o comando:

```
stk list plugin
```

Para execução do plugin, basta roda-lo *dentro* do diretório do projeto que você deseja realizar a análise de código.

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
