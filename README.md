# fibonacci-python

[![CircleCI](https://circleci.com/gh/xaoc-303/fibonacci-python/tree/master.svg?style=shield)](https://circleci.com/gh/xaoc-303/fibonacci-python/tree/master)

## recursive if-else

| v | # | 30 | 35 | 40 | 45 |
| --- | --- | --- | --- | --- | --- |
| 3.7.0 | [Python](./fibo.py) | 0.32678509 | 3.54449487 | 38.80285716 | 478.11391401 |
| | [Total](https://github.com/xaoc-303/fibonacci) | | | | |

## optimization

| v | # | 30 | 35 | 40 | 45 |
| --- | --- | --- | --- | --- | --- |
| 3.7.0 | [Python](./fibo.py) | 0.00000501 | 0.00000501 | 0.00000620 | 0.00000691 |
| | [Total](https://github.com/xaoc-303/fibonacci) | | | | |

## run

```
time python3.7 main.py f1 30
time python3.7 main.py f2 30
```

```
python3 -m unittest -v fibo_test.py
```
