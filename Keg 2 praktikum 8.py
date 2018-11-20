def konfersisuhu(C=0, F=0):
    "konversi dari c ke f"
    ckf = 1.8*C + 32
    fkc = 0.55555555555*(F - 32)
    if (C >= 0 and F == 0):
        print('Suhu ', C, 'c setara dengan ', ckf, 'f')
    elif (F >= 0 and C == 0):
        print('Suhu ', F, 'f setara dengan ', fkc, 'c')
    return;
