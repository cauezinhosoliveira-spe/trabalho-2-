atividade-fourier/
│
├── main.py
├── imagem.jpg
├── README.md
└── resultados/
    ├── espectro.png
    ├── passa_baixa.png
    ├── passa_alta.png
    └── passa_banda.png



    # Processamento de Imagens com Transformada de Fourier

## Objetivo

Este projeto tem como objetivo aplicar a Transformada de Fourier em imagens digitais e utilizar filtros no domínio da frequência para analisar seus efeitos visuais.

## Tecnologias Utilizadas

* Python
* OpenCV
* NumPy
* Matplotlib

## Imagem Utilizada

Foi utilizada uma imagem digital em escala de cinza para a realização dos experimentos.

## Transformada de Fourier

A Transformada de Fourier converte a imagem do domínio espacial para o domínio da frequência, permitindo identificar quais frequências contribuem para a formação da imagem.

## Filtros Implementados

### Filtro Passa-Baixa

Preserva as baixas frequências e remove as altas frequências.

**Efeito visual:** suavização da imagem e redução de ruídos.

### Filtro Passa-Alta

Preserva as altas frequências e remove as baixas frequências.

**Efeito visual:** realce de bordas e detalhes.

### Filtro Passa-Banda

Permite apenas uma faixa específica de frequências.

**Efeito visual:** seleção de determinados detalhes da imagem.

## Resultados

Foram observadas diferenças significativas entre os filtros aplicados, demonstrando a influência das frequências na composição visual da imagem.

## Conclusão

A Transformada de Fourier mostrou-se uma ferramenta eficiente para análise de frequências em imagens. Os filtros aplicados permitiram destacar ou remover características específicas, evidenciando a importância do processamento no domínio da frequência.
