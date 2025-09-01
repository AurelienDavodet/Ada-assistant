# 🤖 Ada - Perso AI Assistant

Un **assistant personnel multi-agents** construit avec [LangGraph](https://github.com/langchain-ai/langgraph) et [Chainlit](https://www.chainlit.io/).
Il agit comme un **majordome numérique** : il peut préparer ton digest du matin, donner la météo, convertir des devises, suivre la bourse, sortir des blagues, vérifier le trafic RATP et bien plus.

---

## ✨ Fonctionnalités

* 🗓️ **Morning Buddy** : digest du matin (date, heure, météo, 2–3 actus, citation motivante).
* 📰 Actus en France (via **GNews**).
* 🌦️ Météo à la journée, demain ou la semaine (via **Open-Meteo**).
* 💸 Conversion de devises, cours boursiers, prix crypto.
* 🚇 Infos trafic RATP.
* 🤓 Anecdotes et citations motivantes.
* 🔎 Recherche Web (DuckDuckGo).

---

## 📂 Structure du projet

```
perso_ai_agents/
│
├── app.py                   # Entrée Chainlit (chat UI)
├── llm_loader.py            # Config du LLM (Mistral / OpenAI)
│
├── my_assistant/            # Cœur de l’assistant
│   ├── agents.py             # Définition des sous-agents
│   ├── graph.py              # Assemblage du graphe (assistant_graph)
│   ├── router.py             # Routage rule-based
│   └── prompts/              # Prompts séparés (si besoin)
│
├── tools/                   # Tous les outils (regroupés par domaine)
│   ├── time_tools.py
│   ├── weather_tools.py
│   ├── news_tools.py
│   ├── finance_tools.py
│   ├── transport_tools.py
│   ├── fun_tools.py
│   └── summary_tools.py
│
├── tests/                   # Tests unitaires
│
├── .env                     # Clés API & config
├── requirements.txt          # Dépendances
└── README.md
```

---

## 🔧 Installation

### 1. Cloner le repo

```bash
git clone https://github.com/ton-compte/perso_ai_agents.git
cd perso_ai_agents
```

### 2. Créer un environnement Python

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer les clés API

Créer un fichier `.env` à la racine :

```env
# Clé LLM
MISTRAL_API_KEY=ta_clef_mistral
# ou
OPENAI_API_KEY=ta_clef_openai

# GNews API pour les actualités
GNEWS_API_KEY=ta_clef_gnews
```

---

## 🚀 Lancer l’assistant

### Avec Chainlit

```bash
chainlit run app.py -w
```

➡️ Ouvre ensuite [http://localhost:8000](http://localhost:8000) dans ton navigateur.

---

## 🧪 Tests

Exemple pour tester les outils individuellement :

```bash
pytest tests/
```

---

## 🔮 Roadmap

* [ ] Ajouter d’autres sous-agents spécialisés (ex : Coach Sportif, Nutrition).
* [ ] Améliorer le routage avec un LLM superviseur (au lieu de règles).
* [ ] Ajouter le streaming token-par-token dans Chainlit.

---

## 👨‍💻 Crédit

Projet perso d’**Aurélien**, propulsé par LangGraph + Chainlit.
