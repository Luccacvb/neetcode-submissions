class Solution:
    def areSentencesSimilar(
        self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]
    ) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        similar_map = defaultdict(set)
        for a, b in similarPairs:
            similar_map[a].add(b)
            similar_map[b].add(a)

        for i in range(len(sentence1)):
            w1, w2 = sentence1[i], sentence2[i]
            if w1 == w2:
                continue

            if w2 not in similar_map.get(w1, set()):
                return False

        return True
