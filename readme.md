# 📊 Meganium Games - Insights de Vendas Globais

Este projeto tem como objetivo consolidar e analisar os dados de vendas dos consoles fabricados pela **Meganium Games**, vendidos por terceiros em diferentes marketplaces globais.

---

## 🧭 Objetivo

Transformar dados brutos de vendas em **insights estratégicos** para a Meganium Games, identificando:

- Os **consoles mais populares** globalmente e por país;
- Tendências de crescimento de mercado;
- Correlações entre vendas e indicadores econômicos;
- Projeções de demanda por país.

---

## 🗂 Estrutura de Pastas

```text
📦 meganium-games-insights/
├── 📂 data/
│   ├── 📂 raw_data/          # Planilhas originais de vendas de Etsy, Shopee e AliExpress
│   ├── 📂 processed_data/    # Dados limpos e consolidados para análise
├── 📂 insights/              # Resultados e gráficos das análises realizadas
├── 📂 prompts/
│   └── 📄 chatgpt_prompts.md # Lista de perguntas usadas para gerar os insights
├── 📂 scripts/               # Códigos de ETL, limpeza, unificação e análise
└── 📄 readme.md              # Este arquivo de documentação
```

---

## 📄 Fontes de Dados

Os dados de vendas foram obtidos das seguintes plataformas de terceiros:

- **Etsy** (`Meganium_Sales_Data_-_Etsy.csv`)
- **Shopee** (`Meganium_Sales_Data_-_Shopee.csv`)
- **AliExpress** (`Meganium_Sales_Data_-_AliExpress.csv`)

---

## 💡 Prompts Utilizados

Os principais prompts de análise são:

1. **Volume de vendas nos últimos 12 meses**
2. **Top 1 console mais vendido no mundo**
3. **Popularidade por país (unidades e receita)**
4. **Países com maior crescimento nos últimos 3 trimestres**
5. **Projeção de demanda para o próximo semestre**

Todos estão documentados em `prompts/chatgpt_prompts.md`.

---

## 🚀 Como usar

1. Coloque os arquivos de vendas em `data/raw_data/`
2. Execute os scripts de limpeza e consolidação 
3. Acesse os relatórios consolidados em `insights/`
4. Use os prompts da IA para novas perguntas de negócio

---

## 🧠 Desenvolvido com IA

Este projeto é assistido por um modelo GPT personalizado chamado [**Sales-Report-Manager**](https://chatgpt.com/g/g-680a6b1de00c8191b43ca76986b12213-sales-report-manager), que analisa e responde com base em dados reais, sempre apresentando o raciocínio em formato de tabela.

---

