# Market Basket Analysis em Transcrições de Aulas de Tecnologia

Repositório de análises de palavras-chave e Market Basket Analysis para identificar associações entre termos técnicos em transcrições de aulas.

---

## 📂 Estrutura do Projeto
```
aplicando-market-basket/
├── data/
│   ├── keywords_dev/        # Arquivos com palavras-chave de desenvolvimento
│   ├── keywords_ed/         # Arquivos com palavras-chave de estrutura de dados
│   ├── keywords_rc/         # Arquivos com palavras-chave de redes de computadores
│   └── transcricao_video_aulas/  # Transcrições de aulas aleatórias do youtube
├── results/
│   ├── matriz_duas_combinacoes.csv  # Combinações de 2 categorias de keywords
│   ├── matriz_por_tag.csv           # Amostras por categoria (dev, ed, rc)
│   └── matriz_total.csv             # Combinações de todas as categorias
└── scripts/
│   ├── criando_datasets.py   # Gera datasets de combinações aleatórias
│   └── market_basket.py      # Aplica algoritmo Apriori e regras de associação  
│── README.md             # Documentação
└── requirements.txt      # Dependências (pandas, mlxtend)
```

---

## ⚙️ Instalação

1. Instale as dependências:
```bash
pip install -r scripts/requirements.txt
```

2. Certifique-se de que as pastas `keywords_dev`, `keywords_ed` e `keywords_rc` contenham arquivos `.txt` com uma palavra-chave por linha.

---

## 🚀 Como Usar

### Passo 1: Gerar Datasets
Execute para criar combinações de palavras-chave:
```bash
python scripts/criando_datasets.py
```
**Arquivos gerados**:
- `matriz_por_tag.csv`: Combinações por categoria.
- `matriz_duas_combinacoes.csv`: Combinações de 2 categorias.
- `matriz_total.csv`: Combinações de todas as categorias.

### Passo 2: Executar Market Basket Analysis
Identifique regras de associação entre termos:
```bash
python scripts/market_basket.py
```
**Saídas**:
- `teste.csv`: Regras de associação (suporte, confiança, lift).
- Top 5 associações para uma palavra-chave específica (ex: `back-end`).

---

## 🧩 Exemplo Prático
Para encontrar termos associados a `back-end`:
```python
# No script market_basket.py:
basket = ['back-end']
rules_filtered = rules[rules['antecedents'].apply(lambda x: set(basket).issubset(set(x)))]
print(rules_filtered.head(5))
```

**Resultado esperado** (exemplo):
| antecedents  | consequents | lift  |
|--------------|-------------|-------|
| {back-end}   | {api}       | 5.2   |
| {back-end}   | {cloud}     | 4.1   |

---

## 📌 Observações
- **Reprodutibilidade**: A semente aleatória (`random.seed(42)`) garante resultados consistentes.
- **Personalização**: Ajuste `min_support` e `min_threshold` no script `market_basket.py` para refinar as regras.
- **Dados**: Adicione transcrições de aulas em `transcricao_video_aulas` para análises futuras.
