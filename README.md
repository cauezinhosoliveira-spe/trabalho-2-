# 🔬 Processamento de Imagens com Transformada de Fourier e Filtros

> Atividade 02 — Disciplina de Processamento de Imagens  
> Tema: Transformada de Fourier e Filtros no Domínio da Frequência

---

## 📋 Descrição do Projeto

Este projeto implementa análise e processamento de imagens utilizando a **Transformada de Fourier** e **filtros no domínio da frequência** com Python. O objetivo é demonstrar visualmente como diferentes frequências compõem uma imagem e como filtros específicos podem remover ou preservar informações visuais relevantes.

---

## 🎯 Objetivos

- Aplicar a Transformada de Fourier em uma imagem para análise no domínio da frequência
- Visualizar o espectro de Fourier e interpretar suas informações
- Implementar e comparar três tipos de filtros: **passa-baixa**, **passa-alta** e **rejeita-banda**
- Analisar o impacto visual de cada filtro sobre a imagem original

---

## 🗂️ Estrutura do Repositório

```
📁 projeto-fourier/
│
├── 📄 README.md               # Documentação do projeto
├── 📄 main.py                 # Código principal com todos os filtros
├── 📁 imagens/
│   ├── imagem_original.jpg    # Imagem utilizada no projeto
│   └── resultados/
│       ├── espectro_fourier.png
│       ├── filtro_passa_baixa.png
│       ├── filtro_passa_alta.png
│       └── filtro_rejeita_banda.png
└── 📄 requirements.txt        # Dependências do projeto
```

---

## 🛠️ Tecnologias Utilizadas

| Biblioteca   | Versão   | Finalidade                          |
|--------------|----------|-------------------------------------|
| Python       | 3.10+    | Linguagem base do projeto           |
| OpenCV       | 4.x      | Leitura e manipulação de imagens    |
| NumPy        | 1.x      | Operações matemáticas e FFT         |
| Matplotlib   | 3.x      | Visualização dos resultados         |

---

## ⚙️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/projeto-fourier.git
cd projeto-fourier
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Execute o código principal

```bash
python main.py
```

O script irá gerar e exibir automaticamente os resultados de cada filtro, além de salvar as imagens na pasta `imagens/resultados/`.

---

## 📡 O que é a Transformada de Fourier?

A **Transformada de Fourier** decompõe uma imagem do **domínio espacial** (pixels) para o **domínio da frequência**. No espectro resultante:

- O **centro** representa as **baixas frequências** — responsáveis pelas variações suaves de cor e iluminação (informações globais da imagem).
- As **bordas** representam as **altas frequências** — responsáveis pelos detalhes finos, bordas e texturas (mudanças abruptas de intensidade).

O espectro é exibido em escala logarítmica para facilitar a visualização, já que os coeficientes de baixa frequência têm magnitude muito maior.

---

## 🔎 Filtros Implementados

### 1. Filtro Passa-Baixa (Suavização)

**O que faz:** Permite a passagem apenas das baixas frequências, bloqueando as altas.

**Implementação:** Máscara circular centrada no espectro, com raio definido pelo limiar de corte.

**Efeito visual:** A imagem fica **borrada/suavizada**, pois os detalhes finos (bordas e texturas) são removidos. Ruídos de alta frequência também são eliminados — técnica base para desfoque gaussiano.

---

### 2. Filtro Passa-Alta (Realce de Bordas)

**O que faz:** Bloqueia as baixas frequências e preserva as altas.

**Implementação:** Inverso do passa-baixa — mascara o centro do espectro.

**Efeito visual:** Somente as **bordas e detalhes** da imagem permanecem visíveis. O fundo fica escuro. É a base de técnicas de detecção de contornos e nitidez.

---

### 3. Filtro Rejeita-Banda (Notch / Banda de Rejeição)

**O que faz:** Bloqueia uma faixa específica de frequências, preservando o resto.

**Implementação:** Máscara em forma de anel — remove as frequências entre dois raios definidos.

**Efeito visual:** Remove padrões periódicos específicos da imagem (como ruídos de varredura ou texturas repetitivas), mantendo tanto as estruturas globais quanto os detalhes finos.

---

## 📊 Comparação dos Resultados

| Filtro          | Frequências Preservadas | Frequências Removidas | Efeito Visual              |
|-----------------|-------------------------|-----------------------|----------------------------|
| Passa-Baixa     | Baixas (centro)         | Altas (bordas)        | Imagem suavizada / borrada |
| Passa-Alta      | Altas (bordas)          | Baixas (centro)       | Bordas realçadas           |
| Rejeita-Banda   | Baixas e altas          | Faixa intermediária   | Remoção de padrões         |

**Melhor resultado:** O **filtro passa-baixa** apresentou o resultado mais visualmente impactante para demonstrar o princípio da Transformada de Fourier, pois a suavização progressiva evidencia claramente a relação entre frequências removidas e perda de detalhes na imagem.

---

## 📸 Resultados

| Original | Espectro de Fourier |
|----------|---------------------|
| *(imagem_original.jpg)* | *(espectro_fourier.png)* |

| Passa-Baixa | Passa-Alta | Rejeita-Banda |
|-------------|------------|---------------|
| *(filtro_passa_baixa.png)* | *(filtro_passa_alta.png)* | *(filtro_rejeita_banda.png)* |

> Os arquivos de resultado são gerados automaticamente ao executar `main.py`.

---

## 📚 Referências

- Gonzalez, R. C.; Woods, R. E. — *Processamento Digital de Imagens*, 3ª ed.
- Documentação oficial do [OpenCV](https://docs.opencv.org/)
- Documentação oficial do [NumPy — FFT](https://numpy.org/doc/stable/reference/routines.fft.html)

---

## 👤 Autor

**Cauê Soares de Oliveira**  
Curso: Ciencias da computação  
Instituição: Anhanguera  
Período: 7° Semestre
