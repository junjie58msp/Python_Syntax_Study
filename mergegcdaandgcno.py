#coding:utf-8
# 主要功能：gcda 和 gcno 两个文件夹
# 要找出在两个文件夹中同前缀的文件，移动到一个结果目录
# 比如 gcda 文件夹： A.gcda, B.gcda, C.gcda 
#      gcno 文件夹： B.gcno, C.gcno, d.gcno
# 那么结果目录的文件应该是： B.gcda, B.gcno, C.gcda, C.gcno 四个文件
import os
import argparse

def mergegcdaandgcno(filepathgcda, filepathgcno, filepathmerge):
    if os.path.exists(filepathmerge):
        os.system('rm -rf '+filepathmerge)
        os.system('mkdir '+filepathmerge)
    filesgcda = os.listdir(filepathgcda)
    gcdaset =set()
    filesgcno = os.listdir(filepathgcno)
    gcnoset =set()
    for fileeache in filesgcda:
        if fileeache.endswith('.gcda'):
            gcdaset.add(fileeache.split('gcda')[0]) # FMSendGreetingCardCollectionView..gcda  
    for fileeache in filesgcno:
        if fileeache.endswith('.gcno'):
            gcnoset.add(fileeache.split('gcno')[0])
    gcdaintergcno = gcdaset.intersection(gcnoset)
    print gcdaintergcno
    for fileeache in gcdaintergcno:
        os.system('cp '+filepathgcda+'/'+fileeache+'gcda' + " "+filepathmerge+"/")
        os.system('cp '+filepathgcno+'/'+fileeache+'gcno' + " "+filepathmerge+"/")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("gcdapath", help="gcda file path")
    parser.add_argument("gcnopath", help="gcno file path")
    parser.add_argument("gcdaandgcnomergepath", help="merge gcda and gcno, get the corresponding")
    args = parser.parse_args()
    mergegcdaandgcno(args.gcdapath, args.gcnopath, args.gcdaandgcnomergepath)


if __name__ == '__main__':
    main()
	