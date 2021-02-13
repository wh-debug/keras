'''
Author: 零到正无穷
Date: 2021-02-08 22:10:43
LastEditTime: 2021-02-08 22:38:54
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \TensorFlow\test_file_write_read.py
'''
dict_data = [{'Address': 'CKYsrEiJBrUGXfKYGrr4PkCLbRQn5TiXCm',
  'miner_balance': 197561652,
  'miner_recieved': 197561652,
  'miner_sent': 0,
  'top': 98,
  'turnover_rate': '0%'},
 {'Address': 'CQ7CtUqNzbQCUMrpvK6KRx36iNd4sUtEj6',
  'miner_balance': 789587472,
  'miner_recieved': 195821124,
  'miner_sent': 593766347,
  'top': 99,
  'turnover_rate': '75.20%'},
 {'Address': 'CVgM6SEWL339zmd9Wqjspoe6iyCHtCeK6v',
  'miner_balance': 415825423,
  'miner_recieved': 187499058,
  'miner_sent': 228326365,
  'top': 100,
  'turnover_rate': '54.91%'}]
print(pd.DataFrame(list(dic_data)))