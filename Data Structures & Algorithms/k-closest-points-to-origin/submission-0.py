class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            dist = x**2 + y**2
            distances.append((dist, x, y))
        
        sorted_distances = sorted(distances)
        closet_points = []
        for i in range(k):
            x = sorted_distances[i][1]
            y = sorted_distances[i][2]
            closet_points.append([x, y])
        
        return closet_points