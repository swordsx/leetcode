# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {Point[]} points
    # @return {integer}
    def maxPoints(self, points):
        dict = {}
        result = 0
        for point in points:
            dict[point] = collections.defaultdict(int)
        for i in range(len(points)):
            same = 1
            for j in range(i + 1, len(points)):                
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    same += 1
                else:
                    slope = 1.0 * (points[j].y - points[i].y) / (points[j].x - points[i].x) if points[i].x != points[j].x else 'inf'
                    dict[points[i]][slope] += 1
                    dict[points[j]][slope] += 1
            result = max(result, same)
            for slope in dict[points[i]]:
                dict[points[i]][slope] += same
                result = max(result, dict[points[i]][slope])
        return result
