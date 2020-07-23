
/**
  This file was autogenerated when saving a board with
  Teacup's Configtool. You can edit it, but the next board
  save operation in Configtool will overwrite it without
  asking.
*/

#define NUMTABLES 2
#define NUMTEMPS 25

#define THERMISTOR_EXTRUDER 0
#define THERMISTOR_BED 1

const uint16_t PROGMEM temptable[NUMTABLES][NUMTEMPS][3] = {
  // EXTRUDER temp table using Beta algorithm with parameters:
  // R0 = 100000, T0 = 25, R1 = 0, R2 = 1000, beta = 4092, maxadc = 1023
  {
    {  22,  1995,     0}, //  498 C,     22 ohms, 0.107 V, 0.53 mW, m =  0.000
    {  26,  1898,  6177}, //  474 C,     26 ohms, 0.127 V, 0.62 mW, m =  6.033
    {  30,  1820,  5012}, //  455 C,     30 ohms, 0.146 V, 0.71 mW, m =  4.895
    {  35,  1740,  4109}, //  435 C,     35 ohms, 0.171 V, 0.83 mW, m =  4.013
    {  40,  1673,  3397}, //  418 C,     41 ohms, 0.195 V, 0.94 mW, m =  3.318
    {  46,  1607,  2840}, //  401 C,     47 ohms, 0.225 V, 1.07 mW, m =  2.774
    {  53,  1542,  2365}, //  385 C,     55 ohms, 0.259 V, 1.23 mW, m =  2.310
    {  69,  1428,  1821}, //  357 C,     72 ohms, 0.337 V, 1.57 mW, m =  1.779
    {  88,  1330,  1324}, //  332 C,     94 ohms, 0.430 V, 1.96 mW, m =  1.293
    { 112,  1238,   983}, //  309 C,    123 ohms, 0.547 V, 2.44 mW, m =  0.960
    { 140,  1156,   744}, //  289 C,    158 ohms, 0.684 V, 2.95 mW, m =  0.727
    { 174,  1080,   576}, //  270 C,    205 ohms, 0.850 V, 3.53 mW, m =  0.563
    { 211,  1013,   459}, //  253 C,    260 ohms, 1.030 V, 4.09 mW, m =  0.448
    { 254,   950,   375}, //  237 C,    330 ohms, 1.240 V, 4.66 mW, m =  0.367
    { 362,   829,   287}, //  207 C,    547 ohms, 1.768 V, 5.71 mW, m =  0.281
    { 484,   724,   221}, //  181 C,    896 ohms, 2.363 V, 6.23 mW, m =  0.216
    { 783,   496,   194}, //  124 C,   3249 ohms, 3.823 V, 4.50 mW, m =  0.190
    { 853,   433,   232}, //  108 C,   4988 ohms, 4.165 V, 3.48 mW, m =  0.227
    { 908,   371,   286}, //   92 C,   7828 ohms, 4.434 V, 2.51 mW, m =  0.280
    { 957,   297,   390}, //   74 C,  14284 ohms, 4.673 V, 1.53 mW, m =  0.382
    { 991,   214,   620}, //   53 C,  30030 ohms, 4.839 V, 0.78 mW, m =  0.606
    {1002,   172,   979}, //   43 C,  45545 ohms, 4.893 V, 0.53 mW, m =  0.956
    {1011,   122,  1428}, //   30 C,  77769 ohms, 4.937 V, 0.31 mW, m =  1.396
    {1017,    68,  2297}, //   17 C, 145286 ohms, 4.966 V, 0.17 mW, m =  2.244
    {1021,     2,  4230}  //    0 C, 340333 ohms, 4.985 V, 0.07 mW, m =  4.132
  },
  // BED temp table using Beta algorithm with parameters:
  // R0 = 100000, T0 = 25, R1 = 0, R2 = 4700, beta = 4092, maxadc = 1023
  {
    {   5,  1966,     0}, //  491 C,     23 ohms, 0.024 V, 0.03 mW, m =  0.000
    {   6,  1865, 25946}, //  466 C,     28 ohms, 0.029 V, 0.03 mW, m = 25.339
    {   7,  1784, 20652}, //  446 C,     32 ohms, 0.034 V, 0.04 mW, m = 20.169
    {   9,  1662, 15700}, //  415 C,     42 ohms, 0.044 V, 0.05 mW, m = 15.333
    {  11,  1571, 11629}, //  392 C,     51 ohms, 0.054 V, 0.06 mW, m = 11.357
    {  14,  1469,  8687}, //  367 C,     65 ohms, 0.068 V, 0.07 mW, m =  8.483
    {  18,  1371,  6300}, //  342 C,     84 ohms, 0.088 V, 0.09 mW, m =  6.153
    {  22,  1297,  4712}, //  324 C,    103 ohms, 0.107 V, 0.11 mW, m =  4.602
    {  27,  1226,  3637}, //  306 C,    127 ohms, 0.132 V, 0.14 mW, m =  3.552
    {  33,  1160,  2815}, //  290 C,    157 ohms, 0.161 V, 0.17 mW, m =  2.749
    {  40,  1100,  2201}, //  275 C,    191 ohms, 0.195 V, 0.20 mW, m =  2.150
    {  48,  1045,  1746}, //  261 C,    231 ohms, 0.234 V, 0.24 mW, m =  1.705
    {  68,   947,  1258}, //  236 C,    334 ohms, 0.332 V, 0.33 mW, m =  1.229
    {  94,   861,   842}, //  215 C,    475 ohms, 0.459 V, 0.44 mW, m =  0.823
    { 126,   788,   589}, //  197 C,    659 ohms, 0.615 V, 0.57 mW, m =  0.575
    { 163,   725,   432}, //  181 C,    890 ohms, 0.796 V, 0.71 mW, m =  0.423
    { 207,   668,   331}, //  167 C,   1191 ohms, 1.011 V, 0.86 mW, m =  0.324
    { 323,   562,   234}, //  140 C,   2166 ohms, 1.577 V, 1.15 mW, m =  0.229
    { 457,   473,   169}, //  118 C,   3788 ohms, 2.231 V, 1.31 mW, m =  0.165
    { 771,   296,   144}, //   74 C,  14323 ohms, 3.765 V, 0.99 mW, m =  0.141
    { 889,   211,   185}, //   52 C,  30950 ohms, 4.341 V, 0.61 mW, m =  0.181
    { 935,   164,   260}, //   41 C,  49376 ohms, 4.565 V, 0.42 mW, m =  0.254
    { 969,   116,   361}, //   29 C,  82805 ohms, 4.731 V, 0.27 mW, m =  0.353
    { 994,    62,   552}, //   15 C, 155727 ohms, 4.854 V, 0.15 mW, m =  0.539
    {1010,     2,   962}  //    0 C, 339071 ohms, 4.932 V, 0.07 mW, m =  0.940
  }
};
