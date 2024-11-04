from gmpy2 import *
from Crypto.Util.number import *


# Given parameters (replace these with the values you obtained)
p = 94515040220263097875872541668071470619435707358211716562219917331797767488022053087267566586709944785329708571559126640339609375166385904147189950035630910404534642622114804635856314928438531544553236458244225698694846607333226704467932079712515971615643868209281460429629880920550469170449935295454629293399
q = 1001535514136994695529636128311212301250326767869
g = 89288700225171676599759774184146798321191748739703246395529001979988401303800066044674449834184095667747898974375431700503800142840899194492182057885675147681600217979466719692984863330298347742657472936559041930489702116255999412448996714923112824244267910808782794442895518685864174817501040060680962447941
y = 93887528695360292524813814240190328732283663255426806128197957720674496260060703595933676082882204724501085633424942582304707395449222043328895852812543576418567716781870179606049899540449729036771290550645770978667075821043797569255787271932556218014920373462882329802597672026806552417735660553144344650642
h = 775593521305134275967472254218401264703166138817
r = 75084117510316201869105133948164969652170742276
s = 599417004454208825884865529281453774324093134827
c = 94203926294365722030261882520165826558476099177297861176153811285238289485953276649563642144753132730431066372867407177248194182778827143183520415437355921352580608448713381897280433120409711633310458263502217605470824497215111936036532237050330222480782799188409969149722885261258984444311562364318406725475829089368796269160936194172040318140462371217663
k = 208672457767877303895327222020982963931779123819  # Use the correct value of k if available


x = (s * k - h) * invert(r, q) % q  

# Calculate n and phi
n = p * q
phi = (p - 1) * (q - 1)

# Recover m
d = invert(x, phi)  # Calculate d
m = pow(c, d, n)  # Recover m using n

# Convert m back to bytes and then decode
flag = long_to_bytes(m)

# Print the recovered flag
print(f"Recovered flag: {flag.decode(errors='ignore')}")