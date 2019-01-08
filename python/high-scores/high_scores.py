class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def personal_best(self):
        return max(self.scores)

    def latest(self):
        return self.scores[-1]

    def personal_top(self):
        sorted_scores = sorted(self.scores, reverse=True)
        return sorted_scores[:3]

    def report(self):
        diff = self.personal_best() - self.latest()
        if diff > 0:
            return (f"Your latest score was {self.latest()}. That's {diff} short of your personal best!")
        return f"Your latest score was {self.personal_best()}. That's your personal best!"