if __name__ == '__main__':
    input_bytes = b'\xff\xfe4\x001\x003\x00 \x00i\x00s\x00 \x00i\x00n\x00.\x00'
    input_characters = input_bytes.decode('utf-16')
    print((repr(input_characters)))   #repr 将其他格式转化为字符串格式

    output_charachters = 'we copy you down, Eagle.\n'
    output_bytes = output_charachters.encode('utf-8')
    print(output_bytes)
