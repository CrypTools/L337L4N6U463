SUBSTITUTIONS = [['a','4'], ['e','3'], ['g', '6'], ['i','1'], ['o','0'], ['s', '5'], ['t','7'], ['A','4'], ['E','3'], ['G', '6'], ['I','1'], ['O','0'], ['S', '5'], ['T','7']]
def decrypt(message, SUBSTITUTIONS):
  """ Use : decrypt("m355463", SUBSTITUTIONS)
  => 'message'
  """
  for element in substitutions:
    old = element[1]
    new = element[0]
    message = message.replace(old, new)
  return message
