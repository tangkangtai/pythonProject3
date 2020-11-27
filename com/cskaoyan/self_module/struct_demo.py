#struct
#struct的pack函数 把任意数据类型变成bytes
import struct

#pack第一个参数是处理命令, >表示字节顺序是big-endian,也就是网络序
#   I表示4字节无符号整数
#后面的参数个数要和处理指令一致

print(struct.pack('>I',10240099))

# >IH的说明  后面的bytes一次变为 I：4字节无符号整数  H: 2字节无符号整数
print(struct.unpack('>IH',b'\xf0\xf0\xf0\xf0\x80\x80'))


def bmp_info(data):
    result = struct.unpack('<ccIIIIIIHH',data[:30])
    if result[0:2] == (b'B',b'M'):
        return {
            'width':result[6],
            'height':result[7],
            'color':result[9]
        }

    print('this is not a bmp file')

test_x = (b'B',b'M',3,4,5,6)
print(test_x[:2] == (b'B',b'M'))
