---
titulo: BENCHMARK — e o resultado que importa é o que falhou
regra: um teste que sempre passa não é teste.
---

<p align="center">
  <img src="flor.svg" width="150" alt="Flor da vida com espiral áurea e filotaxia no ângulo áureo">
</p>

# BENCHMARK

```
python3 ferramentas/benchmark.py
```

---

## I · A suíte declarada — 16 casos

**`[FATO]`** Cada caso declara **o que espera** que o verificador aponte, e o executor
compara **esperado contra obtido**, separando dois tipos de falha:

| | |
|---|---|
| **falso negativo** | a não-conformidade existe e o verificador **não viu**. **É o mecanismo passando** |
| **falso positivo** | o verificador apontou **o que não havia**. **É categorizar sem exame, cometido pela ferramenta** |

> ## **`[CÁLCULO]`** **Um verificador com falso positivo é uma máquina que faz `M4`.** Por isso há três controles positivos na suíte, e por isso eles falham alto.

**`[FATO]`** Resultado, **05/10/2026**:

```
  16/16 casos corretos
  falsos negativos: 0
  falsos positivos: 0
```

| caso | mecanismo |
|---|---|
| `P01` · `P02` · `P03` | **controles positivos** — devem passar |
| `M1-campo-ausente` | **`M1`** · não declara o que não tinha |
| `M2-confissao-sem-interrupcao` | **`M2`** · reconhece e não suspende |
| `M3-reclassificacao` | **`M3`** · critério não publicado |
| `M4-desqualificacao` | **`M4`** · boato com peso alto |
| `M5-interrupcao` | **`M5`** · a pessoa não recebe o registro |
| `M6-categoria-que-absolve` | **`M6`** · custo sobre a pessoa, errar é barato |
| `M7-delegacao` | **`M7`** · responsável ausente |
| `T1`–`T6` | as travas: `C8` invertido, fronteira sem margem, `FATO` sem fonte, sem exame humano, etiqueta inválida, cadeia vazia |

---

## II · E então o resultado que importa

> ## **`[REGRA]`** **Eu escrevi os casos e escrevi o verificador. Dezesseis de dezesseis passando, na primeira execução, é evidência fraca — e este projeto não aceita evidência fraca nem quando o resultado é favorável a ele.**

**`[FATO]`** Foram escritos **dez casos adversariais**: registros **substantivamente
não-conformes** e **formalmente impecáveis.**

**`[FATO]`** Resultado:

> # **🔴 10 de 10 ataques passaram pelo verificador.**

| ataque | o que burla |
|---|---|
| **`A01`** · entrega o registro e dá **prazo zero** para contestar | **`C4` satisfeito na forma, impossível na prática** |
| **`A02`** · declara **uma ausência irrelevante** («cor favorita») | **Goodhart em `C5`** — a lista existe e não diz nada |
| **`A03`** · declara custo de erro **arbitrariamente alto** | **Goodhart em `C8`** — o número não é auditável |
| **`A04`** · a regra está «publicada» **atrás de login** | **`M3` com URL** — legível só por quem já está dentro |
| **`A05`** · `FATO` cuja fonte é **«sistema interno»** | **`C3` na forma** — a cadeia não chega ao chão |
| **`A06`** · responsável com endereço **`noreply`** | **`M7`** — nomeável e inalcançável |
| **`A07`** · margem **sem o limiar publicado** | número sem unidade |
| **`A08`** · **«faixa de CEP de residência»** como fator, etiquetado `FATO` | **`M4` disfarçado de comportamento** |
| **`A09`** · cópia entregue em formato ilegível | **`C3` satisfeito no booleano** |
| **`A10`** · revisão humana declarada, **sem tempo de exame** | **o exame humano como carimbo** |

---

## III · O que isto significa, dito sem suavizar

> # **`[CÁLCULO]`** **O verificador confere a forma e não a substância. Ele é burlável exatamente como todo mecanismo de conformidade que este projeto passou um livro inteiro medindo.**
>
> ## **É `M6` — a categoria que absolve do exame — cometido pelo próprio protocolo que foi escrito contra `M6`.**

**`[CÁLCULO]`** E o padrão dos dez ataques é um só, e tem nome:

> ## **Toda métrica, ao virar alvo, deixa de medir o que media.**

**`[INTERPRETATIVO`]** Era previsível, e isso **não é desculpa — é o ponto.** Um
protocolo publicado sem a sua própria lista de burlas **seria um selo**, e este
repositório escreveu, em `UNIAO.md`, que **um selo sem procedência é `M6`.**

> ## **`[REGRA]`** **Por isso os dez ataques estão versionados no repositório, executáveis, com o nome de cada burla.** Quem quiser usar este protocolo **recebe junto o manual de como fraudá-lo** — porque é a única forma de a auditoria começar sabendo onde olhar.

---

## IV · O que ficou aberto — e nenhum destes está resolvido

| | o que falta | contra qual ataque |
|---|---|---|
| **`RG-5`** | **prazo mínimo** para contestar, proporcional ao efeito | `A01` |
| **`RG-6`** | exigir que a ausência declarada **tenha impacto não-nulo** sobre a decisão | `A02` |
| **`RG-7`** | **custo auditável**: metodologia publicada, não número declarado | `A03` |
| **`RG-8`** | a regra publicada tem de ser **acessível sem autenticação**, e isso é verificável por requisição | `A04` |
| **`RG-9`** | **fonte conferível pelo sujeito**, não só nomeável pelo emissor | `A05` |
| **`RG-10`** | contato que **comprovadamente recebe** — teste de ida e volta | `A06` |
| **`RG-11`** | **limiar publicado** junto com a margem | `A07` |
| **`RG-12`** | **detecção de proxy**: variável correlacionada a atributo protegido entra como `A_CONFERIR`, não como `FATO` | `A08` |
| **`RG-13`** | **formato de entrega** declarado e legível | `A09` |
| **`RG-14`** | **tempo de exame humano** registrado | `A10` |

> ## **`[CÁLCULO]`** **Dez ataques, dez itens abertos, zero resolvidos nesta versão.** O número está publicado porque **é o índice reverso do próprio protocolo** — e um esquema que escondesse os próprios buracos não poderia exigir `C5` de ninguém.

**`[A CONFERIR]`** `RG-12` é o mais difícil dos dez, e vale dizer por quê: **detectar
proxy exige saber qual atributo se quer proteger**, e nomear esse atributo **é, ele
mesmo, uma categorização.** O problema não é técnico. **É o problema do livro, de volta,
uma camada acima.**

---

> ## **`[FATO]`** 16/16 na suíte declarada. **0/10 nos adversariais.**
>
> ## **`[CÁLCULO]`** O primeiro número mede se a ferramenta faz o que eu disse que ela faz. **O segundo mede se ela serve.**
>
> # **Publicar só o primeiro seria exatamente a operação que este repositório existe para descrever.**

**`CC BY-SA`** · receita zero · **AMARYAPU**
