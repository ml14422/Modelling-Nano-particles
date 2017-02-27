"""Program that modules brownian motion of 
   particle through stochastic force """

from random import randint
import sys
import math
import argparse
import matplotlib.pyplot as plt

def main(argv):
    """Parse args and do calc"""
    parser = argparse.ArgumentParser(prog='gmpsf',
                                     description="""
                                     calculates and graphs motionof partical 
                                     through stochastic force
                                     """)
    #parse all the arguments
    parser.add_argument("-n", required=True, type=int, dest="count", help="Data point count")
    parser.add_argument("-dt", required=True, type=float, dest="dt", help="Time increment")
    parser.add_argument("-b", required=True, type=float, dest="b", help="Nms⁻¹")
    parser.add_argument("-kb", required=True, type=float, dest="kb", help="Boltzmann constant(JK⁻¹)")
    parser.add_argument("-t", required=True, type=float, dest="t", help="Temperature(K)")
    args = parser.parse_args(argv)

    # map the step range (0..step) to random vectors(tuples)
    vectors = [(randint(0, 100), randint(0, 100)) for n in range(0, args.count)]
    print(vectors)
    # map our random vectors to solved 2D vectors
    mapped = [solve(v, args.dt*(i+1), args.b, args.kb, args.t) for i, v in enumerate(vectors)]
    print(mapped)
    # zip all tuples (i.e [(a,b,c),(d,e,f)] -> [(a,d),(b,e),(c,f)]) and plot it
    plotVectors(mapped)
    rms = [(math.sqrt(v[0]**2 + v[1]**2), args.dt*i) for i, v in enumerate(mapped)]
    plotVectors(rms)

def plotVectors(vectors):
    plt.scatter(*zip(*vectors))
    plt.show()

def solve(vector2D: (float, float), dt, b, kb, t) -> (float, float):
    return (
        solve1D(vector2D[0], dt, b, kb, t),
        solve1D(vector2D[1], dt, b, kb, t)
        )

def solve1D(value, dt, b, kb, t):
    return  math.sqrt(((6*kb*t) / (b*dt))) * value * (dt/b)

if __name__ == "__main__":
    main(sys.argv[1:])
