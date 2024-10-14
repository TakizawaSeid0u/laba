input_data = open('input.txt','r')
data = input_data.read()
data = data.split()
c = int(data[0])
h = int(data[1])
o = int(data[2])
v = int(h / 6)
b = int(c / 2)
n = 0
if int(v) > 1:
    if int(o) < int(v):
        if int(b) > int(o):
            output_data = open('output.txt','w')
            output_data.write(str(v))
            input_data.close
            output_data.close
        else:
            output_data = open('output.txt','w')
            output_data.write(str(o))
            input_data.close
            output_data.close
else:
    output_data = open('output.txt','w')
    output_data.write(str(n))
    input_data.close
    output_data.close
