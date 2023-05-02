
from CryCollege.week1.cipher import XORCipher
from CryCollege.week3.weierstrass_curve import WeierstrassCurve
from CryCollege.week2.finitefield import PrimeField

BRAINPOOL_Prime = 0xe95e4a5f737059dc60dfc7ad95b3d8139515620f
BRAINPOOL_Field = PrimeField(BRAINPOOL_Prime)

CurveBrainpoolP160r1 =WeierstrassCurve(
        0x340e7be2a280eb74e2be61bada745d97e8f7c300, 
        0x1e589a8595423412134faa2dbdec95c8d8675e58, 
        BRAINPOOL_Field,
        generator=(
            0xbed5af16ea3f6a4f62938c4631eb5af7bdbcdbc3,
            0x1667cb477a1a8ec338f94741669c976316da6321
        ),
        generator_order=0xe95e4a5f737059dc60df5991d45029409e60fc09
    ) 


curve, GEN = CurveBrainpoolP160r1


key = 1337 * GEN
# Use first 32 bytes of x value as key
x_val = key.x
key = x_val.elem.to_bytes(128, "big")[:32]
cipher = XORCipher(key)
x = bytes.fromhex("4352597b4253495f427261696e706f6f6c5f4375727665735f486176655f436f666163746f725f317d")
ciphertext = cipher.dec(x)
print("Ciphertext:", ciphertext.hex())
# Output:
# Ciphertext: 4352597b4253495f427261696e706f6f6c5f4375727665735f486176655f436f666163746f725f317d