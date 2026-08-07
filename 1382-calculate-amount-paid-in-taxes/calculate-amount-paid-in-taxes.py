class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0.0
        previous_limit = 0

        for upper_limit, percent in brackets:
            if income <= previous_limit:
                break

            taxable_income = min(income, upper_limit) - previous_limit
            tax += taxable_income * percent / 100

            previous_limit = upper_limit

        return tax