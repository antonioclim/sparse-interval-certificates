# Complete V2 and V3 displayed results

Article: Sparse interval certificates for parametric biobjective optimisation: linear cell bounds and quantitative continuity.

Author: Antonio Clim. Journal of Global Optimization.

This technical documentation accompanies Online Resource 2 and is supplied with Online Resource 10. It retains the complete migrated text and displayed table values from the source-bound 28-page ESM2 presentation. The scientific release 1.1.0 and its named archives are unchanged. No experiment or timing run was performed by this migration.

<a id="s20-4"></a>
## S20.4 Complete V2 producer and evidence-size table

Every row summarises seven accepted repetitions. An em dash in the cell column denotes a negative obstruction, for which positive certificate cell count is inapplicable.

| Case | Producer | Cells | Proof bytes | Complete producer time (s) |
| --- | --- | --- | --- | --- |
| N=4 | event | 14 | 1,781 | 0.076 [0.074, 0.090] |
| N=4 | geometric | 8 | 1,177 | 0.180 [0.159, 0.233] |
| N=8 | event | 44 | 5,551 | 0.100 [0.089, 0.110] |
| N=8 | geometric | 12 | 1,727 | 0.273 [0.253, 0.405] |
| N=16 | event | 152 | 19,983 | 0.138 [0.127, 0.157] |
| N=16 | geometric | 20 | 2,875 | 0.505 [0.459, 0.576] |
| N=32 | event | 560 | 77,423 | 0.446 [0.395, 0.599] |
| N=32 | geometric | 36 | 5,875 | 1.240 [1.195, 1.338] |
| N=64 | event | 2,144 | 307,381 | 2.761 [2.545, 9.991] |
| N=64 | geometric | 68 | 11,125 | 3.900 [3.708, 11.251] |
| Constant mixed positive | event | 2 | 321 | 0.096 [0.086, 0.153] |
| Constant mixed positive | geometric | 2 | 321 | 0.125 [0.106, 0.216] |
| Irrational-only negative | event | — | 210 | 0.090 [0.077, 0.278] |
| Irrational-only negative | geometric | — | 210 | 0.115 [0.100, 0.181] |

Exact displayed cells: [s20_4_v2_producers.csv](../data/esm2/s20_4_v2_producers.csv).

<a id="s20-5"></a>
## S20.5 Complete V3 producer and evidence-size table

Raw and final sizes are invariant within each case/method’s seven repetitions. The original object is retained in the execution record; recipients check the final object. Arrow notation shows raw → coalesced. For negative objects the final representation is unchanged.

| Case | Producer | Raw → final cells | Raw → final proof bytes | Complete producer time (s) |
| --- | --- | --- | --- | --- |
| N=4 | event | 14 → 4 | 1,781 → 599 | 0.098 [0.078, 0.108] |
| N=4 | geometric | 8 → 4 | 1,177 → 626 | 0.202 [0.174, 0.270] |
| N=8 | event | 44 → 8 | 5,551 → 1,113 | 0.091 [0.081, 0.103] |
| N=8 | geometric | 12 → 8 | 1,727 → 1,159 | 0.245 [0.234, 0.278] |
| N=16 | event | 152 → 16 | 19,983 → 2,239 | 0.142 [0.137, 0.254] |
| N=16 | geometric | 20 → 16 | 2,875 → 2,286 | 0.427 [0.405, 0.469] |
| N=32 | event | 560 → 32 | 77,423 → 4,590 | 0.466 [0.453, 0.530] |
| N=32 | geometric | 36 → 32 | 5,875 → 5,189 | 1.272 [1.064, 1.582] |
| N=64 | event | 2,144 → 64 | 307,381 → 9,373 | 2.572 [2.407, 3.564] |
| N=64 | geometric | 68 → 64 | 11,125 → 10,424 | 3.338 [3.176, 3.713] |
| Constant mixed positive | event | 2 → 1 | 321 → 226 | 0.092 [0.080, 0.097] |
| Constant mixed positive | geometric | 2 → 1 | 321 → 226 | 0.123 [0.103, 0.135] |
| Irrational-only negative | event | — → — | 210 → 210 | 0.086 [0.082, 0.104] |
| Irrational-only negative | geometric | — → — | 210 → 210 | 0.111 [0.102, 0.117] |

Exact displayed cells: [s20_5_v3_producers.csv](../data/esm2/s20_5_v3_producers.csv).

<a id="s20-6"></a>
## S20.6 All V2 recipient prefixes

Every entry summarises seven accepted within-case repetitions; every ratio uses all seven matched pairs.

| Case | Recipients | Event workflow (s) | Geometric workflow (s) | Paired event/geometric ratio |
| --- | --- | --- | --- | --- |
| N=4 | 1 | 0.152 [0.140, 0.184] | 0.250 [0.226, 0.307] | 0.600 [0.552, 0.689] |
| N=4 | 2 | 0.228 [0.201, 0.253] | 0.307 [0.283, 0.391] | 0.709 [0.647, 0.806] |
| N=4 | 4 | 0.378 [0.332, 0.421] | 0.440 [0.396, 0.539] | 0.857 [0.703, 0.920] |
| N=4 | 8 | 0.651 [0.587, 0.803] | 0.691 [0.657, 0.797] | 0.944 [0.868, 1.042] |
| N=4 | 16 | 1.227 [1.156, 1.359] | 1.199 [1.160, 1.350] | 0.997 [0.944, 1.092] |
| N=8 | 1 | 0.170 [0.159, 0.235] | 0.342 [0.312, 0.567] | 0.496 [0.308, 0.689] |
| N=8 | 2 | 0.241 [0.230, 0.306] | 0.410 [0.378, 0.690] | 0.598 [0.363, 0.746] |
| N=8 | 4 | 0.388 [0.362, 0.453] | 0.587 [0.497, 0.852] | 0.664 [0.490, 0.838] |
| N=8 | 8 | 0.678 [0.631, 0.950] | 0.853 [0.792, 1.179] | 0.756 [0.713, 1.175] |
| N=8 | 16 | 1.314 [1.210, 1.632] | 1.506 [1.282, 1.802] | 0.906 [0.804, 1.240] |
| N=16 | 1 | 0.230 [0.218, 0.259] | 0.570 [0.532, 0.661] | 0.403 [0.352, 0.484] |
| N=16 | 2 | 0.322 [0.296, 0.350] | 0.641 [0.603, 0.752] | 0.507 [0.428, 0.580] |
| N=16 | 4 | 0.498 [0.449, 0.575] | 0.776 [0.736, 0.949] | 0.652 [0.524, 0.768] |
| N=16 | 8 | 0.842 [0.807, 0.983] | 1.054 [0.993, 1.250] | 0.792 [0.679, 0.962] |
| N=16 | 16 | 1.580 [1.498, 2.194] | 1.692 [1.486, 1.814] | 0.963 [0.866, 1.437] |
| N=32 | 1 | 0.600 [0.531, 0.851] | 1.313 [1.264, 1.404] | 0.459 [0.389, 0.648] |
| N=32 | 2 | 0.765 [0.674, 1.025] | 1.419 [1.334, 1.498] | 0.540 [0.452, 0.722] |
| N=32 | 4 | 1.077 [0.931, 1.730] | 1.577 [1.484, 1.916] | 0.711 [0.571, 1.061] |
| N=32 | 8 | 1.709 [1.482, 3.852] | 1.831 [1.781, 2.464] | 0.947 [0.769, 1.563] |
| N=32 | 16 | 2.998 [2.572, 5.569] | 2.442 [2.346, 3.400] | 1.208 [0.967, 1.638] |
| N=64 | 1 | 3.109 [2.930, 10.394] | 3.982 [3.812, 11.397] | 0.750 [0.273, 2.684] |
| N=64 | 2 | 3.475 [3.330, 10.845] | 4.054 [3.902, 12.069] | 0.834 [0.288, 2.751] |
| N=64 | 4 | 4.183 [4.069, 11.528] | 4.203 [4.066, 12.313] | 0.980 [0.340, 2.816] |
| N=64 | 8 | 5.766 [5.528, 13.003] | 4.585 [4.399, 12.798] | 1.226 [0.451, 2.956] |
| N=64 | 16 | 9.843 [8.426, 25.615] | 5.206 [5.008, 13.439] | 1.798 [0.772, 4.876] |
| Constant mixed positive | 1 | 0.177 [0.152, 0.355] | 0.202 [0.167, 0.759] | 0.869 [0.321, 1.725] |
| Constant mixed positive | 2 | 0.254 [0.215, 0.457] | 0.269 [0.232, 0.850] | 0.911 [0.379, 1.689] |
| Constant mixed positive | 4 | 0.394 [0.342, 0.718] | 0.417 [0.360, 1.387] | 0.915 [0.340, 1.710] |
| Constant mixed positive | 8 | 0.675 [0.620, 1.415] | 0.732 [0.623, 1.840] | 0.971 [0.444, 1.847] |
| Constant mixed positive | 16 | 1.436 [1.144, 2.159] | 1.293 [1.155, 2.362] | 0.937 [0.608, 1.731] |
| Irrational-only negative | 1 | 0.159 [0.133, 0.366] | 0.206 [0.162, 0.289] | 0.884 [0.629, 1.270] |
| Irrational-only negative | 2 | 0.220 [0.186, 0.445] | 0.271 [0.217, 0.376] | 0.913 [0.667, 1.284] |
| Irrational-only negative | 4 | 0.352 [0.299, 0.600] | 0.410 [0.352, 0.641] | 0.908 [0.709, 1.153] |
| Irrational-only negative | 8 | 0.640 [0.511, 0.862] | 0.687 [0.605, 1.094] | 0.838 [0.675, 1.129] |
| Irrational-only negative | 16 | 1.153 [0.982, 1.622] | 1.200 [1.114, 1.904] | 0.879 [0.814, 1.106] |

Exact displayed cells: [s20_6_v2_recipients.csv](../data/esm2/s20_6_v2_recipients.csv).

<a id="s20-7"></a>
## S20.7 All V3 recipient prefixes

The compact scientific PDF retains the adverse V3 interpretation: all 25 median lower-family paired ratios favour event refinement; the five geometric wins are nested prefixes from one N=64 repetition, not five independent repetitions.

| Case | Recipients | Event workflow (s) | Geometric workflow (s) | Paired event/geometric ratio |
| --- | --- | --- | --- | --- |
| N=4 | 1 | 0.172 [0.144, 0.182] | 0.262 [0.246, 0.391] | 0.605 [0.406, 0.700] |
| N=4 | 2 | 0.241 [0.212, 0.294] | 0.328 [0.313, 0.457] | 0.694 [0.588, 0.902] |
| N=4 | 4 | 0.384 [0.326, 0.437] | 0.467 [0.447, 0.608] | 0.754 [0.698, 0.947] |
| N=4 | 8 | 0.667 [0.554, 0.764] | 0.779 [0.717, 0.850] | 0.874 [0.709, 0.993] |
| N=4 | 16 | 1.223 [1.034, 1.349] | 1.361 [1.295, 1.494] | 0.910 [0.724, 0.992] |
| N=8 | 1 | 0.165 [0.142, 0.177] | 0.315 [0.295, 0.341] | 0.517 [0.422, 0.586] |
| N=8 | 2 | 0.231 [0.209, 0.247] | 0.378 [0.350, 0.411] | 0.611 [0.513, 0.705] |
| N=8 | 4 | 0.356 [0.322, 0.411] | 0.505 [0.470, 0.540] | 0.721 [0.599, 0.822] |
| N=8 | 8 | 0.620 [0.560, 0.703] | 0.762 [0.727, 0.815] | 0.826 [0.688, 0.904] |
| N=8 | 16 | 1.185 [1.074, 1.235] | 1.309 [1.223, 1.341] | 0.906 [0.863, 0.965] |
| N=16 | 1 | 0.219 [0.197, 0.357] | 0.498 [0.463, 0.539] | 0.444 [0.394, 0.733] |
| N=16 | 2 | 0.286 [0.280, 0.422] | 0.571 [0.528, 0.600] | 0.519 [0.491, 0.767] |
| N=16 | 4 | 0.422 [0.413, 0.565] | 0.707 [0.660, 0.749] | 0.616 [0.586, 0.847] |
| N=16 | 8 | 0.707 [0.676, 0.832] | 0.955 [0.909, 1.033] | 0.749 [0.679, 0.915] |
| N=16 | 16 | 1.276 [1.223, 1.408] | 1.453 [1.418, 1.619] | 0.858 [0.785, 0.969] |
| N=32 | 1 | 0.543 [0.520, 0.614] | 1.338 [1.130, 1.680] | 0.439 [0.335, 0.460] |
| N=32 | 2 | 0.614 [0.579, 0.695] | 1.406 [1.192, 1.747] | 0.472 [0.357, 0.494] |
| N=32 | 4 | 0.782 [0.696, 0.871] | 1.537 [1.323, 1.879] | 0.523 [0.405, 0.567] |
| N=32 | 8 | 1.078 [0.931, 1.191] | 1.853 [1.572, 2.171] | 0.592 [0.473, 0.652] |
| N=32 | 16 | 1.632 [1.433, 1.792] | 2.412 [2.078, 2.746] | 0.689 [0.575, 0.745] |
| N=64 | 1 | 2.641 [2.472, 3.632] | 3.429 [3.274, 3.783] | 0.768 [0.721, 1.042] |
| N=64 | 2 | 2.713 [2.550, 3.711] | 3.493 [3.339, 3.852] | 0.774 [0.730, 1.041] |
| N=64 | 4 | 2.848 [2.672, 3.856] | 3.627 [3.483, 4.056] | 0.781 [0.701, 1.042] |
| N=64 | 8 | 3.115 [2.938, 4.141] | 3.888 [3.739, 4.408] | 0.797 [0.704, 1.036] |
| N=64 | 16 | 3.741 [3.508, 4.676] | 4.481 [4.281, 5.410] | 0.819 [0.674, 1.022] |
| Constant mixed positive | 1 | 0.155 [0.146, 0.184] | 0.189 [0.168, 0.202] | 0.895 [0.724, 0.922] |
| Constant mixed positive | 2 | 0.226 [0.218, 0.264] | 0.259 [0.227, 0.294] | 0.894 [0.769, 0.969] |
| Constant mixed positive | 4 | 0.359 [0.343, 0.420] | 0.393 [0.353, 0.460] | 0.928 [0.802, 1.017] |
| Constant mixed positive | 8 | 0.652 [0.612, 0.700] | 0.687 [0.610, 0.770] | 0.968 [0.849, 1.016] |
| Constant mixed positive | 16 | 1.236 [1.132, 1.366] | 1.252 [1.110, 1.367] | 1.020 [0.912, 1.061] |
| Irrational-only negative | 1 | 0.152 [0.148, 0.187] | 0.179 [0.171, 0.187] | 0.838 [0.802, 1.045] |
| Irrational-only negative | 2 | 0.219 [0.214, 0.264] | 0.245 [0.240, 0.330] | 0.901 [0.656, 1.058] |
| Irrational-only negative | 4 | 0.344 [0.335, 0.412] | 0.376 [0.369, 0.476] | 0.927 [0.716, 1.095] |
| Irrational-only negative | 8 | 0.606 [0.595, 0.727] | 0.639 [0.608, 0.730] | 0.978 [0.815, 1.138] |
| Irrational-only negative | 16 | 1.112 [1.096, 1.308] | 1.172 [1.116, 1.293] | 0.947 [0.852, 1.116] |

Exact displayed cells: [s20_7_v3_recipients.csv](../data/esm2/s20_7_v3_recipients.csv).

