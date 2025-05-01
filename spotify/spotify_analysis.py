Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas as pd
>>>
>>> 
>>> csv_path = 'C:/spotify/archive/songs_normalize.csv'
>>>
>>>
>>> df = pd.read_csv(csv_path)
>>>
>>>
>>> print(df.head())
           artist                    song  duration_ms  explicit  ...  liveness  valence    tempo         genre
0  Britney Spears  Oops!...I Did It Again       211160     False  ...    0.3550    0.894   95.053           pop
1       blink-182    All The Small Things       167066     False  ...    0.6120    0.684  148.726     rock, pop
2      Faith Hill                 Breathe       250546     False  ...    0.2510    0.278  136.859  pop, country
3        Bon Jovi            It's My Life       224493     False  ...    0.3470    0.544  119.992   rock, metal
4          *NSYNC             Bye Bye Bye       200560     False  ...    0.0845    0.879  172.656           pop

[5 rows x 18 columns]
>>> 
>>> print(df.columns)
Index(['artist', 'song', 'duration_ms', 'explicit', 'year', 'popularity',
       'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
       'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo',
       'genre'],
      dtype='object')
>>>
>>> 
>>> print(df.dtypes)
artist               object
song                 object
duration_ms           int64
explicit               bool
year                  int64
popularity            int64
danceability        float64
energy              float64
key                   int64
loudness            float64
mode                  int64
speechiness         float64
acousticness        float64
instrumentalness    float64
liveness            float64
valence             float64
tempo               float64
genre                object
dtype: object
>>>
>>>
>>> print(df.isnull().sum())
artist              0
song                0
duration_ms         0
explicit            0
year                0
popularity          0
danceability        0
energy              0
key                 0
loudness            0
mode                0
speechiness         0
acousticness        0
instrumentalness    0
liveness            0
valence             0
tempo               0
genre               0
dtype: int64
>>> import matplotlib.pyplot as plt
>>>
>>>
>>> plt.hist(df['duration_ms'], bins=50, color='blue', alpha=0.7)
(array([  3.,   3.,   6.,   3.,   3.,  17.,  17.,  32.,  54.,  68., 106.,
       152., 174., 198., 193., 162., 162., 127.,  99.,  75.,  77.,  50.,
        42.,  42.,  32.,  31.,  12.,  12.,  16.,   6.,   9.,   4.,   3.,
         1.,   1.,   0.,   0.,   1.,   0.,   1.,   0.,   1.,   1.,   0.,
         1.,   2.,   0.,   0.,   0.,   1.]), array([113000.  , 120422.92, 127845.84, 135268.76, 142691.68, 150114.6 ,
       157537.52, 164960.44, 172383.36, 179806.28, 187229.2 , 194652.12,
       202075.04, 209497.96, 216920.88, 224343.8 , 231766.72, 239189.64,
       246612.56, 254035.48, 261458.4 , 268881.32, 276304.24, 283727.16,
       291150.08, 298573.  , 305995.92, 313418.84, 320841.76, 328264.68,
       335687.6 , 343110.52, 350533.44, 357956.36, 365379.28, 372802.2 ,
       380225.12, 387648.04, 395070.96, 402493.88, 409916.8 , 417339.72,
       424762.64, 432185.56, 439608.48, 447031.4 , 454454.32, 461877.24,
       469300.16, 476723.08, 484146.  ]), <BarContainer object of 50 artists>)
>>> plt.title('Distribution of Song Durations')
Text(0.5, 1.0, 'Distribution of Song Durations')
>>> plt.xlabel('Duration (ms)')
Text(0.5, 0, 'Duration (ms)')
>>> plt.ylabel('Frequency')
Text(0, 0.5, 'Frequency')
>>> plt.show()
>>> import matplotlib.pyplot as plt
>>>
>>> # Plotting the distribution of song popularity
>>> plt.figure(figsize=(10, 6))
<Figure size 1000x600 with 0 Axes>
>>> plt.hist(df['popularity'], bins=20, color='green', alpha=0.7)
(array([177.,   3.,   1.,   2.,   3.,   3.,   5.,  11.,  17.,  20.,  59.,
        99., 166., 248., 242., 330., 257., 265.,  78.,  14.]), array([ 0.  ,  4.45,  8.9 , 13.35, 17.8 , 22.25, 26.7 , 31.15, 35.6 ,
       40.05, 44.5 , 48.95, 53.4 , 57.85, 62.3 , 66.75, 71.2 , 75.65,
       80.1 , 84.55, 89.  ]), <BarContainer object of 20 artists>)
>>> plt.title('Distribution of Song Popularity')
Text(0.5, 1.0, 'Distribution of Song Popularity')
>>> plt.xlabel('Popularity')
Text(0.5, 0, 'Popularity')
>>> plt.ylabel('Frequency')
Text(0, 0.5, 'Frequency')
>>> plt.show()
>>>