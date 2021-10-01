# arr = list(input().split(';'))
# print(arr)
# for i in range(3):
#     arr[i]=int(arr[i])

# subject = [];seosul=[];mokjeok=[]
# if arr[0]==0 or arr[1]==0 or arr[2]==0:
#     print("No Possible sentence.;")

# for i in range(3,3+arr[0]):
#     subject.append(arr[i])

# for i in range(3+arr[0],3+arr[0]+arr[1]):
#     seosul.append(arr[i])

# for i in range(3+arr[0]+arr[1],3+arr[0]+arr[1]+arr[2]):
#     mokjeok.append(arr[i])

# print(subject)
# print(seosul)
# print(mokjeok)

    
# for i in range(arr[0]):
#     for j in range(arr[1]):
#         for k in range(arr[2]):
#             print(f"{subject[i]} {seosul[j]} {mokjeok[k]};",end="")
# print("")

def main(): 
    arr = list(input().split(';'))
    print(arr)
    for i in range(3):
        arr[i]=int(arr[i])

    subject = [];seosul=[];mokjeok=[]
    if arr[0]==0 or arr[1]==0 or arr[2]==0:
        print("No Possible sentence.;")

    for i in range(3,3+arr[0]):
        subject.append(arr[i])

    for i in range(3+arr[0],3+arr[0]+arr[1]):
        seosul.append(arr[i])

    for i in range(3+arr[0]+arr[1],3+arr[0]+arr[1]+arr[2]):
        mokjeok.append(arr[i])
        
    for i in range(arr[0]):
        for j in range(arr[1]):
            for k in range(arr[2]):
                print(f"{subject[i]} {seosul[j]} {mokjeok[k]};",end="")
    print("")

if __name__=="__main__": 
    main()