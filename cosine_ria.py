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