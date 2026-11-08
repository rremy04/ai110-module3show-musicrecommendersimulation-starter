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

## System Evaluation: Profile Test Output

All runs use `python -m src.main` on the 18-song catalog. The first three profiles are normal users; the last four are adversarial/edge cases designed to trick the scoring.

```
Profile: High-Energy Pop
============================================================
1. Sunrise City by Neon Echo
   Score: 7.19
   Reasons:
     - mood matches: happy (+2.0)
     - genre matches: pop (+1.0)
     - energy 0.82 vs target 0.90 (+1.84)
     - valence 0.84 vs target 0.80 (+0.96)
     - acousticness 0.18 vs target 0.10 (+0.92)
     - danceability 0.79 vs target 0.85 (+0.47)
------------------------------------------------------------
2. Rooftop Lights by Indigo Parade
   Score: 5.95
   Reasons:
     - mood matches: happy (+2.0)
     - energy 0.76 vs target 0.90 (+1.72)
     - valence 0.81 vs target 0.80 (+0.99)
     - acousticness 0.35 vs target 0.10 (+0.75)
     - danceability 0.82 vs target 0.85 (+0.48)
------------------------------------------------------------
3. Gym Hero by Max Pulse
   Score: 5.35
   Reasons:
     - genre matches: pop (+1.0)
     - energy 0.93 vs target 0.90 (+1.94)
     - valence 0.77 vs target 0.80 (+0.97)
     - acousticness 0.05 vs target 0.10 (+0.95)
     - danceability 0.88 vs target 0.85 (+0.48)
------------------------------------------------------------
4. Pulse Horizon by Kilo Flare
   Score: 4.29
   Reasons:
     - energy 0.95 vs target 0.90 (+1.90)
     - valence 0.79 vs target 0.80 (+0.99)
     - acousticness 0.03 vs target 0.10 (+0.93)
     - danceability 0.90 vs target 0.85 (+0.47)
------------------------------------------------------------
5. Storm Runner by Voltline
   Score: 4.07
   Reasons:
     - energy 0.91 vs target 0.90 (+1.98)
     - valence 0.48 vs target 0.80 (+0.68)
     - acousticness 0.10 vs target 0.10 (+1.00)
     - danceability 0.66 vs target 0.85 (+0.41)
------------------------------------------------------------
```

```
Profile: Chill Lofi
============================================================
1. Library Rain by Paper Lanterns
   Score: 7.35
   Reasons:
     - mood matches: chill (+2.0)
     - genre matches: lofi (+1.0)
     - energy 0.35 vs target 0.38 (+1.94)
     - valence 0.60 vs target 0.58 (+0.98)
     - acousticness 0.86 vs target 0.80 (+0.94)
     - danceability 0.58 vs target 0.60 (+0.49)
------------------------------------------------------------
2. Midnight Coding by LoRoom
   Score: 7.30
   Reasons:
     - mood matches: chill (+2.0)
     - genre matches: lofi (+1.0)
     - energy 0.42 vs target 0.38 (+1.92)
     - valence 0.56 vs target 0.58 (+0.98)
     - acousticness 0.71 vs target 0.80 (+0.91)
     - danceability 0.62 vs target 0.60 (+0.49)
------------------------------------------------------------
3. Spacewalk Thoughts by Orbit Bloom
   Score: 6.01
   Reasons:
     - mood matches: chill (+2.0)
     - energy 0.28 vs target 0.38 (+1.80)
     - valence 0.65 vs target 0.58 (+0.93)
     - acousticness 0.92 vs target 0.80 (+0.88)
     - danceability 0.41 vs target 0.60 (+0.41)
------------------------------------------------------------
4. Focus Flow by LoRoom
   Score: 5.43
   Reasons:
     - genre matches: lofi (+1.0)
     - energy 0.40 vs target 0.38 (+1.96)
     - valence 0.59 vs target 0.58 (+0.99)
     - acousticness 0.78 vs target 0.80 (+0.98)
     - danceability 0.60 vs target 0.60 (+0.50)
------------------------------------------------------------
5. Coffee Shop Stories by Slow Stereo
   Score: 4.23
   Reasons:
     - energy 0.37 vs target 0.38 (+1.98)
     - valence 0.71 vs target 0.58 (+0.87)
     - acousticness 0.89 vs target 0.80 (+0.91)
     - danceability 0.54 vs target 0.60 (+0.47)
------------------------------------------------------------
```

```
Profile: Deep Intense Rock
============================================================
1. Storm Runner by Voltline
   Score: 7.35
   Reasons:
     - mood matches: intense (+2.0)
     - genre matches: rock (+1.0)
     - energy 0.91 vs target 0.92 (+1.98)
     - valence 0.48 vs target 0.40 (+0.92)
     - acousticness 0.10 vs target 0.08 (+0.98)
     - danceability 0.66 vs target 0.60 (+0.47)
------------------------------------------------------------
2. Gym Hero by Max Pulse
   Score: 5.94
   Reasons:
     - mood matches: intense (+2.0)
     - energy 0.93 vs target 0.92 (+1.98)
     - valence 0.77 vs target 0.40 (+0.63)
     - acousticness 0.05 vs target 0.08 (+0.97)
     - danceability 0.88 vs target 0.60 (+0.36)
------------------------------------------------------------
3. Iron Requiem by Black Tundra
   Score: 4.08
   Reasons:
     - energy 0.97 vs target 0.92 (+1.90)
     - valence 0.20 vs target 0.40 (+0.80)
     - acousticness 0.04 vs target 0.08 (+0.96)
     - danceability 0.45 vs target 0.60 (+0.43)
------------------------------------------------------------
4. Night Drive Loop by Neon Echo
   Score: 3.86
   Reasons:
     - energy 0.75 vs target 0.92 (+1.66)
     - valence 0.49 vs target 0.40 (+0.91)
     - acousticness 0.22 vs target 0.08 (+0.86)
     - danceability 0.73 vs target 0.60 (+0.43)
------------------------------------------------------------
5. Pulse Horizon by Kilo Flare
   Score: 3.85
   Reasons:
     - energy 0.95 vs target 0.92 (+1.94)
     - valence 0.79 vs target 0.40 (+0.61)
     - acousticness 0.03 vs target 0.08 (+0.95)
     - danceability 0.90 vs target 0.60 (+0.35)
------------------------------------------------------------
```

```
Profile: Conflicted: Sad but Energetic
============================================================
1. Moonlit Sonata by Clara Wren
   Score: 4.07
   Reasons:
     - genre matches: classical (+1.0)
     - energy 0.22 vs target 0.90 (+0.64)
     - valence 0.25 vs target 0.20 (+0.95)
     - acousticness 0.97 vs target 0.95 (+0.98)
     - danceability 0.30 vs target 0.30 (+0.50)
------------------------------------------------------------
2. Iron Requiem by Black Tundra
   Score: 3.38
   Reasons:
     - energy 0.97 vs target 0.90 (+1.86)
     - valence 0.20 vs target 0.20 (+1.00)
     - acousticness 0.04 vs target 0.95 (+0.09)
     - danceability 0.45 vs target 0.30 (+0.42)
------------------------------------------------------------
3. Storm Runner by Voltline
   Score: 3.17
   Reasons:
     - energy 0.91 vs target 0.90 (+1.98)
     - valence 0.48 vs target 0.20 (+0.72)
     - acousticness 0.10 vs target 0.95 (+0.15)
     - danceability 0.66 vs target 0.30 (+0.32)
------------------------------------------------------------
4. Night Drive Loop by Neon Echo
   Score: 2.97
   Reasons:
     - energy 0.75 vs target 0.90 (+1.70)
     - valence 0.49 vs target 0.20 (+0.71)
     - acousticness 0.22 vs target 0.95 (+0.27)
     - danceability 0.73 vs target 0.30 (+0.29)
------------------------------------------------------------
5. Dusty Back Road by Hollis Creek
   Score: 2.86
   Reasons:
     - energy 0.51 vs target 0.90 (+1.22)
     - valence 0.68 vs target 0.20 (+0.52)
     - acousticness 0.74 vs target 0.95 (+0.79)
     - danceability 0.64 vs target 0.30 (+0.33)
------------------------------------------------------------
```

```
Profile: Unknown Genre and Mood
============================================================
1. Rooftop Lights by Indigo Parade
   Score: 4.21
   Reasons:
     - energy 0.76 vs target 0.70 (+1.88)
     - valence 0.81 vs target 0.80 (+0.99)
     - acousticness 0.35 vs target 0.20 (+0.85)
     - danceability 0.82 vs target 0.80 (+0.49)
------------------------------------------------------------
2. Sunrise City by Neon Echo
   Score: 4.20
   Reasons:
     - energy 0.82 vs target 0.70 (+1.76)
     - valence 0.84 vs target 0.80 (+0.96)
     - acousticness 0.18 vs target 0.20 (+0.98)
     - danceability 0.79 vs target 0.80 (+0.49)
------------------------------------------------------------
3. Concrete Crown by Verse Kingdom
   Score: 4.05
   Reasons:
     - energy 0.78 vs target 0.70 (+1.84)
     - valence 0.62 vs target 0.80 (+0.82)
     - acousticness 0.12 vs target 0.20 (+0.92)
     - danceability 0.85 vs target 0.80 (+0.48)
------------------------------------------------------------
4. Night Drive Loop by Neon Echo
   Score: 4.04
   Reasons:
     - energy 0.75 vs target 0.70 (+1.90)
     - valence 0.49 vs target 0.80 (+0.69)
     - acousticness 0.22 vs target 0.20 (+0.98)
     - danceability 0.73 vs target 0.80 (+0.46)
------------------------------------------------------------
5. Island Breeze by Sun Rootz
   Score: 3.93
   Reasons:
     - energy 0.58 vs target 0.70 (+1.76)
     - valence 0.88 vs target 0.80 (+0.92)
     - acousticness 0.45 vs target 0.20 (+0.75)
     - danceability 0.80 vs target 0.80 (+0.50)
------------------------------------------------------------
```

```
Profile: Dead Center (all 0.5)
============================================================
1. Sunrise City by Neon Echo
   Score: 6.05
   Reasons:
     - mood matches: happy (+2.0)
     - genre matches: pop (+1.0)
     - energy 0.82 vs target 0.50 (+1.36)
     - valence 0.84 vs target 0.50 (+0.66)
     - acousticness 0.18 vs target 0.50 (+0.68)
     - danceability 0.79 vs target 0.50 (+0.35)
------------------------------------------------------------
2. Rooftop Lights by Indigo Parade
   Score: 5.36
   Reasons:
     - mood matches: happy (+2.0)
     - energy 0.76 vs target 0.50 (+1.48)
     - valence 0.81 vs target 0.50 (+0.69)
     - acousticness 0.35 vs target 0.50 (+0.85)
     - danceability 0.82 vs target 0.50 (+0.34)
------------------------------------------------------------
3. Velvet Hours by Amara Sky
   Score: 4.07
   Reasons:
     - energy 0.48 vs target 0.50 (+1.96)
     - valence 0.66 vs target 0.50 (+0.84)
     - acousticness 0.38 vs target 0.50 (+0.88)
     - danceability 0.72 vs target 0.50 (+0.39)
------------------------------------------------------------
4. Midnight Coding by LoRoom
   Score: 4.01
   Reasons:
     - energy 0.42 vs target 0.50 (+1.84)
     - valence 0.56 vs target 0.50 (+0.94)
     - acousticness 0.71 vs target 0.50 (+0.79)
     - danceability 0.62 vs target 0.50 (+0.44)
------------------------------------------------------------
5. Dusty Back Road by Hollis Creek
   Score: 3.99
   Reasons:
     - energy 0.51 vs target 0.50 (+1.98)
     - valence 0.68 vs target 0.50 (+0.82)
     - acousticness 0.74 vs target 0.50 (+0.76)
     - danceability 0.64 vs target 0.50 (+0.43)
------------------------------------------------------------
```

```
Profile: Out of Range (energy 2.0)
============================================================
1. Sunrise City by Neon Echo
   Score: 4.99
   Reasons:
     - mood matches: happy (+2.0)
     - genre matches: pop (+1.0)
     - energy 0.82 vs target 2.00 (+-0.36)
     - valence 0.84 vs target 0.80 (+0.96)
     - acousticness 0.18 vs target 0.10 (+0.92)
     - danceability 0.79 vs target 0.85 (+0.47)
------------------------------------------------------------
2. Rooftop Lights by Indigo Parade
   Score: 3.74
   Reasons:
     - mood matches: happy (+2.0)
     - energy 0.76 vs target 2.00 (+-0.48)
     - valence 0.81 vs target 0.80 (+0.99)
     - acousticness 0.35 vs target 0.10 (+0.75)
     - danceability 0.82 vs target 0.85 (+0.48)
------------------------------------------------------------
3. Gym Hero by Max Pulse
   Score: 3.27
   Reasons:
     - genre matches: pop (+1.0)
     - energy 0.93 vs target 2.00 (+-0.14)
     - valence 0.77 vs target 0.80 (+0.97)
     - acousticness 0.05 vs target 0.10 (+0.95)
     - danceability 0.88 vs target 0.85 (+0.48)
------------------------------------------------------------
4. Pulse Horizon by Kilo Flare
   Score: 2.29
   Reasons:
     - energy 0.95 vs target 2.00 (+-0.10)
     - valence 0.79 vs target 0.80 (+0.99)
     - acousticness 0.03 vs target 0.10 (+0.93)
     - danceability 0.90 vs target 0.85 (+0.47)
------------------------------------------------------------
5. Storm Runner by Voltline
   Score: 1.91
   Reasons:
     - energy 0.91 vs target 2.00 (+-0.18)
     - valence 0.48 vs target 0.80 (+0.68)
     - acousticness 0.10 vs target 0.10 (+1.00)
     - danceability 0.66 vs target 0.85 (+0.41)
------------------------------------------------------------
```

---

## Experiments You Tried

**Weight shift:** energy weight 2.0 -> 4.0 and genre bonus 1.0 -> 0.5 (max score 7.5 -> 9.0; every term still non-negative for targets in 0-1, so the math stays valid). Reverted afterward.

| Profile | Baseline top 5 | After weight shift |
|---|---|---|
| High-Energy Pop | Sunrise City, Rooftop Lights, Gym Hero, Pulse Horizon, Storm Runner | same order |
| Chill Lofi | Library Rain, Midnight Coding, Spacewalk, Focus Flow, Coffee Shop | same order |
| Deep Intense Rock | Storm Runner, Gym Hero, Iron Requiem, Night Drive Loop, Pulse Horizon | Storm Runner, Gym Hero, Iron Requiem, Pulse Horizon, Concrete Crown |
| Sad but Energetic | **Moonlit Sonata**, Iron Requiem, Storm Runner, Night Drive, Dusty Back Road | **Iron Requiem**, Storm Runner, Night Drive, Gym Hero, Sunrise City |
| Unknown Genre and Mood | Rooftop, Sunrise, Concrete Crown, Night Drive, Island Breeze | Rooftop, Sunrise, Night Drive, Concrete Crown, Island Breeze |
| Dead Center | Sunrise, Rooftop, Velvet Hours, Midnight Coding, Dusty Back Road | Sunrise, Rooftop, Velvet Hours, Dusty Back Road, Midnight Coding |
| Out of Range | Sunrise, Rooftop, Gym Hero, Pulse Horizon, Storm Runner | same order |

Result: different, not clearly more accurate. Normal profiles barely moved (their winners already matched on energy). The only big change was the conflicted profile: Moonlit Sonata (a very low-energy song) fell out of first place, so the energy number "won" over the genre/acoustic taste the user also stated. Whether that is better depends on which signal the user meant.


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



