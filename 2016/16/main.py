def expand_data(data, length):
    while len(data) < length:
        data = '{}0{}'.format(data, ''.join('1' if x == '0' else '0' for x in data[::-1]))
    return data[0:length]

def calc_checksum(data):
    checksum = ''
    pairs = [data[i:i + 2] for i in range(0, len(data), 2)]
    for pair in pairs:
        checksum += str(int((pair[0] == pair[1])))
    return checksum;

def data_checksum(data):
    checksum = calc_checksum(data)
    if len(checksum) % 2 == 0:
        return data_checksum(checksum)
    return checksum


length = 272
length = 35651584
data = '11011110011011101'

print('edata start')
edata = expand_data(data, length)
print('edata done')

print('checksum start')
cs = data_checksum(edata)
print('checksum done')
print(cs)
