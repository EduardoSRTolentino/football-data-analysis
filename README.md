# ⚽ Football Data Analysis API

API desenvolvida em Python para análise de performance de jogadores de futebol, utilizando métricas avançadas, filtros dinâmicos e otimização de performance com cache.

---

## 🚀 Tecnologias utilizadas

- Python  
- FastAPI  
- Pandas  
- Matplotlib  
- NumPy  
- Pydantic  

---

## 📊 Funcionalidades

- 📈 Cálculo de métricas de performance:
  - **Score** → (Gols * 4 + Assistências * 3)
  - **Efficiency** → Gols por minuto jogado
  - **Advanced Score** → Métrica composta com dados normalizados

- 🏆 Ranking de jogadores

- 🎯 Filtros dinâmicos:
  - Por número mínimo de gols
  - Por número mínimo de assistências

- ⚡ Cache de dados com LRU (melhora performance)

- 📡 API REST com documentação automática

---

## 🔥 Endpoints

### 📌 Listar jogadores

GET `/players`

Parâmetros:
- `limit` (int) → quantidade de jogadores retornados  
- `min_gols` (int) → filtro mínimo de gols  
- `min_assistencias` (int) → filtro mínimo de assistências  

---

### 📌 Top jogadores

GET `/top_players`

Parâmetros:
- `metric` (str) → Score | Advanced_Score | Efficiency  
- `limit` (int) → quantidade de jogadores  
- `min_gols` (int) → filtro mínimo de gols  

---

### 📌 Atualizar cache

POST `/refresh`

Limpa o cache e força o recálculo dos dados.

---

## ▶️ Como rodar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/football-data-analysis-api.git
cd football-data-analysis-api