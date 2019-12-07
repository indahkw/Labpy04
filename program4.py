data=[]
while(True):
    nama=input("Masukan nama : ")
    nim=input("Masukan nim : ")
    tugas=int(input("Masukan Nilai Tugas : "))
    uts=int(input("Masukan Nilai Uts : "))
    uas=int(input("Masukan Nilai Uas : "))
    akhir = (30 * tugas / 100) + (35 * uts / 100) + (35 * uas / 100)
    data.append([nama, nim, tugas, uts, uas, akhir])
    ulangi=input("Tambah data (y/t)?")
    if ulangi.lower() == 't':
        break;

print("\nDaftar Nama\n")
print("==========================================================================================")
print("|         NAMA         |        NIM        |    TUGAS    |   UTS   |   UAS   |   AKHIR   |")
print("==========================================================================================")
for x in data:
    print("| {0:20} | {1:17} | {2:11} | {3:7} | {4:7} | {5:9} |".format(x[0], x[1], x[2], x[3], x[4], x[5]))
print("==========================================================================================")