import asyncio
# from time import sleep
rocket = [0]
alphabet = "abcdefghijklmnopqrstuvwxyz"


async def fnum():
    print('start fnum')
    l=0
    while l<200:
        filr = open("input.txt", "r")
        l=len(filr.readlines())
        fila = open("input.txt", "a")
        fila.write(f"f1:{l} -> {l}\n")
        await asyncio.sleep(0.1)
        fila.close()
    print('end fnum')


async def fchar():
    print('start fchar')
    l=0
    while l< 200:
        filr = open("input.txt", "r")
        l=len(filr.readlines())
        fil2 = open("input.txt", "a")
        fil2.write(f"f2:{l} -> {alphabet[l%26]}\n")
        await asyncio.sleep(0.1)
        fil2.close()
    print('end fchar')


async def fbool():
    print('start fbool')
    l=0
    while l < 200:
        filr = open("input.txt", "r")
        l=len(filr.readlines())
        fil3 = open("input.txt", "a")
        fil3.write(f"f3:{l} -> {bool(l%2)}\n")
        await asyncio.sleep(0.1)
        fil3.close()
    print('end fbool')


if __name__ == '__main__':
    def main():
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.gather(fnum(), fchar(), fbool()))
        loop.close()
    print("debut")
    main()
    # a=open("input.txt", "w")
    # a.close()
    # # launch the coroutines
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(asyncio.gather(fnum(), fchar(), fbool()))


    # p1 = Process(target=fnum)
    # sleep(0.02)
    # p1.start()
    # p2 = Process(target=fbool)
    # sleep(0.02)
    # p2.start()
    # sleep(0.02)
    # print("debut?")
    # fchar()
    print("fin?")
