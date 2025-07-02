from collections import Counter
text = input("enter a text:")
counter = Counter(text)
print("Characters frequencies:",dict(counter))