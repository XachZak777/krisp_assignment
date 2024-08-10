def find_min_pledge(pledge_list):
  pledge_list.sort()
  min_pledge = 1  # Start with the smallest possible pledge
  for pledge in pledge_list:
    if pledge <= 0:  # Ignore negative or zero pledges
      continue
    if pledge == min_pledge:
      min_pledge += 1
    elif pledge > min_pledge:
      return min_pledge
  return min_pledge  # If no suitable pledge found, return the current min_pledge

assert find_min_pledge([1, 3, 6, 4, 1, 2]) == 5
assert find_min_pledge([1, 2, 3]) == 4
assert find_min_pledge([-1, -3]) == 1