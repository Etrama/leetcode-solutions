class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # two sources of cost:
        # 1. count of G / M / P
        # 2. travel
        # 1: counting elements:
        cost = 0
        for element in garbage:
            cost += len(element)
        # 2: travel time
        g_index = 0
        p_index = 0
        m_index = 0
        for index, val in enumerate(garbage):
            if "G" in val:
                g_index = index
            if "P" in val:
                p_index = index
            if "M" in val:
                m_index = index
        print(g_index)
        print(p_index)
        print(m_index)
        cost += sum(travel[:g_index]) + sum(travel[:p_index]) + sum(travel[:m_index])
        return cost