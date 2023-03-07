# Conversor de números inteiros em algarismo romano

Programa desenvolvido em python, que ler um número inteiro e retorna o algarismo romano correspondente.

```
===========================================
CONVERSOR DE ALGARISMOS ROMANOS EM INTEIROS
Digite um número: 40
===========================================
------------------
ARABICO: 40
ROMANO: XL
------------------
```

Há também a opção de verificar quantos números você quiser:

```
Deseja verificar mais algum número?
             [1] - SIM
             [2] - NÃO
->
```

## Restrições

- 1 <= numero <= 3999

## Como o código funciona

### Função converter_para_romanos( )

Para o código ficar mais limpo, primerio é criado uma função chamada `converter_para_romanos`, que receberá um `numero`. Essa função retornará o símbolo desejado.

Dentro da função é criado um dicionário para armazenar todos os símbolos possíveis para a conversão. Já é adicionado símbolos como o `IV`, `IX` para evitar fazer cálculos de subtração e adição.

```python
romanos = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
    }
```

Depois, é declarado a variável que receberá o resultado da função.

```python
resultado = ''
```

A lógica utilizada é que, vamos pegar um número qualquer, e derivar até o último algarismo. Lógica parecida com sistema de máquina de dinheiro.

Imagine que é necessário sacar R$225,00 no caixa do banco. As notas possíveis são `[2, 5, 10, 20, 50, 100]`, para o sistema da máquina sacar 225, seria necessária verificar qual a maior cédula possível. No exemplo apresentado é 100, subtrai o 100, e continua até sacar todas as notas. Seria necessárias duas notas de 100, uma de 20, e outra de 5.

É essa a lógica que vamos usar, mas ao invés das notas `[2, 5, 10, 20, 50, 100]`, vamos utilizar os valores `[1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]`, correspondentes aos simbolos `[I, IV, V, IX, X, XL, L, XC, C, CD, D, CM, M]`, pois todos os outros símbolos são derivados desses.

Tendo isso em vista, vamos fazer um loop para derivar até o último algarismo possível, que é 1 (I).

```python
while numero >= 1:
```

Dentro desse loop, vamos percorrer as chaves do dicionário onde estão os algarismos.

```python
for chave in romanos.keys():
```

E no momento em que a chave for menor que o número, então aquele é o maior valor possível:

```python
if chave <= numero:
    maior_possivel = chave
```

Poderia ser feito um `break` para quebrar o loop, mas como o dicionário é pequeno, optei por não quebrar, mas em programas mais complexos seria o ideal.

Depois de coletado o algarismo, diminuímos o `numero` para continuar a derivar.

```python
numero -= maior_possivel # deriva
resultado += romanos[maior_possivel] # coleta o algarismo
```

<br>

Finalizando todo o loop, retornaremos o `resultado` da função.

### Programa principal

Fazemos um loop "infinito", até o usuário preferir não continuar.

```python
while True
```

Será lido um número inteiro inserido pelo usuário. Esse valor é atribuído a uma variável chamada `algarismo_romano`, que recebe o retorno da função `converter_para_romanos`.

```python
valor_usuario = int((input('Digite um número: ')))
algarismo_romano = converter_para_romanos(valor_usuario)
```

É mostrado o algarismo correspondente ao número inserido.

```python
print(f'ROMANO: {algarismo_romano}')
```

No fim é criado um loop para perguntar do usuário, se ele quer continuar a converter mais números. Dependendo da resposta, o programa para.

```python
opcao_usuario = 3
    while opcao_usuario not in [1, 2]:
        print('Deseja verificar mais algum número?')
        print(f"{'[1] - SIM':^35}")
        print(f"{'[2] - NÃO':^35}")
        opcao_usuario = int(input('-> '))
```

Se caso, for digitado algum valor diferente das opções, o programa perguta novamente.

```python
if opcao_usuario not in [1, 2]:
    print()
    print('Não entendi!')
```

## Mais projetos python

Mais estudos sobre python: https://github.com/andre-jnr/estudos-python
