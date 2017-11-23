#!/usr/bin/python3

#
def splitAnckor(src):
    # '>>[0 9]+'を探して分割する
    dist = []
    ix   = 0
    while True:
        ix = src.find('>>')
        if ix >= 0:
            dist.append(src[:ix])
            src = src[ix:]
            iy = 2
            while iy < len(src):
                if src[iy] < '0' or src[iy] > '9':
                    break
                iy += 1
            dist.append(src[0:iy])
            src = src[iy:]
        else:
            dist.append(src)
            break

    return dist
#
def convHTML(src):
    dist = []
    for im in src:
        ank = im[0:2]
        num = im[2:]
        w   = im
        if ank == '>>' and len(num) > 0:
            w = '<a href="#' + num + '">&gt;&gt;' + num + '</a>'
        im = w
        dist.append(im)

    return dist
#
# 原文
# s = 書き込まれた文章
s = ">>1 の意見には<<賛成>>だけど、\n>>123 はいただけないな。これも参照→>>987"
# 分割
# d[0] = '>>1'
# d[1] = 'の意見には賛成だけど、\n'
# d[2] = '>>123'
# d[3] = 'はいただけないな'
d1 = splitAnckor(s)
# HTML へ変換
# '>>123'   >  <a href="#123">&gt;&gt;123</a>
d2 = convHTML(d1)
d3 = ''.join(d2)

print(d1)
print()

print(d2)
print()

print(d3)
print()
