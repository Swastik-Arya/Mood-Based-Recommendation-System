import pandas as pd
import random

class Recommender:
    def __init__(self):
        self.df = pd.read_csv("data.csv", encoding='utf-8')

        # Clean columns
        self.df.columns = self.df.columns.str.strip()
        for col in ["Mood", "Type", "Language", "Era"]:
            self.df[col] = self.df[col].astype(str).str.strip()

        self.history = set()

    def filter_data(self, mood, category, language, reason=None):
        # NEW LOGIC
        if mood == "Sad" and reason:
            mood = f"Sad_{reason}"

        return self.df[
            (self.df["Mood"] == mood) &
            (self.df["Type"] == category) &
            (self.df["Language"] == language)
        ]

    def pick_items(self, items, count):
        items = [x for x in items if x not in self.history]
        random.shuffle(items)
        return items[:count]

    def get_recommendations(self, mood, category, language, reason=None):
        data = self.filter_data(mood, category, language, reason)

        if data.empty:
            return ["No recommendations found"]

        old = data[data["Era"] == "Old"]["Title"].tolist()
        mid = data[data["Era"] == "Mid"]["Title"].tolist()
        new = data[data["Era"] == "New"]["Title"].tolist()

        selected_old = self.pick_items(old, 5)
        selected_mid = self.pick_items(mid, 5)
        selected_new = self.pick_items(new, 5)

        results = selected_old + selected_mid + selected_new

        if len(results) < 15:
            remaining = data["Title"].tolist()
            random.shuffle(remaining)
            results = remaining[:15]

        self.history.update(results)
        return results