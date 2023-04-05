def thaphanoi(n,cotA, cotB, cotC):
    if n == 1:
        print("chuyển từ",cotA,"sang",cotC )
        return
    else:
        thaphanoi(n-1,cotA, cotC, cotB)
        print("chuyển từ",cotA,"sang",cotC)
        thaphanoi(n-1,cotB,cotA,cotC)



def main():
    n=int(input("nhap so n tang = "))
    thaphanoi(n, "cotA", "cotB", "cotC")

if __name__ =='__main__':
    main()