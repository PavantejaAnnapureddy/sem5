import math

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        LIMIT = 10**6 + 1   # any value > max k

        # 1. Frequency of each character
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1

        # 2. Build half and find middle character
        middle = ''
        half = []
        for i in range(26):
            if freq[i] % 2 == 1:
                middle = chr(i + 97)
            half.extend([chr(i + 97)] * (freq[i] // 2))

        n = len(half)
        if n == 0:
            return s if k == 1 else ""

        # 3. Count characters in half
        cnt = [0] * 26
        for ch in half:
            cnt[ord(ch) - 97] += 1

        # 4. Total distinct permutations (capped at LIMIT)
        total = 1
        rem = n
        for i in range(26):
            if cnt[i] > 0:
                total *= math.comb(rem, cnt[i])
                if total > LIMIT:
                    total = LIMIT
                    break
                rem -= cnt[i]

        if k > total:
            return ""

        # 5. Build the k-th permutation of the half
        res = []
        remaining = k - 1
        available = [i for i in range(26) if cnt[i] > 0]

        for pos in range(n):
            rem_pos = n - pos - 1

            # If we already determined the exact permutation, fill with smallest chars
            if remaining == 0:
                for i in available:
                    if cnt[i] > 0:
                        res.extend([chr(i + 97)] * cnt[i])
                        cnt[i] = 0
                break

            for i in available:
                if cnt[i] == 0:
                    continue

                # Try placing character i at current position
                cnt[i] -= 1

                # Compute number of permutations of the remaining positions
                perms = 1
                r = rem_pos
                for j in available:
                    if cnt[j] > 0:
                        perms *= math.comb(r, cnt[j])
                        if perms > LIMIT:
                            perms = LIMIT
                            break
                        r -= cnt[j]

                if remaining < perms:
                    res.append(chr(i + 97))
                    break
                else:
                    remaining -= perms
                    cnt[i] += 1   # restore for next candidate

        # 6. Build the full palindrome
        first = ''.join(res)
        return first + middle + first[::-1] if middle else first + first[::-1]