def sum_possible(amount, numbers, memo={}):
  if amount == 0:
    return True

  if amount < 0:
    return False

  if amount in memo:
    return memo[amount]

  for num in numbers:
    if sum_possible(amount - num, numbers, memo):
      memo[amount] = True
      return True
    else:
      memo[amount] = False
  return False
