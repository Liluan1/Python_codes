#coding: utf-8
# “ab” 是地址（Address）簿（Book）的缩写

ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'Spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])

del ab['Spammer']   #删除一对键值对

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in list(ab.items()):    #使用 items 方法来访问字典中的每一对键值对
    print('Connect {} at {}'.format(name, address))

ab['Guido'] = 'guido@python.org'    #添加一对键值对
if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])
