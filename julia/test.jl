println("a")

function test()
    println("b")
    a = 1
    println(a)
    1234
end
a=2
println(test())
a


function estimate_pi(n)
    s = 1.0
    for i in 1:n
        s += (isodd(i) ? -1 : 1) / (2i + 1)
    end
    4s
end

p = estimate_pi(100_000)
println("π ≈ $p")
println("Error is $(p - π)")

using PyCall

sys = pyimport("sys")
sys.version

py"""
import math

def estimate_pi(n):
    s = 1.0
    for i in range(1, n + 1):
        s += (-1 if i % 2 else 1) / (2 * i + 1)
    return 4 * s

p = estimate_pi(100_000)
print(f"π ≈ {p}") # f-strings are available in Python 3.6+
print(f"Error is {p - math.pi}")
varrrr=1
"""

s = "
1. the first line feed is ignored if it immediately follows \"
2. triple quotes let you use "quotes" easily
3. indentation is ignored
    - up to left-most character
    - ignoring the first line (the one with \")
4. the final line feed it n̲o̲t̲ ignored
"
println("<start>")
println(s)
println("<end>")

