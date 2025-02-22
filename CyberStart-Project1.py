points = []
distances = []

def euclidean_distance(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2) ** 0.5

while True:
    user_input = input("Enter a point (x, y) or type 'q' to exit: ")
    if user_input.lower() == 'q':
        break
    try:
        x, y = map(int, user_input.split(','))
        points.append((x, y))
    except ValueError:
        print("Please enter a valid input. Example: 3,4")

if len(points) >= 2:
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distances.append((points[i], points[j], round(euclidean_distance(points[i], points[j]), 3)))
    
    min_distance = min(distances, key=lambda x: x[2])
    print(f"All points: {points}")
    print("All distances:")
    for p1, p2, d in distances:
        print(f"{p1} - {p2}: {d:.3f}")
    print(f"Minimum Euclidean distance: {min_distance[0]} - {min_distance[1]} = {min_distance[2]:.3f}")

else: 
    print("At least two points are required for the operation.")
