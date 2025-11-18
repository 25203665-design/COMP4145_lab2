import math
from collections import Counter

# Documents
D1 = "Python is an easy programming language with good readability"
D2 = "Java is a simple programming language with strong security"

# Preprocess: lowercase and split
d1_words = D1.lower().split()
d2_words = D2.lower().split()

# Unique words across both
all_words = set(d1_words + d2_words)

# Corpus size
N = 2

# Compute TF for each document
tf_d1 = Counter(d1_words)
tf_d2 = Counter(d2_words)

# Compute DF (document frequency)
df = {}
for word in all_words:
    df[word] = (1 if word in tf_d1 else 0) + (1 if word in tf_d2 else 0)

# Compute IDF
idf = {word: math.log(N / df[word]) for word in all_words}

# Compute TF-IDF
tfidf_d1 = {word: tf_d1.get(word, 0) * idf[word] for word in all_words}
tfidf_d2 = {word: tf_d2.get(word, 0) * idf[word] for word in all_words}

# Print TF-IDF table
print("(a) TF-IDF for each unique word:")
print(f"{'Word':<15} {'TF-D1':<6} {'IDF':<8} {'TF-IDF D1':<10} {'TF-D2':<6} {'TF-IDF D2':<10}")
for word in sorted(all_words):
    print(f"{word:<15} {tf_d1.get(word, 0):<6} {idf[word]:<8.4f} {tfidf_d1[word]:<10.4f} {tf_d2.get(word, 0):<6} {tfidf_d2[word]:<10.4f}")

# (b) Cosine similarity using TF vectors
def cosine_similarity(vec1, vec2, words):
    dot_product = sum(vec1.get(word, 0) * vec2.get(word, 0) for word in words)
    norm1 = math.sqrt(sum(vec1.get(word, 0)**2 for word in words))
    norm2 = math.sqrt(sum(vec2.get(word, 0)**2 for word in words))
    if norm1 == 0 or norm2 == 0:
        return 0.0
    return dot_product / (norm1 * norm2)

cos_sim = cosine_similarity(tf_d1, tf_d2, all_words)
print(f"\n(b) Cosine Similarity between D1 and D2 using TF: {cos_sim:.4f}")

# (c) Stop word removal
stop_words = ["is", "a"]
d1_filtered = [word for word in d1_words if word not in stop_words]
d2_filtered = [word for word in d2_words if word not in stop_words]

tf_d1_filtered = Counter(d1_filtered)
tf_d2_filtered = Counter(d2_filtered)

all_words_filtered = set(d1_filtered + d2_filtered)

cos_sim_filtered = cosine_similarity(tf_d1_filtered, tf_d2_filtered, all_words_filtered)
print(f"\n(c) Cosine Similarity after removing stop words '{stop_words}': {cos_sim_filtered:.4f}")
print("\n(c) Discussion: Stop word removal eliminates common words that do not carry significant meaning, reducing noise in similarity calculations.")
print(f"Before removal, cosine similarity was {cos_sim:.4f}, which considers all words including 'is' and 'a'.")
print(f"After removal, similarity decreased to {cos_sim_filtered:.4f}, as it focuses on content words like 'programming' and 'language', highlighting shared concepts.")
print("In this case, removing stop words slightly decreased the similarity because the shared stop words contributed to the dot product.")
