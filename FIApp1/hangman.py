def string_writer(guessed, word):
    string = ""
    for char in word: #For every character
        if not char in guessed: #If its not guessed
            if char == " ": #If its a space
                string += "  " #Add double space
            else: #Else, any character
                string += "_ " #Make it a _
        else: #If it is guessed
            string += f"{char} " # Add the character to the string
    return(string)
