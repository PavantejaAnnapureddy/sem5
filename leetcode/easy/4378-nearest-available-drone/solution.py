class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        tx,ty= target
        best_idx = -1
        best_dist = float('inf')
        for i, (x, y, r) in enumerate(drones):
            dist = abs(x - tx) + abs(y - ty)
            if dist <= r and dist < best_dist:
                best_dist = dist
                best_idx = i
        return best_idx