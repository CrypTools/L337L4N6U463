SUBSTITUTIONS = [['a','4'], ['e','3'], ['g', '6'], ['i','1'], ['o','0'], ['s', '5'], ['t','7'], ['A','4'], ['E','3'], ['G', '6'], ['I','1'], ['O','0'], ['S', '5'], ['T','7']]
def encrypt(message, SUBSTITUTIONS):
  """ Use : encrypt("message", SUBSTITUTIONS)
  => 'm355463'
  """
  for element in substitutions:
    old = element[0]
    new = element[1]
    message = message.replace(old, new)
  return message
