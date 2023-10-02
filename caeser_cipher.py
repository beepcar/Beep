import random

def caesar_cipher(text, shift):
  """Encrypts a text using the Caesar cipher.
  Args:
    text: The text to be encrypted.
    shift: The shift value.
  Returns:
    The encrypted text.
  """
  ciphertext = ""
  for char in text:
    if char.isalpha():
      # Convert the character to uppercase.
      char = char.upper()
      # Calculate the encrypted character.
      encrypted_char = ord(char) + shift
      # If the encrypted character is greater than Z, wrap it around to A.
      if encrypted_char > ord("Z"):
        encrypted_char -= 26
      # Convert the encrypted character back to lowercase.
      if char.islower():
        encrypted_char = chr(encrypted_char).lower()
      # Add the encrypted character to the ciphertext.
      ciphertext += chr(encrypted_char)
    else:
      # Add the non-alphabetic character to the ciphertext without encryption.
      ciphertext += char
  return ciphertext


def decrypt_caesar_cipher(ciphertext, shift):
  """Decrypts a text using the Caesar cipher.
  Args:
    ciphertext: The text to be decrypted.
    shift: The shift value.
  Returns:
    The decrypted text.
  """
  plaintext = ""
  for char in ciphertext:
    if char.isalpha():
      # Convert the character to uppercase.
      char = char.upper()
      # Calculate the decrypted character.
      encrypted_char = ord(char) + shift

      # If the decrypted character is less than A, wrap it around to Z.
      if encrypted_char < ord("A"):
        encrypted_char += 26
      # Convert the decrypted character back to lowercase.
      if char.islower():
        encrypted_char = chr(encrypted_char).lower()
      # Add the decrypted character to the plaintext.
      plaintext += chr(encrypted_char)
    else:
      # Add the non-alphabetic character to the plaintext without decryption.
      plaintext += char
  return plaintext


def main():
  # Get the text from the user.
  text = input("Enter the text to be encrypted: ")
  # Get the shift value from the user.
  shift = random.randint(1,26)
  print(shift)
  # Encrypt the text using the Caesar cipher.
  ciphertext = caesar_cipher(text, shift)
  # Print the encrypted text.
  print("The encrypted text is:", shift , ciphertext  )
  # Decrypt the text using the Caesar cipher.
  plaintext = decrypt_caesar_cipher(ciphertext, -shift)
  # Print the decrypted text.
  print("The decrypted text is:", plaintext.lower())


if __name__ == "__main__":
  main()
