class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        areaABCD = (C - A) * (D - B)
        areaEFGH = (G - E) * (H - F)
        xOverlap = max(0, min(C, G) - max(A, E))
        yOverlap = max(0, min(D, H) - max(B, F))
        areaOverlap = xOverlap * yOverlap
        return areaABCD + areaEFGH - areaOverlap
