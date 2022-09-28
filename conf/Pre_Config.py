#!/usr/scripts/env python
# encoding: utf-8 

"""
@author: Swindler
@contact: 1033199817@qq.com
@file: Pre_Config.py
@time: 5/19/22 7:26 PM
@function: 配置文件
"""

# 最大染色体长度
MAX_CHROMOSOME_LENGTH = 250000000  # 250Mb

# 预定义ColorRange
COLOR_RANGE_SETS = {
    2500000: 6361,
    1250000: 1607,
    1000000: 1650,
    500000: 262,
    250000: 192,
    125000: 126,
    100000: 45,
    50000: 26,
    25000: 15,
    12500: 5,
    10000: 7,
    5000: 5,
    2500: 2,
    1000: 2,
    500: 2}

# 预定义长宽
LEN_WIDTH_SETS = {
    2500000: 300000000,  # 300M
    1250000: 300000000,  # 300M
    1000000: 200000000,  # 200M
    500000: 200000000,  # 200M
    250000: 150000000,  # 150M
    125000: 100000000,  # 100M
    100000: 70000000,  # 70M
    50000: 50000000,  # 50M
    25000: 25000000,  # 25M
    12500: 18000000,  # 18M
    10000: 14000000,  # 14M
    5000: 5000000,  # 5M
    2500: 3600000,  # 3.6M
    1000: 1445000,  # 1.4M
    500: 720000  # 720K
}

# 预定义增量，详细版
INCREMENT_SETS_DETAIL = {
    2500000: 150000000,  # 300M
    1250000: 150000000,  # 300M
    1000000: 100000000,  # 200M
    500000: 100000000,  # 200M
    250000: 80000000,  # 150M
    125000: 50000000,  # 100M
    100000: 40000000,  # 70M
    50000: 25000000,  # 50M
    25000: 13000000,  # 25M
    12500: 9000000,  # 18M
    10000: 7000000,  # 14M
    5000: 2500000,  # 5M
    2500: 1800000,  # 3.6M
    1000: 700000,  # 1.4M
    500: 360000  # 720K
}

# 预定义增量，快速版
INCREMENT_SETS_FAST = {
    2500000: 250000000,  # 200M
    1250000: 250000000,  # 200M
    1000000: 195000000,  # 150M
    500000: 195000000,  # 150M
    250000: 145000000,  # 100M
    125000: 95000000,  # 80M
    100000: 65000000,  # 50M
    50000: 45000000,  # 30M
    25000: 24000000,  # 20M
    12500: 17000000,  # 15M
    10000: 13000000,  # 10M
    5000: 4000000,  # 4M
    2500: 3000000,  # 3M
    1000: 1400000,  # 1M
    500: 710000}  # 700K

# 用于获取错误矩阵时，预防矩阵长度超出分辨率的限制
RSE_MAX_LEN = {
    2500000: 3610000000,
    1250000: 1800000000,
    1000000: 1445000000,
    500000: 722000000,
    250000: 361400000,
    125000: 180740000,
    100000: 144500000,
    50000: 72299000,
    25000: 36149000,
    12500: 18070000,
    10000: 14450000,
    5000: 7229000,
    2500: 3614000,
    1000: 1445000,
    500: 722900}