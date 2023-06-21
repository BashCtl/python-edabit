def maximum_score(tile_hand):
    return sum([item['score'] for item in tile_hand])


lst = [
  { "tile": "N", "score": 1 },
  { "tile": "K", "score": 5 },
  { "tile": "Z", "score": 10 },
  { "tile": "X", "score": 8 },
  { "tile": "D", "score": 2 },
  { "tile": "A", "score": 1 },
  { "tile": "E", "score": 1 }
]

print(maximum_score(lst))