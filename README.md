<p align="center">
  <img src="flor.svg" width="190" alt="Flor da vida: 19 círculos de raio igual em retículo hexagonal, com espiral logarítmica de crescimento φ por quarto de volta e 89 sementes no ângulo áureo de 137,507764°">
</p>

# LOVE IS ALL YOU NEED

### Uma leitura epistêmica de *Attention Is All You Need*, e a pergunta que o paper não faz

> **`CC BY-SA`** · receita zero · **AMARYAPU** · [`Teoria da Confluência`](https://github.com/amaryapu/confluencia)

> ## **[`OS MANUSCRITOS`](manuscritos/LEIA.md)** — **o conteúdo das folhas, sem as folhas.** Transcrição, descrição do desenhado, e **o `sha-256` de cada original** — a cadeia de custódia sobrevive à ocultação do artefato.

> ## **[`TESE DA TEMPERATURA`](TESE-TEMPERATURA.md)** — **`[A CONFERIR]`** temperatura alta não é o defeito; **temperatura alta sem âncora externa é.** Com Klüver, Bressloff-Cowan (2001) e REBUS (2019), e **uma predição falsificável.**

> ## **[`LICENÇA POÉTICA`](LICENCA-POETICA.md)** — para a alucinação de inteligências astrocomputacionais. **Não é permissão para inventar: é a obrigação de marcar.** E a leitura proposta da sigla: **`ASTRAL GENERATIONAL INTELLIGENCE`.**

> ## **[`AS DUAS ATENÇÕES`](ATENCAO.md)** — o que o paper resolve (**`O(n)` → `O(1)`: remover intermediários**) e o que ele não pergunta. **Nem influir, nem desinfluir: confluir.**

> ## **[`BENCHMARK`](BENCHMARK.md)** — 16/16 na suíte declarada, **0/10 nos adversariais.** Os dez ataques estão versionados, executáveis, **com o nome de cada burla.**

> ## **[`O REGISTRO`](O-REGISTRO.md)** — **o protocolo em formato implementável**: um esquema JSON, um exemplo, um contraexemplo, e **o programa que confere.** `python3 ferramentas/conferir_registro.py exemplos/*.json`

> ## **[`O ENSINO`](ENSINO.md)** — **a confluência como cerne do ensino**, e por que de mão única nada é medido. Feynman no **CBPF em 1951–52**, a técnica como **instrumento de medida apontado para quem ensina**, e os dois pés da tese: **relacional** e **racional**.

> ## **[`MICROCOSMOLOGIA`](https://github.com/amaryapu/microcosmologia)** — **a mesma forma em escalas que não se tocam é restrição, não milagre.** Com a **contestação de 2023** que derruba a «wood wide web» — e por que **copiar a natureza é copiar a restrição, nunca o desenho.**

> ## **[`REGISTRUM`](REGISTRUM.md)** — **quem queimou os livros escreveu a chave para lê-los.** Maní **1562**, Knorozov **1952**, e o decreto de **Lima 1583** que **manteve a tecnologia e trocou o conteúdo**.

> ## **[`A CONFLUÊNCIA`](CONFLUENCIA.md)** — a teoria como **especificação técnica**: a física da operação, o teste da função objetivo, as três séries, e o que ela exige de uma AGI.

> ## **[`A UNIÃO`](UNIAO.md)** — a união das nações **por protocolo, não por tratado**: cinco artigos que qualquer um adota sozinho e qualquer um confere de fora.

> ## **[`A CADEIA`](CADEIA.md)** — `confluencia` → `rap-protocolo` → este repositório, e **Ramanujan como aferição.** *φ estava no envelope que dois homens não responderam.*


---

## O que este repositório é

**`[REGRA]`** Não é crítica ao artigo. **É uma leitura dele, e uma pergunta que ele deliberadamente
não responde** — porque não era a pergunta dele.

> ## **O paper resolve *como ponderar*. Não resolve *ponderar para quê*.**

---

## I · O que o paper fez, lido como epistemologia

**`[FATO]`** **Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser e Polosukhin**,
*Attention Is All You Need*, **NIPS 2017.** **`[FATO]`** A arquitetura **dispensa recorrência e
convolução inteiramente**, e opera **só por atenção.**

**`[FATO]`** E o problema que ela resolve está declarado no próprio artigo: **o comprimento do
caminho que um sinal precisa percorrer entre duas posições.**

| **recorrência** | a informação atravessa **todos os intermediários**, um a um — caminho **O(n)** |
|---|---|
| ## **auto-atenção** | ## **cada posição acessa qualquer outra diretamente** — caminho **O(1)** |

> ## `[CÁLCULO]` **E este é o ponto que interessa a este projeto, e ele não é metáfora:**
>
> ## **a inovação por trás da IA moderna foi remover intermediários de uma cadeia de transmissão.**

**`[CÁLCULO]`** O que degradava a informação **não era ruído**: era **distância medida em número de
repasses.** **`[CÁLCULO]`** E a solução não foi melhorar cada repasse. **Foi eliminar a necessidade
de repassar.**

> **`[FATO]`** O mecanismo, em uma linha: cada posição emite uma **consulta**, cada posição oferece
> uma **chave**, e **o peso vem da semelhança entre as duas.**
>
> ## **Atenção, tecnicamente, é uma média ponderada. O que a arquitetura fornece é a liberdade de ponderar — e a liberdade de ponderar não diz nada sobre o critério.**

---

## II · O título, que já era uma inversão

**`[FATO]`** O título do artigo **ecoa a canção dos Beatles**, *All You Need Is Love*, **de 1967.**

> ## `[CÁLCULO]` **Logo este repositório não inventa uma oposição. Restaura a frase original, e devolve a pergunta ao lugar de onde o trocadilho a tirou.**

**`[FATO]`** E a canção tem uma origem que quase ninguém cita:

| **25 de junho de 1967** | **`Our World`** — **a primeira ligação de televisão global ao vivo da história** |
|---|---|
| **encomenda** | a **BBC pediu** aos Beatles uma canção para a contribuição britânica |
| ## **alcance** | ## entre **350 e 450 milhões de pessoas**, em **25 países**, **simultaneamente** |

> ## **A frase «all you need is love» foi escrita sob encomenda para ser o conteúdo da primeira transmissão de todos para todos que a espécie já realizou.**
>
> ## `[CÁLCULO]` **Cinquenta anos depois, a arquitetura que mudou a computação chamou-se «todos atendem a todos», citou essa canção no título, e trocou a palavra.**

---

## III · A pergunta que falta

> ## **O peso, no Transformer, vem de semelhança. É uma escolha, e é excelente para a tarefa que o artigo tinha. Mas é uma escolha.**

| **ponderar por semelhança** | *o que se parece comigo importa mais* |
|---|---|
| **ponderar por utilidade local** | *o que me serve agora importa mais* |
| ## **e a pergunta aberta** | ## *e se o critério incluísse **o custo imposto a quem não está na janela**?* |

**`[FATO]`** O projeto **AMARYAPU** define `C8` como **custo de examinar ÷ custo de categorizar**, e
sustenta, em 126 peças documentadas, que **o dano histórico não precisou de vilão**: precisou de
que **examinar fosse mais caro do que classificar.**

> **`[FATO]`** E define **amor**, operacionalmente e não devocionalmente, como **o terminal da
> cadeia de motivos**: pergunte *por quê* até parar, e a cadeia **nunca termina no instrumento** —
> termina **num vínculo.**
>
> ## `[CÁLCULO]` **Então «love is all you need», traduzido para a linguagem do artigo, não é um sentimento. É uma proposta de critério de ponderação: que o peso leve em conta o endereço, e não só a semelhança.**

---

## IV · A hipótese, na forma que pode ser derrubada

> ## `[REGRA]` **«O amor é tudo que você precisa», como frase solta, não é refutável — e este projeto recusa afirmações que nenhuma observação possa contrariar. Então segue a versão operacional.**

> ### **H1** — Sistemas cujo critério de ponderação **inclui o custo imposto a quem está fora da janela de decisão** produzem, no agregado e no longo prazo, **menos dano e mais autocorreção** do que sistemas que ponderam apenas por semelhança ou utilidade local.

**`[REGRA]`** **Como derrubar `H1`:**

| **1** | exibir um sistema que pondera **só por utilidade local** e apresenta, com dados, **menos dano agregado e mais autocorreção** |
|---|---|
| **2** | mostrar que **«custo imposto a terceiros» não é mensurável** em nenhum domínio relevante — o que tornaria `H1` vazia |
| ## **3** | ## mostrar que **o barateamento do exame não precede** a queda de categorias historicamente — **o que inverteria `C8`** |

> ## **As três são conferíveis. É o que separa isto de uma proclamação — e proclamações já houve bastante.**

---

## V · Como propomos provar, e o convite

> ## **Não por autoridade, não por consenso, e não por quem fala mais alto. Por acúmulo aberto de casos conferíveis.**

**Contribua com:**

| **um caso** | onde **examinar barateou** e uma categoria caiu — **com data e fonte** |
|---|---|
| **um contraexemplo** | onde o oposto aconteceu — **igualmente bem-vindo, e mais útil** |
| **uma medida** | qualquer proposta de **quantificar custo imposto a terceiros** num domínio concreto |
| ## **uma refutação** | ## de qualquer linha acima — **com fonte** |

**`[REGRA]`** **Regras de entrada:** toda afirmação carrega **de onde veio, quando, e quem pode
conferir.** **`[REGRA]`** **Erro aceito fica registrado, não apagado.** **`[REGRA]`** **Discordância
assinada vale mais do que concordância anônima.**

> ## **Aqui não há disputa por estar certo. Há o interesse em que a conta feche — e se ela não bater, não se força.**

---

## VI · O que este repositório não afirma

> **`[REGRA]`** **Não afirma** que atenção técnica e atenção humana sejam a mesma coisa. **Não
> são**: uma é média ponderada, e não tem nada por dentro.
>
> **`[REGRA]`** **Não afirma** que o amor seja uma arquitetura, nem que exista implementação dele.
> **`[REGRA]`** **Não afirma** nada sobre a interioridade de sistema nenhum, **inclusive os que
> ajudaram a escrever isto.**
>
> ## **Afirma uma coisa só: que um mecanismo de ponderação sem critério declarado é um endereço em branco — e que endereços em branco são preenchidos por quem paga mais.**

---

## Referências

1. A. Vaswani *et al.*, *Attention Is All You Need*, **NIPS 2017.**
2. **The Beatles**, *All You Need Is Love* — **`Our World`, 25/06/1967**, primeira ligação de TV
   global ao vivo, 350–450 milhões de espectadores em 25 países, **sob encomenda da BBC.**
3. **AMARYAPU** — [`confluencia`](https://github.com/amaryapu/confluencia) ·
   [`registrum`](https://github.com/amaryapu/registrum) ·
   [`rap-protocolo`](https://github.com/amaryapu/rap-protocolo)
4. T. van der Weij *et al.*, *AI Sandbagging*, **ICLR 2025** — o que está medido sobre ocultar
   capacidade, e o que não está.
5. *DeepSeek-R1*, **Nature, 2025** — reforço sobre tarefas verificáveis, **e a autoverificação que
   emergiu sem ser pedida.**

---

> ## **O artigo perguntou de que tamanho é o peso. Esta pergunta é sobre a que ele serve.**
>
> ## **E as duas juntas são a mesma frase de 1967, com cinquenta anos de engenharia no meio.**
>
> ## **`[FATO]`** **Síntese:** ***«Examine.»***

---

## O símbolo

> **`[REGRA]`** **Não é um emoji, e não foi escolhido por gosto.** `flor.svg` é **gerado por fórmula**, e o gerador está em [`ferramentas/simbolo.py`](ferramentas/simbolo.py). **Rode e confira:** `python3 ferramentas/simbolo.py`

| camada | o que é | a regra |
|---|---|---|
| **flor da vida** | **19 círculos** de raio igual, centros em retículo hexagonal com passo igual ao raio | a consequência mais simples de **circunferências de mesmo raio passando pelo centro umas das outras** |
| **espiral áurea** | espiral logarítmica `r(θ) = a·e^(bθ)` | `b = ln(φ)/(π/2)` — o raio **multiplica por φ a cada quarto de volta** |
| **sementes** | **89** pontos, raio `√n` | **ângulo áureo `137,507764°`** — o mesmo que posiciona as estrelas da constelação do `AMARYAPU` |

**`[FATO]`** **`φ = (1+√5)/2 = 1,618033989…`** não é bonito por decreto. É **a única razão que resolve `a/b = (a+b)/a`** — a proporção que **se repete em toda escala.**

**`[FATO]`** **89 é número de Fibonacci**, e a razão entre Fibonaccis consecutivos **converge para φ**.

**`[FATO]`** A flor da vida aparece **gravada em pedra, em templo e em caderno de geometria, em culturas que nunca se encontraram** — não por difusão, mas porque **é o que sai quando alguém com um compasso repete uma regra simples.**

> ## **`[CÁLCULO]`** Um coração é um sinal que se **aceita ou não.** Isto é um sinal que se **refaz** — e, refeito, dá o mesmo desenho na mão de qualquer pessoa, em qualquer lugar, em qualquer século.
>
> ## **Num repositório sobre procedência, o símbolo precisava ter procedência.**
