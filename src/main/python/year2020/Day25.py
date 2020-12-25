card_pubkey = 2959251
door_pubkey = 4542595
# card_pubkey = 5764801
# door_pubkey = 17807724

residue = 1
card_loop = 0
while residue != card_pubkey:
    while residue < 20201227 and residue != card_pubkey:
        residue *= 7
        card_loop += 1
    residue = residue % 20201227
print("Card loop:", card_loop)
residue = 1
pow_loop = 0
while pow_loop < card_loop:
    while residue < 20201227:
        residue *= door_pubkey
        pow_loop += 1
    residue = residue % 20201227
# print((pow(door_pubkey, card_loop)) % 20201227)

print("Encryption key:", residue)
