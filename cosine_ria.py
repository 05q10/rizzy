import math

# Given vectors
A = [1, 2, 3]
B = [2, 3, 4]

# -----------------------------
# Step 1: Compute Dot Product
# -----------------------------
dot_product = 0

for i in range(len(A)):
    dot_product += A[i] * B[i]

# -----------------------------
# Step 2: Compute Magnitudes
# -----------------------------
magnitude_A = 0
magnitude_B = 0

for value in A:
    magnitude_A += value ** 2

for value in B:
    magnitude_B += value ** 2

magnitude_A = math.sqrt(magnitude_A)
magnitude_B = math.sqrt(magnitude_B)

# -----------------------------
# Step 3: Compute Cosine Similarity
# -----------------------------
cosine_similarity = dot_product / (magnitude_A * magnitude_B)

# -----------------------------
# Display Results
# -----------------------------
print("Vector A:", A)
print("Vector B:", B)

print("\nDot Product =", dot_product)

print("Magnitude of A =", round(magnitude_A, 3))
print("Magnitude of B =", round(magnitude_B, 3))

print("\nCosine Similarity =", round(cosine_similarity, 3))



# import math

# # --------------------------------
# # Input Sentences
# # --------------------------------
# s1 = "I love NLP"
# s2 = "I love machine learning"

# # --------------------------------
# # Step 1: Tokenize
# # --------------------------------
# words1 = s1.lower().split()
# words2 = s2.lower().split()

# # --------------------------------
# # Step 2: Create Vocabulary
# # --------------------------------
# vocab = list(set(words1 + words2))

# print("Vocabulary:", vocab)

# # --------------------------------
# # Step 3: Create Vectors
# # --------------------------------
# A = []
# B = []

# for word in vocab:
#     A.append(words1.count(word))
#     B.append(words2.count(word))

# print("Vector A:", A)
# print("Vector B:", B)

# # --------------------------------
# # Step 4: Dot Product
# # --------------------------------
# dot_product = 0

# for i in range(len(A)):
#     dot_product += A[i] * B[i]

# # --------------------------------
# # Step 5: Magnitudes
# # --------------------------------
# magnitude_A = 0
# magnitude_B = 0

# for value in A:
#     magnitude_A += value ** 2

# for value in B:
#     magnitude_B += value ** 2

# magnitude_A = math.sqrt(magnitude_A)
# magnitude_B = math.sqrt(magnitude_B)

# # --------------------------------
# # Step 6: Cosine Similarity
# # --------------------------------
# cosine_similarity = dot_product / (magnitude_A * magnitude_B)

# # --------------------------------
# # Output
# # --------------------------------
# print("\nDot Product =", dot_product)

# print("Magnitude of A =", round(magnitude_A, 3))
# print("Magnitude of B =", round(magnitude_B, 3))

# print("\nCosine Similarity =", round(cosine_similarity, 3))