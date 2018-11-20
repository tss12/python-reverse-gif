from PIL import Image, ImageSequence

im = Image.open(r'./zr651.gif') #注意把gif动图放在该程序的相同目录下
sequence = []

for f in ImageSequence.Iterator(im):
    sequence.append(f.copy())    

sequence.reverse()
sequence[0].save(r'./out_zr651.gif',save_all = True, append_images=sequence[1:]) #倒放的gif图保存在当前目录下
