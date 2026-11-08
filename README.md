# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

A content-based recommender. It scores every song in `data/songs.csv` against one user profile with fixed rules, then returns the top `k`.

- **Song features used:** genre, mood, energy, valence, acousticness, danceability.
- **UserProfile stores:** favorite genre, favorite mood, and a target for each numeric feature.

```
User prefs → load 18 songs → score each song → sort (ties by title) → top k + reasons
```

### Algorithm Recipe

| Component | Points | Rule |
|---|---|---|
| Mood match | +2.0 | exact match, else 0 |
| Genre match | +1.0 | exact match, else 0 |
| Energy | 0–2.0 | `2.0 * (1 - abs(song - target))` |
| Valence | 0–1.0 | `1.0 * (1 - abs(song - target))` |
| Acousticness | 0–1.0 | `1.0 * (1 - abs(song - target))` |
| Danceability | 0–0.5 | `0.5 * (1 - abs(song - target))` |

Max is 7.5. Sort high to low, break ties by title, return the top 5, and explain each pick with its biggest contributors.

Mood outweighs genre because 14 of 18 genres appear once, so a big genre bonus would just pick "the one song in your genre."

### Expected biases

- Genre (+1.0) can lift a mediocre song over a slightly better mood/energy match.
- Exact-match labels: "relaxed" earns nothing against "chill."
- One target per user, so mixed tastes are poorly served.
- Mood and energy are over half the points, so they can outvote the other features.
- Always picking the closest songs makes a filter bubble, and 18 songs means repeats.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Output for the default pop/happy profile (`python -m src.main`):

```
Loaded songs: 18

Profile: genre=pop, mood=happy, energy=0.8
Top recommendations
============================================================
1. Sunrise City by Neon Echo
   Score: 4.96
   Reasons:
     - mood matches: happy (+2.0)
     - genre matches: pop (+1.0)
     - energy 0.82 vs target 0.80 (+1.96)
------------------------------------------------------------
2. Rooftop Lights by Indigo Parade
   Score: 3.92
   Reasons:
     - mood matches: happy (+2.0)
     - energy 0.76 vs target 0.80 (+1.92)
------------------------------------------------------------
3. Gym Hero by Max Pulse
   Score: 2.74
   Reasons:
     - genre matches: pop (+1.0)
     - energy 0.93 vs target 0.80 (+1.74)
------------------------------------------------------------
4. Concrete Crown by Verse Kingdom
   Score: 1.96
   Reasons:
     - energy 0.78 vs target 0.80 (+1.96)
------------------------------------------------------------
5. Night Drive Loop by Neon Echo
   Score: 1.90
   Reasons:
     - energy 0.75 vs target 0.80 (+1.90)
------------------------------------------------------------
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



