import randomorg as ro

def randomstr():
    rand = ro.string(num=1, length=10, digits=False, upper=True,
                         lower=True, unique=True)
    randstr = str(rand)[2:-2]
    return randstr
