from PIL import Image
import argparse#管理命令行参数输入

#命令行输入参数处理，判断输入参数
parser = argparse.ArgumentParser()

parser.add_argument('file')     #输入文件
parser.add_argument('-o', '--output')   #输出文件
parser.add_argument('--width', type = int, default = 80) #输出字符画宽
parser.add_argument('--height', type = int, default = 80) #输出字符画高

#获取输入的参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output


#字符画所用到字符列表
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

#把256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
	if alpha ==0:
		return ' '
	length = len(ascii_char)
	gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
	
	unit = (256.0+1)/length
	return ascii_char[int(gray/unit)]#调用字符
	
if __name__ =='__main__':
	im = Image.open(IMG)#打开处理的图片
	im = im.resize((WIDTH,HEIGHT), Image.NEAREST)#设置输出的高度宽度
	
	txt = ""
	
	for i in range(HEIGHT):
		for j in range(WIDTH):
			#getpixel获取（j,i）处像素值，得到r,g,b信息
			#根据高度宽度依次获取像素值转换成字符
			txt += get_char(*im.getpixel((j,i)))
		txt +='\n'
	
	print(txt)

	if OUTPUT:
		with open(OUTPUT,'w') as f:
			f.write(txt)
	else:
		with open("output.txt",'w') as f:
			f.write(txt)
