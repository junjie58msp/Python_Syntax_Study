#coding: utf-8
#author: jayjay

import os
import argparse

def clearinfoDA0(infofileinput, infofileoutput):
    if not os.path.exists(infofileinput):
        raise Exception("value")
    if os.path.exists(infofileoutput):
        os.system('rm -rf '+infofileoutput)
    else:
        os.system('touch '+ infofileoutput)
    with open(infofileoutput,'w') as fpout:
        with open(infofileinput,'r') as fpin:
            for eachline in fpin:
                if eachline.strip().startswith('DA:') and eachline.strip().endswith(",0"):
                    pass
                else:
                    fpout.write(eachline)


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("infofileinput", help="input the info file")
    argparser.add_argument("infofileoutput", help="output info file")
    args = argparser.parse_args()
    clearinfoDA0(args.infofileinput, args.infofileoutput)

if __name__ == "__main__":
    main()
