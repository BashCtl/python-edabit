def like_or_dislike(lst):
    state = "Nothing"
    for item in lst:
        if item == "Like":
            if state == "Dislike":
                state = "Like"
            elif state == "Like":
                state = "Nothing"
            else:
                state = "Like"
        if item == "Dislike":
            if state == "Like":
                state = "Dislike"
            elif state == "Dislike":
                state = "Nothing"
            else:
                state = "Dislike"
    return state


print(like_or_dislike(["Dislike"]))
print(like_or_dislike(["Like", "Like"]))
print(like_or_dislike(["Dislike", "Like"]))
print(like_or_dislike(["Like", "Dislike", "Dislike"]))
print(like_or_dislike(["Like", "Like", "Like"]))
