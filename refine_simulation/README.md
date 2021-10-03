The objective of this script is to find out how many equipment you have to prepare for refining form +x to +y

- This script only focuses on the equipments being used in repairing or safe refining. Other items like zeny, 神之金屬, 鋁 are ignored.
- The script simulates the refinement process many times, and get a distribution of the cost.

## The simulation process:

In this example, simulate (+10 => +11) 100k times

1. assume we have an equipment of a given level (+10)
2. assume we have infinite material
3. if the refinement level drops, keep refining
4. if the equipment is broken, repair and keep refining
5. stop only when the target level (e.g. +11) is reached
6. check the cost (count how many equipment are used)
7. repeat 1-5 100k times, and get a distribution of the cost

## The following are the result of simulating 100000 times of each (+x => +y) refinement

### 普通精鍊

Note that for +4 => +7, 普通精鍊 is cheaper then 安全精鍊 on average.

```
Simulation (100000 rounds for each target level):
+4  => +5 : cost(mean, 75/90/95%-tile):   0.499,   1.00/  2.00/  2.00. length:   2.997
+5  => +6 : cost(mean, 75/90/95%-tile):   1.003,   1.00/  3.00/  5.00. length:   4.995
+6  => +7 : cost(mean, 75/90/95%-tile):   2.238,   3.00/  7.00/ 10.00. length:   9.941
+7  => +8 : cost(mean, 75/90/95%-tile):   4.131,   6.00/ 13.00/ 19.00. length:  17.522
+8  => +9 : cost(mean, 75/90/95%-tile):   6.892,   9.00/ 22.00/ 33.00. length:  28.564
+9  => +10: cost(mean, 75/90/95%-tile):  11.212,  14.00/ 37.00/ 55.00. length:  45.860
+10 => +11: cost(mean, 75/90/95%-tile):  18.350,  22.00/ 62.00/ 91.00. length:  71.436
+11 => +12: cost(mean, 75/90/95%-tile):  29.076,  33.00/ 99.00/149.00. length: 109.639
+12 => +13: cost(mean, 75/90/95%-tile):  44.605,  50.00/155.00/233.00. length: 165.280
+13 => +14: cost(mean, 75/90/95%-tile):  67.996,  72.00/238.00/363.00. length: 248.866
+14 => +15: cost(mean, 75/90/95%-tile): 103.110, 107.00/362.00/556.00. length: 374.293
```

### 安全精鍊

+7 => +10 時使用安全精鍊 (+4 => +7 用普通精鍊比較便宜)

```
Simulation (100000 rounds for each target level):
+4  => +5 : cost(mean, 75/90/95%-tile):   0.502,   1.00/  2.00/  2.00. length:   3.006
+5  => +6 : cost(mean, 75/90/95%-tile):   0.990,   1.00/  3.00/  5.00. length:   4.966
+6  => +7 : cost(mean, 75/90/95%-tile):   2.268,   3.00/  7.00/ 10.00. length:  10.068
+7  => +8 : cost(mean, 75/90/95%-tile):   4.000,   4.00/  4.00/  4.00. length:   1.000
+8  => +9 : cost(mean, 75/90/95%-tile):   6.000,   6.00/  6.00/  6.00. length:   1.000
+9  => +10: cost(mean, 75/90/95%-tile):   8.000,   8.00/  8.00/  8.00. length:   1.000
+10 => +11: cost(mean, 75/90/95%-tile):  13.521,  18.00/ 36.00/ 45.00. length:   4.005
+11 => +12: cost(mean, 75/90/95%-tile):  21.704,  30.00/ 67.00/ 94.00. length:   8.492
+12 => +13: cost(mean, 75/90/95%-tile):  34.314,  46.00/113.00/164.00. length:  15.327
+13 => +14: cost(mean, 75/90/95%-tile):  53.014,  64.00/180.00/267.00. length:  25.493
+14 => +15: cost(mean, 75/90/95%-tile):  80.202,  91.00/279.00/417.00. length:  40.389
```

