def unique_styles(albums):
    unique = set()
    for styles in albums:
        for style in styles.split(","):
            unique.add(style)

    return len(unique)


albums = [
    "Dub,Dancehall",
    "Industrial,Heavy Metal",
    "Techno,Dubstep",
    "Synth-pop,Euro-Disco",
    "Industrial,Techno,Minimal"
]

print(unique_styles(albums))
