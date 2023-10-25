def increasing_word_weights(sentence):
    weights = [sum([ord(l) for l in word if l.isalpha()])for word in sentence.split(" ")]
    
    for i in range(len(weights)-1):
        if weights[i]>= weights[i+1]:
            return False
    return True


print(increasing_word_weights("Why not try?"))
print(increasing_word_weights("All other roads."))
print(increasing_word_weights("You get what you settle for."))
print(increasing_word_weights("Standing on the shoulders of giants."))
print(increasing_word_weights("Louise's grannie escapes hassled village gardens."))