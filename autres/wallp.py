#!/bin/python3

import os
import time


codes = [
100,
101,
102,
103,
110,
111,
112,
113,
199,
200,
201,
202,
203,
204,
205,
206,
207,
208,
214,
226,
299,
300,
301,
302,
303,
304,
305,
306,
307,
308,
400,
401,
402,
403,
404,
405,
406,
407,
408,
409,
410,
411,
412,
413,
414,
415,
416,
417,
418,
421,
422,
423,
424,
425,
426,
428,
429,
431,
451,
500,
501,
502,
503,
504,
506,
507,
508,
510,
511 ]


def main():
    while True:
        for code in codes:
            os.system(f'gsettings set org.gnome.desktop.background picture-uri-dark "https://http.cat/{code}"')
            time.sleep(300)

if __name__== "__main__":
    main()
