class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        
        total=0.0
        k = min(len(prices),len(discounts))
        
        for i in range(k):
            price = prices[i]
            discount = discounts[i]
            final_price = (price * (100-discount))/100
            total += final_price
        for i in range(k, len(prices)):
            total += prices[i]
        return total
            