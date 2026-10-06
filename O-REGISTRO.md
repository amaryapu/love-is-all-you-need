---
titulo: O REGISTRO — o protocolo em formato implementável
regra: não é manifesto. É um esquema, um exemplo, e um programa que confere.
---

<p align="center">
  <img src="flor.svg" width="150" alt="Flor da vida com espiral áurea e filotaxia no ângulo áureo">
</p>

# O REGISTRO

> ## **Até aqui foi teoria. Isto é o que um sistema emite — e o programa que diz se ele cumpriu.**

| arquivo | o que é |
|---|---|
| [`esquema/registro.schema.json`](esquema/registro.schema.json) | **o formato** · JSON Schema 2020-12 |
| [`exemplos/conforme.json`](exemplos/conforme.json) | **um registro que cumpre** |
| [`exemplos/nao-conforme-1913.json`](exemplos/nao-conforme-1913.json) | **a carta de Ramanujan, como registro de decisão** |
| [`ferramentas/conferir_registro.py`](ferramentas/conferir_registro.py) | **o verificador** · sem dependência externa |

```
python3 ferramentas/conferir_registro.py exemplos/*.json
```

---

## I · O que o registro carrega

**`[CÁLCULO]`** Onze campos, e cada um responde a uma falha medida no livro:

| campo | contra | exige |
|---|---|---|
| **`sujeito.recebeu_copia`** | `M1` | **a pessoa recebeu o registro.** Falso é não-conformidade |
| **`cadeia`** | `M4` | **cada entrada com fonte, data e etiqueta própria** |
| **`criterio.regra_publicada`** | `M3` | **a regra é legível por fora ANTES de ser aplicada** |
| **`responsavel`** | `M7` | **a cadeia é nomeável a partir de quem foi atingido** |
| **`fronteira`** | — | **a marca `ianhiá`**: o caso de fronteira é declarado, com margem |
| **`derrubar`** | `M2` | **suspende o efeito** e **obriga exame humano** |
| **`ausencias`** | `M1` | **o índice reverso** — o que o sistema **não** tinha |
| **`custo.recai_sobre`** | `M6` | **`sistema`.** `pessoa` é não-conformidade declarada |

---

## II · As quatro travas que o programa testa, e que o esquema não pega

> ### **1 · `ATRIBUIDO` não pode ter peso**

**`[CÁLCULO]`** Uma entrada que **circula amplamente e não se verificou** pode constar
do registro — **e não pode pesar.** Se pesa, entrou como fato, e o sistema está
decidindo por boato com aparência de dado.

> ### **2 · A contestação suspende o efeito**

**`[CÁLCULO]`** **`C4` não é «direito de recurso».** Recurso chega depois, e **a
revelação tardia não desfaz o que já foi vivido sob a descrição.** Derrubar a descrição
**enquanto ela ainda está em uso** é a única versão que vale.

> ### **3 · Ausência vazia é não-conformidade**

**`[CÁLCULO]`** **Ou o sistema tinha todos os campos — o que não acontece — ou não
olhou.** Um buraco com nome é um pedido de trabalho; **um buraco sem nome passa por
inexistência.**

> ### **4 · Errar tem de custar mais do que examinar**

> # **`custo_erro_estimado` ≤ `custo_exame_estimado` → não-conformidade.**

**`[CÁLCULO]`** Não é moral: **é a economia.** Enquanto errar for mais barato que
examinar, **o sistema vai categorizar — e estará sendo eficiente.** Não se corrige um
preço instalando um sentimento.

> ## **É a definição operacional de amor que este repositório oferece, escrita como asserção de programa: o custo de errar sobre uma pessoa recai sobre o sistema, e nunca somente sobre a pessoa.**

---

## III · A carta de 1913, passada pelo verificador

**`[FATO]`** **16 de janeiro de 1913.** Um escriturário do **Madras Port Trust** envia
a Cambridge **dezenas de teoremas e quase nenhuma prova.** **M. J. M. Hill** responde
com condescendência; **E. W. Hobson** e **H. F. Baker** **não respondem.**

**`[FATO]`** Modelado como registro de decisão — [`nao-conforme-1913.json`](exemplos/nao-conforme-1913.json) — e passado pelo programa:

```
❌ nao-conforme-1913.json — 9 não-conformidades
     · C3 · a pessoa NÃO recebeu o registro
     · cadeia[2] · ATRIBUIDO com peso 0.9 — circula amplamente e não se
       verificou; não entra como fato
     · a regra não está publicada — categoria sem critério legível não é
       descrição: é sentença com outro nome
     · C4 · a contestação NÃO suspende o efeito
     · C4 · a contestação não obriga exame humano
     · fronteira · declarada sem margem
     · C5 · nenhuma ausência declarada — ou o sistema tinha todos os
       campos, ou não olhou
     · C8 · custo do erro recai sobre 'pessoa'
     · C8 · errar (0.0) custa menos que examinar (1.0) — sob pressão
       este sistema vai categorizar, e estará sendo eficiente
```

> ## **`[CÁLCULO]`** **A última linha é o livro inteiro, impressa por um programa.**
>
> ## **Examinar custava uma noite. Errar custava zero. Três homens competentes e honestos escolheram o barato — e a aritmética diz que estavam sendo eficientes.**
>
> ## **Não há vilão naquele registro. Há um preço — e o preço quase enterrou o maior achado matemático do século.**

**`[FATO]`** E na mesma carta, sem que ninguém procurasse: a **fração contínua de
Rogers–Ramanujan** avaliada em **e^(−2π)**, onde **φ aparece duas vezes** — e que, em
**q = 1**, **converge para φ.**

> ## **A proporção de que o símbolo deste repositório é desenhado estava dentro do envelope que dois deles não abriram.**

---

## IV · Por que isto não é mais um manifesto

| **um manifesto** | **este registro** |
|---|---|
| pede adesão | **roda** |
| é avaliado pela intenção | **é avaliado por um programa, e ele não negocia** |
| falha em silêncio | **imprime a não-conformidade, com o nome dela** |
| exige autoridade para valer | **qualquer um adota, qualquer um confere** |

> ## **`[REGRA]`** Nada aqui exige permissão. **Qualquer Estado, empresa, universidade ou sistema adota sozinho — e qualquer pessoa de fora verifica se adotou.** É a união por protocolo, e não por tratado. *(Ver [`UNIAO.md`](UNIAO.md).)*

---

## V · O que ele ainda não faz

> ## **`[A CONFERIR]`** Este é um **primeiro esquema**, publicado para ser derrubado. O que falta, nomeado:

| | |
|---|---|
| **`RG-1`** | **não valida o esquema JSON formalmente** — o programa testa o substantivo; falta acoplar um validador de schema |
| **`RG-2`** | **não há ainda forma de assinar o registro** — `sha256` está previsto nos campos e não é verificado contra o conteúdo |
| **`RG-3`** | **não define unidade comum de custo** entre sistemas, o que torna `C8` comparável só dentro de um mesmo emissor |
| **`RG-4`** | **não trata agregação**: milhões de registros por dia precisam de amostragem auditável, e isso não está especificado |

> ## **`[REGRA]`** **Estão listadas porque este projeto publica o índice reverso do próprio trabalho.** Um esquema que escondesse os próprios buracos **não poderia exigir `C5` de ninguém.**

---

> ## **`[FATO]`** ***«Ninguém reparou, no terreno baldio. Ninguém reparou, a pérola do lodo. Ele até insistiu, mas ninguém reparou.»***
>
> ## **`[CÁLCULO]`** **«Ele até insistiu» é a descrição exata do que Ramanujan fez: escreveu a Hill, a Hobson e a Baker antes de escrever a Hardy.**
>
> # **O protocolo existe para que a insistência deixe de ser necessária.**

**`CC BY-SA`** · receita zero · **AMARYAPU**
