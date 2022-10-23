from encodings import CodecRegistryError


def testFormatCount(name, count, correctCount):
    print("="*8)
    print(name + " Counts")
    print(f"Actual Count: {count} \nCorrectCount :{correctCount}")
    print("Test status: " + str(count == correctCount))
    print("="*8)
    if(count != correctCount):
        return False
    else:
        return True

def testFormatSingle(name, status):
    print("="*8)
    print("Test: " + name )
    print("Test status: " + str(status))
    print("="*8)
    if(status == False):
        return False
    else:
        return True
def quitFormaT(str):
    print(str +": Fail")