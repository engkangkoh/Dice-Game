def count_wins(dice1, dice2):
  assert len(dice1) == 6 and len(dice2) == 6
  dice1_wins, dice2_wins = 0, 0

  for i in dice1:
    for j in dice2:
      if i > j:
        dice1_wins += 1
      elif i < j:
        dice2_wins += 1
  return (dice1_wins, dice2_wins)


def find_the_best_dice(dices):

  assert all(len(dice) == 6 for dice in dices)

  for i in dices:
    counter = 0


    for j in dices:
      if i != j:
        dice1_wins, dice2_wins = count_wins(i, j)
        if dice1_wins > dice2_wins:
          counter += 1
          if counter == len(dices) - 1:
            return dices.index(i)
  return -1


def compute_strategy(dices):
  assert all(len(dice) == 6 for dice in dices)
  strategy = dict()

  index_best_die = find_the_best_dice(dices)
  if index_best_die != -1:
    update_d = {'choose_first': True, 'first_dice': index_best_die}
    strategy.update(update_d)
  else:
    strategy.update({'choose_first': False})
    for i in dices:
      for j in dices:
        if i != j:
          dice1_wins, dice2_wins = count_wins(i, j)
          if dice1_wins > dice2_wins:
            update = {dices.index(j): dices.index(i)}
            strategy.update(update)

  return strategy


dices = [[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [3, 3, 3, 5, 5, 8]]
x = compute_strategy(dices)
print(x)