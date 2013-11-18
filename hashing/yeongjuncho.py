#Skywave

data = raw_input().split('$')
print int(data[0][::-1]) + int(data[2][::-1]) + int(data[1])