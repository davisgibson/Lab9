############################################
#                                          # 
#                   70pt                   #
#                                          #
############################################

# Create a celcius to fahrenheit calculator.
# Multiply by 9, then divide by 5, then add 32 to calculate your answer.

# TODO:
# Ask user for Celcius temperature to convert
# Accept user input 
# Calculate fahrenheit
# Output answer

print 'What is your celcius value that you would like to convert to fahrenheit'
celcius = int(raw_input())

celcius = celcius * 9
celcius = celcius / 5
celcius = celcius + 32
print 'The answer is ' + str(celcius) + ' degrees fahrenheit.'