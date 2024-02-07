def Numero():
   while True:
        try:
            return int(input("\nInserisci un numero decimale: "))
        except ValueError:
            int(input("\nInserisci un numero decimale: "))

def ConversioneBin(numDec):
    binario = ''
    if numDec == 0:
        return '0'
    while numDec > 0:
        resto = numDec % 2
        numDec = numDec // 2
        binario = str(resto) + binario
    return binario

def ConversioneEx(numDec):
    if numDec == 0:
        return '0'
    return hex(numDec)
    
def ConversioneOtt(numDec):
    if numDec == 0:
        return '0'
    return oct(numDec)

def main():
    numDec = Numero()
    if not numDec:
        print("\nNessun numero inserito.")
    else:
        binario = ConversioneBin(numDec)
        esadecimale = ConversioneEx(numDec)
        ottale = ConversioneOtt(numDec)
        print(f"\nIl numero in binario è: {binario}")
        print(f"Il numero decimale in esadecimale è: {esadecimale}")
        print(f"Il numero decimale in ottale è: {ottale}\n")
    
if __name__ == "__main__":
    main()