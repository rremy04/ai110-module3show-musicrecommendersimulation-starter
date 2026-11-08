# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0**

---

## 2. Intended Use  

VibeFinder suggests five songs from a small catalog based on one listener profile: a favorite genre, a favorite mood, and target levels for energy, brightness, acoustic sound and danceability.

It assumes a listener has one steady taste. It is for classroom exploration only.

**Not for:** real listeners, real music apps, or any decision about artists. It has 18 songs and no listening history, so it cannot be fair to everyone.

---

## 3. How the Model Works  

The recommender compares every song in the catalog to one description of what the listener wants, gives each song points, and shows the highest scorers.

A song earns points in six ways:

- **Mood:** 2 points if it matches the listener's favorite mood, otherwise none.
- **Genre:** 1 point if it matches the favorite genre, otherwise none.
- **Energy:** up to 2 points, more the closer the song's energy is to what the listener wants.
- **Valence (how bright or dark it sounds):** up to 1 point, using the same closeness idea.
- **Acousticness (organic vs. electronic):** up to 1 point, using the same closeness idea.
- **Danceability:** up to half a point, since it mostly repeats energy.

Closeness works like a ruler: a perfect match gets full points, and points shrink as the gap grows. A song that is too low and a song that is too high are treated the same.

Mood counts for more than genre because mood is how a song feels, and people will cross genres to get that feeling. Most genres appear only once in the catalog, so a big genre bonus would just pick that one song.

After scoring every song, the system sorts from highest to lowest, breaks ties alphabetically by title, and returns the top five. Each pick comes with the reasons that earned its points, such as "mood matches: happy (+2.0)".

Changes from the starter: the starter returned the first songs in the file with a placeholder explanation. This version loads the CSV, scores every song, ranks them, and explains each result.

---

## 4. Data  

The catalog is `data/songs.csv`. It has 18 songs, each with genre, mood, energy, tempo, valence, danceability and acousticness.

There are 15 genres and 14 moods. Most genres and moods show up only once. Lofi (3 songs) and chill (3 songs) are the biggest groups, and pop has 2.

I did not add or remove songs. Missing from the data: lyrics, language, artist popularity, year, and anything about what a person has actually listened to.

---

## 5. Strengths  

It works well when the listener's taste is clear and the labels line up. Chill Lofi and Deep Intense Rock both got lists I would agree with.

It separates very different tastes. The Chill Lofi and Deep Intense Rock lists share no songs.

Every pick comes with reasons, so it is easy to see why a song ranked where it did.

---

## 6. Limitations and Bias 

The biggest weakness I found is that the system matches labels as exact words, so near-synonyms count as total misses. My "sad but energetic" test user asked for mood "sad," but the catalog's closest song is labeled "melancholic," so no song earned the 2-point mood bonus. The top pick, Moonlit Sonata, won only on genre plus acousticness and valence, even though its energy (0.22) is nowhere near the 0.90 the user wanted. A second weakness is that the catalog is tiny (18 songs, 14 genres appearing once), so a genre or mood the user names often matches just one song, and high-energy fans keep getting the same few songs (Gym Hero, Storm Runner, Pulse Horizon). Finally, a target outside 0 to 1 (like energy 2.0) is not rejected; it quietly produces negative points instead of an error.

---

## 7. Evaluation  

**Profiles tested.** Three normal users (High-Energy Pop, Chill Lofi, Deep Intense Rock) and four adversarial ones: Sad but Energetic (conflicting wishes), Unknown Genre and Mood (k-pop / "bubbly," which are not in the catalog), Dead Center (every target 0.5), and Out of Range (energy 2.0). Full top-5 terminal output is in the README under "System Evaluation."

**Do the results feel right?** For the normal profiles, yes. Chill Lofi returns the three lofi songs plus ambient and jazz, all quiet and acoustic, which is what I would expect. Deep Intense Rock puts Storm Runner first by a wide margin, and metal (Iron Requiem) is third, which makes sense musically.

**Why Gym Hero keeps showing up for Happy Pop fans.** Gym Hero is pop but its mood is "intense," not "happy," so it gets no mood points. It still ranks third for the High-Energy Pop profile (5.35) because it is pop (+1.0) and its energy, brightness and electronic sound are almost exactly what that listener asked for (about 4.3 points from closeness). In plain terms: the system sees "pop, loud, upbeat, danceable" and does not know the song is a workout track rather than a happy one. Mood is a single yes/no, so a wrong mood only costs 2 points and strong numbers can cover it.

**Surprises.**
- Sad but Energetic: no song is labeled "sad," so the classical song with the right genre and sound won even though it is the opposite of high energy. Iron Requiem and Storm Runner (energy match, wrong everything else) were close behind.
- Unknown Genre and Mood: with no label matches possible, the top five scores are within 0.3 points of each other (4.21 to 3.93), so the ranking is basically a coin flip on small numeric gaps.
- Out of Range: energy 2.0 gave negative energy points (e.g. -0.36 for Sunrise City) but the order stayed sensible, so the bad input was not caught.

**Experiment: weight shift.** I doubled the energy weight (2.0 to 4.0) and halved the genre bonus (1.0 to 0.5); the maximum score goes from 7.5 to 9.0 and nothing can go negative for valid targets. The normal profiles barely changed, and the conflicted profile changed the most (Moonlit Sonata dropped from 1st to out of the top 5 while Iron Requiem took 1st). The change made the output different, not clearly more accurate: it fixed the "sad but energetic" case only by trusting the energy number over the user's other stated tastes. I reverted it afterward.

**Profile-by-profile comparisons.**
- *High-Energy Pop vs. Chill Lofi:* nearly opposite lists. Pop gets bright, loud, electronic songs (Sunrise City, Pulse Horizon); lofi gets quiet, acoustic ones (Library Rain, Spacewalk Thoughts). That is exactly what the energy and acousticness targets are testing.
- *High-Energy Pop vs. Deep Intense Rock:* both want high energy, so Gym Hero and Pulse Horizon appear in both. The difference is the top: mood "happy" brings Sunrise City and Rooftop Lights, mood "intense" brings Storm Runner, and a lower valence target pulls in darker songs like Iron Requiem.
- *Chill Lofi vs. Deep Intense Rock:* no overlap at all, which is a good sign the scoring separates very different tastes.
- *Sad but Energetic vs. Chill Lofi:* both like acoustic, low-valence songs, but the conflicted user's high energy pulls in Iron Requiem and Storm Runner, which a calm listener would never see.
- *Unknown Genre and Mood vs. High-Energy Pop:* both still lead with Rooftop Lights and Sunrise City, because their numbers (bright, danceable, fairly energetic) fit. The difference is below them: with no mood or genre bonus available, Concrete Crown, Night Drive Loop and Island Breeze fill the list on small numeric gaps instead of Gym Hero.
- *Dead Center vs. Out of Range:* both still list Sunrise City and Rooftop Lights first because the happy/pop labels are the same; Dead Center's lower targets add mid-energy songs (Velvet Hours, Dusty Back Road) while Out of Range keeps the loud ones.

---

## 8. Future Work  

- Treat close moods as partly matching, so "sad" gets some credit for "melancholic."
- Reject or clamp targets outside 0 to 1.
- Add a diversity rule so the top five are not all near-copies of one song.
- Let a user have two tastes, like gym music and study music, instead of one target.

---

## 9. Personal Reflection  

The biggest thing I learned is that the weights are opinions. I picked mood = 2 points and genre = 1 point because it felt right, and then a "sad" test user got no mood points at all because the dataset says "melancholic." Nothing was broken. The rules just did what I told them.

AI tools were good for getting the structure up fast and for thinking of strange test profiles. I still had to read the actual scores myself. The tests passed the whole time, but they would never have told me that an energy of 2.0 gives negative points. I only saw that by reading the output.

What surprised me is how much it feels like a real recommender. Chill Lofi gave me a playlist I would actually use, and it is just addition and subtraction. Then Gym Hero showed up for the happy pop listener and I could see how a feed can feel almost right and still be off.

Next I would try the mood fix first, then let one user have two profiles. I want to see if the Gym Hero problem goes away.

Overall, this was truly a fun project to work on as someone who loves Spotify so getting to work on something like this was exciting
