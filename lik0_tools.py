from os import system
system("clear")
print("██╗░░░░░██╗██╗░░██╗░█████╗░")
print("██║░░░░░██║██║░██╔╝██╔══██╗")
print("██║░░░░░██║█████═╝░██║░░██║")
print("██║░░░░░██║██╔═██╗░██║░░██║")
print("███████╗██║██║░╚██╗╚█████╔╝")
print("╚══════╝╚═╝╚═╝░░╚═╝░╚════╝░")

print("████████╗░█████╗░░█████╗░██╗░░░░░░██████╗")
print("╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝")
print("░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░")
print("░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗")
print("░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝")
print("░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░")
print("code writed by lik0")
print("     ")

print("YAPILABİLECEK İŞLEMLER")
print("1.txt dosyası oluşturma")
print("2.İnternet bağlantını kes")
print("3.internete yeniden bağlan")
print("4.sudo su")
print("5.görsel şölen")
print("6.çıkış")

print("      ")
secenek = input('seçiniz : ')
if(int(secenek)>6):
    print("lütfen geçerli bir sayı giriniz")
    import sys
    sys.exit
if(int(secenek)==1):
    print("Not : işlemi nerdeyken yaparsanız oraya txt dosyayı oluşturulur")
    print("Not2 : yazıcağınız dosya isminde boşluk yerine _ kullanınız ")
    print("   ")
    dosya_adı = input("txt dosyasının ismini belirleyiniz : ")
    from os import system
    system("touch "+dosya_adı)
if(int(secenek)==2):
    from os import system
    system("service NetworkManager stop")
if(int(secenek)==3):
    from os import system
    system("service NetworkManager restart")
if(int(secenek)==4):
    from os import system
    system("sudo su")
if(int(secenek)==5):
    while True:
        import time
        print("██                             ██                                      ██")
        time.sleep(0.05)                       
        print(" ██                              ██                                   ██")
        time.sleep(0.05)
        print("  ██                           ██                                    ██")
        time.sleep(0.05)
        print("   ██                            ██                                 ██")
        time.sleep(0.05)
        print("    ██                         ██                                  ██")
        time.sleep(0.05)
        print("     ██                          ██                               ██")
        time.sleep(0.05)
        print("      ██                       ██                                ██")
        time.sleep(0.05)
        print("       ██                        ██                             ██")
        time.sleep(0.05)
        print("        ██                     ██                              ██")
        time.sleep(0.05)
        print("         ██                      ██                           ██")
        time.sleep(0.05)
        print("          ██                   ██                            ██")
        time.sleep(0.05)
        print("           ██                    ██                         ██")
        time.sleep(0.05)
        print("            ██                 ██                          ██")
        time.sleep(0.05)
        print("             ██                  ██                       ██")
        time.sleep(0.05)
        print("            ██                 ██                          ██")
        time.sleep(0.05)
        print("           ██                    ██                         ██")
        time.sleep(0.05)
        print("          ██                   ██                            ██")
        time.sleep(0.05)
        print("         ██                      ██                           ██")
        time.sleep(0.05)
        print("        ██                     ██                              ██")
        time.sleep(0.05)
        print("       ██                        ██                             ██")
        time.sleep(0.05)
        print("      ██                       ██                                ██")
        time.sleep(0.05)
        print("     ██                          ██                               ██")
        time.sleep(0.05)
        print("    ██                         ██                                  ██")
        time.sleep(0.05)
        print("   ██                            ██                                 ██")
        time.sleep(0.05)
        print("  ██                           ██                                    ██")
        time.sleep(0.05)
        print(" ██                              ██                                   ██")
        time.sleep(0.05)  
if(int(secenek)==6):
    print("hadi bb")
    import sys
    sys.exit()