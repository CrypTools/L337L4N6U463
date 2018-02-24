"""
Convert ASCII to LEET and vice-versa
Encrypting is ASCII to LEET
Decrypting is LEET to ASCII
"""

SUBSTITUTIONS = [['a','4'], ['e','3'], ['g', '6'], ['i','1'], ['o','0'], ['s', '5'], ['t','7'], ['A','4'], ['E','3'], ['G', '6'], ['I','1'], ['O','0'], ['S', '5'], ['T','7']] # Create a list of substitutions for each rule of LEET language


def encrypt(message, substitutions):
  """
  Takes a string as input returns the LEET version of that string
  Use: 
  	encrypt("message", SUBSTITUTIONS)
  	=> 'm355463'
  """
  for article in substitutions: # Repeats for each article of SUBSTITUTIONS list
    old = article[0] # Set variable old to first element of article 
    new = article[1] # Set variable new to second element of article 
    message = message.replace(old, new) # Use replace string method to substitute old value by new value 
    
  return message # Returns encrypted message
 

def decrypt(message, substitutions):
  """
  Takes a string encrypted with LEET as input and returns the original version
  Use:
  	decrypt("m355463", SUBSTITUTIONS)
  	=> 'message'
  """
  for article in substitutions: # Repeats for each article of SUBSTITUTIONS list
    old = article[1] # Set variable old to second element of article 
    new = article[0] # Set variable new to first element of article 
    message = message.replace(old, new) # Use replace string method to substitute old value by new value
    
  return message # Returns decrypted message

# Main section 

if __name__ == "__main__":
  cond = input("Encrypt (e) / decrypt (d): ") # Set cond to "e" or "d"
  message = input("Give the message: ") # Stores input as string in message
  
  if cond == "e": # If cond is "e", then use encrypt function
    print(encrypt(message)) # Print encrypted message
  else: # Else, use decrypt function
    print(decrypt(message)) # Print decrypted message
