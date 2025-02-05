import math

# Noktaları tanımlama
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Öklid Mesafesi Hesaplama Fonksiyonu
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Mesafeleri hesaplama
distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Minimum mesafeyi bulma
min_distance = min(distances)

# Sonucu yazdırma
print(f"Mesafeler: {distances}")
print(f"Minimum Mesafe: {min_distance}")
