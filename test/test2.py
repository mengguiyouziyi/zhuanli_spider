






# from more_itertools import chunked
# from math import ceil
# L = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# a = [sum(x) / len(x) for x in chunked(L, 12)]
# c = [x for x in chunked(L, 12)]
# b = list(chunked(L, ceil(len(L)/2)))
# print(b)







# def div_list(ls, n):
# 	if not isinstance(ls, list) or not isinstance(n, int):
# 		return []
# 	ls_len = len(ls)
# 	if n <= 0 or 0 == ls_len:
# 		return []
# 	if n > ls_len:
# 		return []
# 	elif n == ls_len:
# 		return [[i] for i in ls]
# 	else:
# 		j = ls_len / n
# 		# k = ls_len % n
# 		### j,j,j,...(前面有n-1个j),j+k
# 		# 步长j,次数n-1
# 		ls_return = []
# 		for i in range(0, (n - 1) * j, j):
# 			ls_return.append(ls[i:i + j])
# 		# 算上末尾的j+k
# 		ls_return.append(ls[(n - 1) * j:])
# 		return ls_return
#
# print(div_list([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 3))
#
#
#
# 		# x = {
# 		# 	"pid": "",
# 		# 	"tic": "",
# 		# 	"tie": "",
# 		# 	"tio": "",
# 		# 	"ano": "",
# 		# 	"ad": "",
# 		# 	"pd": "",
# 		# 	"pk": "",
# 		# 	"pno": "",
# 		# 	"apo": "",
# 		# 	"ape": "",
# 		# 	"apc": "",
# 		# 	"ipc": "",
# 		# 	"lc": "",
# 		# 	"vu": "",
# 		# 	"abso": "",
# 		# 	"abse": "",
# 		# 	"absc": "",
# 		# 	"imgtitle": "",
# 		# 	"imgname": "",
# 		# 	"lssc": "",
# 		# 	"pdt": "",
# 		# 	"debec": "",
# 		# 	"debeo": "",
# 		# 	"debee": "",
# 		# 	"imgo": "",
# 		# 	"pdfexist": "",
# 		# 	"ans": "",
# 		# 	"pns": "",
# 		# 	"sfpns": "",
# 		# 	"inc": "",
# 		# 	"ine": "",
# 		# 	"ino": "",
# 		# 	"agc": "",
# 		# 	"age": "",
# 		# 	"ago": "",
# 		# 	"asc": "",
# 		# 	"ase": "",
# 		# 	"aso": "",
# 		# 	"exc": "",
# 		# 	"exe": "",
# 		# 	"exo": ""
# 		# }
# 		# print(len(x))
