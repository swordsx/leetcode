class Solution:
    # @param {integer[][]} buildings
    # @return {integer[][]}
    def getSkyline(self, buildings):
        if not buildings: return []
        tops = [buildings[0]]
        for i in range(1, len(buildings)):
            la, ra, ha = buildings[i][0], buildings[i][1], buildings[i][2]
            if la > tops[-1][1]:
                tops += [[tops[-1][1], la, 0], buildings[i]]
                continue
            j = len(tops) - 1
            while j >= 0 and la <= tops[j][1]:
                lb, rb, hb = tops[j][0], tops[j][1], tops[j][2]
                if la > lb and ra >= rb:
                    if ha > hb: tops[j][1] = la
                    else: la = rb
                elif la > lb and ra < rb:
                    if ha > hb:
                        tops[j][1] = la
                        tops.insert(j + 1, [ra, rb, hb])
                    else: la = ra
                elif la <= lb and ra >= rb:
                    if ha > hb: del tops[j]
                    else: la = rb
                elif la <= lb and ra < rb and ra > lb:
                    if ha > hb: tops[j][0] = ra
                    else: la = ra
                elif ra <= lb:
                    if ha <= hb: la = ra
                j -= 1
            if la != ra:
                if not tops: tops.append([la, ra, ha])
                elif tops[j + 1][2] == ha: tops[j + 1][1] = ra
                else: tops.insert(j + 2, [la, ra, ha])
        tops.append([tops[-1][1], tops[-1][1], 0])
        return [[top[0], top[2]] for top in tops]
