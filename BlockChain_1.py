'''
NeuralCoin (NC)

Transaction t1: Kamalesh sends Resh 999.36 NC
Transaction t2: Resh sends Univ 369.9 NC
Transaction t3: Cosmo sends Tesla 9639.5 NC

Block B1("Initial", t1, t2, t3) ---> SHA256 Alphanumeric Number ---> eg. fah4djjdl
Block B2("fah4djjdl", t4, t5, t6) ---> SHA256 Alphanumeric Number ---> eg. bdjs73ji
Block B3("bdjs73ji", t7) ---> SHA256 Alphanumeric Number ---> eg. kefkmek55

Altering any one of the transaction will give a complete different BlockID at each blocks,
this is how BlockChain integrity is maintained 

'''

import hashlib

class NeuralCoinBlock:
    
    #constructor/ Initializer
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        
        #Seperator for the BlockData between transaction
        self.block_data = "-".join(transaction_list)+ "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
        

t1 = "Kamalesh sends Resh 999.36 NC"
t2 = "Resh sends Univ 369.5 NC"
t3 = "Cosmo sends Tesla 9639.5 NC"
t4 = "Leo sends taurus 333.3 NC"
t5 = "Gemini sends Andromeda 666.66 NC"
t6 = "Solar sends System 936.99369 NC"

initial_block = NeuralCoinBlock("Initial String", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)
print('-'*100)

second_block = NeuralCoinBlock(initial_block.block_hash, [t3, t4])

print(second_block.block_data)
print(second_block.block_hash)
print('-'*100)

third_block = NeuralCoinBlock(second_block.block_hash, [t5, t6])

print(third_block.block_data)
print(third_block.block_hash)
print('-'*100)