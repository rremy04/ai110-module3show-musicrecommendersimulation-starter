"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


PROFILES = {
    "High-Energy Pop": {
        "genre": "pop", "mood": "happy",
        "energy": 0.90, "valence": 0.80, "acousticness": 0.10, "danceability": 0.85,
    },
    "Chill Lofi": {
        "genre": "lofi", "mood": "chill",
        "energy": 0.38, "valence": 0.58, "acousticness": 0.80, "danceability": 0.60,
    },
    "Deep Intense Rock": {
        "genre": "rock", "mood": "intense",
        "energy": 0.92, "valence": 0.40, "acousticness": 0.08, "danceability": 0.60,
    },
    # Adversarial / edge-case profiles (System Evaluation)
    "Conflicted: Sad but Energetic": {
        "genre": "classical", "mood": "sad",
        "energy": 0.90, "valence": 0.20, "acousticness": 0.95, "danceability": 0.30,
    },
    "Unknown Genre and Mood": {
        "genre": "k-pop", "mood": "bubbly",
        "energy": 0.70, "valence": 0.80, "acousticness": 0.20, "danceability": 0.80,
    },
    "Dead Center (all 0.5)": {
        "genre": "pop", "mood": "happy",
        "energy": 0.50, "valence": 0.50, "acousticness": 0.50, "danceability": 0.50,
    },
    "Out of Range (energy 2.0)": {
        "genre": "pop", "mood": "happy",
        "energy": 2.0, "valence": 0.80, "acousticness": 0.10, "danceability": 0.85,
    },
}


def show_recommendations(name: str, user_prefs: dict, songs: list, k: int = 5) -> None:
    """Print the top k recommendations for one named profile."""
    recommendations = recommend_songs(user_prefs, songs, k=k)

    print(f"\nProfile: {name}")
    print("=" * 60)
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"{rank}. {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f}")
        print("   Reasons:")
        for reason in explanation.split("; "):
            print(f"     - {reason}")
        print("-" * 60)


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    for name, user_prefs in PROFILES.items():
        show_recommendations(name, user_prefs, songs)



if __name__ == "__main__":
    main()
