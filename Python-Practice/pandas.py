

Pandas library usage


import pandas as pd

series = pd.Series([1,2,3,4])
print(series)

df = pd.DataFrame([[1,2,3],[4,5,6]], columns=(["rank1", "rank2", "rank3"]), index=(["one", "two"]))
print(df)


Output:

Python 3.6.1 (default, Dec 2015, 13:05:11)
[GCC 4.8.2] on linux
0    1
1    2
2    3
3    4
dtype: int64
     rank1  rank2  rank3
one      1      2      3
two      4      5      6