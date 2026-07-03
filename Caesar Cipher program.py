def process_text(text, shift, mode="encrypt"):
    """
    Encrypts or decrypts text using a basic Caesar cipher.
    
    :param text: The string to be processed.
    :param shift: The integer key used to shift characters.
    :param mode: 'encrypt' or 'decrypt'.
    :return: The processed string.
    """
    result = ""
    
    # If we are decrypting, we reverse the shift direction
    if mode == "decrypt":
        shift = -shift

    for char in text:
        # Check if the character is a letter
        if char.isalpha():
            # Determine the ASCII base (65 for uppercase 'A', 97 for lowercase 'a')
            base = ord('A') if char.isupper() else ord('a')
            
            # Apply the cipher logic
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            # Leave numbers, spaces, and punctuation exactly as they are
            result += char
            
    return result

# ==========================================
# Interactive Console Execution
# ==========================================
if __name__ == "__main__":
    print("--- Interactive Caesar Cipher ---")
    
    # 1. Get the mode
    mode_choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()
    mode = "decrypt" if mode_choice.startswith('d') else "encrypt"
    
    # 2. Get the text
    user_text = input(f"Enter the text to {mode}: ")
    
    # 3. Get the shift key
    while True:
        try:
            key = int(input("Enter the shift key (e.g., 3): "))
            break # Exit the loop if a valid number is entered
        except ValueError:
            print("Please enter a valid whole number for the key.")
            
    # 4. Process and display the result
    final_output = process_text(user_text, key, mode=mode)
    
    print("\n--- Result ---")
    print(f"Original: {user_text}")
    print(f"Output:   {final_output}")