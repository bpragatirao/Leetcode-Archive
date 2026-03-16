class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        is_neg = (dividend < 0) != (divisor < 0)
        a, b = abs(dividend), abs(divisor)
        res = 0

        while a >= b:
            temp_div = b
            count = 1

            while a >= (temp_div << 1):
                temp_div <<= 1
                count <<= 1

            a -= temp_div
            res += count

        return -res if is_neg else res
