import seaborn as sns

data = ["A", "A", "B", "A",
        "B", "B", "C", "C"]
group = ["G1", "G1", "G2", "G2",
         "G1", "G2", "G1", "G2"]

# Count plot
sns.countplot(x = data, hue = group)
