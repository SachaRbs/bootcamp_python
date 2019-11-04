import sys

def    ft_progress(liste):
    count = len(liste)
    def    _show(_i):
        x = int(1000*_i/count)
        sys.stdout.write("%s[%s%s] %i/%i\r" % ("Compilation", "#"*x, "."*(1000-x), _i, count))
        sys.stdout.flush()

    _show(0)
    for i, item in enumerate(liste):
        yield item
        _show(i+1)
    sys.stdout.write("\n")
    sys.stdout.flush()