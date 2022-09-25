# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 23:07:49 2022

@author: DELL
"""

import hashlib

def hashGenerator(data):
    result=hashlib.sha256(data.encode())
    return result.hexdigest()

class Block:
    def __init__(self,data,hash,prev_hash):
        self.data=data
        self.hash=hash
        self.prev_hash=prev_hash

class Blockchain:
    def __init__(self):
      Prevhash=hashGenerator('previous_hash_value')
      CurrentStart=hashGenerator('current_hash_value')

      genesis=Block('current_data',CurrentStart,Prevhash)
      self.chain=[genesis]

    def add_block(self,data):
        prev_hash=self.chain[-1].hash
        hash=hashGenerator(data+prev_hash)
        block=Block(data,hash,prev_hash)
        self.chain.append(block)

bc=Blockchain()
bc.add_block('1')
bc.add_block('2')
bc.add_block('3')

for block in bc.chain:
    print(block.__dict__)
