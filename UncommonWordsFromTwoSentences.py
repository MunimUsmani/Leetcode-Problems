class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Split sentences into words and combine them into a single list
        all_words = s1.split() + s2.split()

        # Use Counter to count the frequency of each word
        word_counts = Counter(all_words)

        # Filter for words that appear exactly once
        uncommon_words = [word for word, count in word_counts.items() if count == 1]

        return uncommon_words
