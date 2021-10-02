This script simulates refinement process from a given level to a target level (e.g. +10 => +11),
and check the cost used (how many pieces of the item are used as material)

## The simulation process:

1. assume we have an item of a given level (e.g. +10)
2. assume we have infinite material
3. keep refining (if the item is broken, repair and continue)
4. stop when the target level (e.g. +11) is reached
5. check the cost (count how many pieces of material are used)
6. repeat 1-5 multiple times, and get a distribution of the cost

## The following are the result of simulating 100000 times of each (+x => +y) refinement

### 普通精鍊 (note that the average cost of 普通精鍊 of +4 => +7 is cheaper than 安全精鍊)

```
Simulation (100000 rounds for each target level):
Simulating +4  => +5 : cost(mean, 75/90/95%-tile):   0.499,   1.00/  2.00/  2.00. mean refine length:   2.997 (slmulation elapsed time: 0.49s)
Simulating +5  => +6 : cost(mean, 75/90/95%-tile):   1.003,   1.00/  3.00/  5.00. mean refine length:   4.995 (slmulation elapsed time: 0.79s)
Simulating +6  => +7 : cost(mean, 75/90/95%-tile):   2.238,   3.00/  7.00/ 10.00. mean refine length:   9.941 (slmulation elapsed time: 1.72s)
Simulating +7  => +8 : cost(mean, 75/90/95%-tile):   4.131,   6.00/ 13.00/ 19.00. mean refine length:  17.522 (slmulation elapsed time: 3.96s)
Simulating +8  => +9 : cost(mean, 75/90/95%-tile):   6.892,   9.00/ 22.00/ 33.00. mean refine length:  28.564 (slmulation elapsed time: 9.14s)
Simulating +9  => +10: cost(mean, 75/90/95%-tile):  11.212,  14.00/ 37.00/ 55.00. mean refine length:  45.860 (slmulation elapsed time: 22.71s)
Simulating +10 => +11: cost(mean, 75/90/95%-tile):  18.350,  22.00/ 62.00/ 91.00. mean refine length:  71.436 (slmulation elapsed time: 55.32s)
Simulating +11 => +12: cost(mean, 75/90/95%-tile):  29.076,  33.00/ 99.00/149.00. mean refine length: 109.639 (slmulation elapsed time: 132.30s)
Simulating +12 => +13: cost(mean, 75/90/95%-tile):  44.605,  50.00/155.00/233.00. mean refine length: 165.280 (slmulation elapsed time: 306.93s)
Simulating +13 => +14: cost(mean, 75/90/95%-tile):  67.996,  72.00/238.00/363.00. mean refine length: 248.866 (slmulation elapsed time: 711.19s)
Simulating +14 => +15: cost(mean, 75/90/95%-tile): 103.110, 107.00/362.00/556.00. mean refine length: 374.293 (slmulation elapsed time: 1614.96s)
```

### +7 => +10 時使用安全精鍊 (+4 => +7 用普通精鍊比較便宜)

```
Simulation (100000 rounds for each target level):
Simulating +4  => +5 : cost(mean, 75/90/95%-tile):   0.502,   1.00/  2.00/  2.00. mean refine length:   3.006 (slmulation elapsed time: 0.43s)
Simulating +5  => +6 : cost(mean, 75/90/95%-tile):   0.990,   1.00/  3.00/  5.00. mean refine length:   4.966 (slmulation elapsed time: 0.83s)
Simulating +6  => +7 : cost(mean, 75/90/95%-tile):   2.268,   3.00/  7.00/ 10.00. mean refine length:  10.068 (slmulation elapsed time: 1.76s)
Simulating +7  => +8 : cost(mean, 75/90/95%-tile):   4.000,   4.00/  4.00/  4.00. mean refine length:   1.000 (slmulation elapsed time: 0.28s)
Simulating +8  => +9 : cost(mean, 75/90/95%-tile):   6.000,   6.00/  6.00/  6.00. mean refine length:   1.000 (slmulation elapsed time: 0.23s)
Simulating +9  => +10: cost(mean, 75/90/95%-tile):   8.000,   8.00/  8.00/  8.00. mean refine length:   1.000 (slmulation elapsed time: 0.28s)
Simulating +10 => +11: cost(mean, 75/90/95%-tile):  13.521,  18.00/ 36.00/ 45.00. mean refine length:   4.005 (slmulation elapsed time: 0.54s)
Simulating +11 => +12: cost(mean, 75/90/95%-tile):  21.704,  30.00/ 67.00/ 94.00. mean refine length:   8.492 (slmulation elapsed time: 1.26s)
Simulating +12 => +13: cost(mean, 75/90/95%-tile):  34.314,  46.00/113.00/164.00. mean refine length:  15.327 (slmulation elapsed time: 2.82s)
Simulating +13 => +14: cost(mean, 75/90/95%-tile):  53.014,  64.00/180.00/267.00. mean refine length:  25.493 (slmulation elapsed time: 6.87s)
Simulating +14 => +15: cost(mean, 75/90/95%-tile):  80.202,  91.00/279.00/417.00. mean refine length:  40.389 (slmulation elapsed time: 16.24s)
```

