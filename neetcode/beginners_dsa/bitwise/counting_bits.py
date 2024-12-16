class Solution:
    def countBits(self, n: int) -> List[int]:
        binary_representation = [base10 for base10 in range(n + 1)]
        for i, num in enumerate(binary_representation):
            # convert each num
            count = 0
            while num > 0:
                if num & 1 == 1:
                    count += 1
                # divide by two via bit shift
                num = num >> 1
            binary_representation[i] = count

        return binary_representation