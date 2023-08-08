def get_frame(w, h, ch):
    if w <= 2 or h <= 2:
        return "invalid"
    return [[ch * w if i == 0 or i == h - 1 else ch + " " * (w - 2) + ch] for i in range(h)]


print(get_frame(4, 5, "#"))
