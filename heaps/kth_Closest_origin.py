# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

#         minheap - calc distance from origin of each given point, add it to heap

        points.sort(key=self.squared_distance)


        return points[:k]

    def squared_distance(self, point: List[int]) -> int:

        return point[0] ** 2 + point[1] ** 2


        # Since heap is sorted in increasing order,
        # negate the distance to simulate max heap
        # and fill the heap with the first k elements of points
        heap = [(-self.squared_distance(points[i]), i) for i in range(k)]
        heapq.heapify(heap)
        for i in range(k, len(points)):
            dist = -self.squared_distance(points[i])
            if dist > heap[0][0]:
                # If this point is closer than the kth farthest,
                # discard the farthest point and add this one
                heapq.heappushpop(heap, (dist, i))

        # Return all points stored in the max heap
        return [points[i] for (_, i) in heap]
