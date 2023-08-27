import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import lagrange, approximate_taylor_polynomial

"""
    Calculates correct coefficients and graphs interpolating polynomial
    a = NDD(xpt,ypt)
    tval = np.linspace(min(xpt)-1,max(xpt)+1,100)
    yval = poly(tval,xpt,a)

    plt.plot(tval,yval,color='green',linestyle='-',label='poly')
    #Annotates graph and plots points used for interpolation
    plt.title('Interpolation')
    plt.xlabel('x values')
    plt.ylabel('y values')
    plt.legend(loc='best')
    plt.plot(xpt,ypt,color='blue',marker='o',linestyle='')
"""

xpt = np.array([0,2,3,5, 10, 16, 18, 19])
ypt = np.array([1,5,0,8, 20, 11, 30, 50])

def NDD(x,y):
    n = len(x)
    #Construct table and load xy pairs in first columns
    A = np.zeros((n,n+1))
    A[:,0]= x[:]
    A[:,1]= y[:]
    #Fill in Divided differences
    for j in range(2,n+1):
        for i in range(j-1,n):
            A[i,j] = (A[i,j-1]-A[i-1,j-1]) / (A[i,0]-A[i-j+1,0])
    #Copy diagonal elements into array for returning
    p = np.zeros(n)
    for k in range(0,n):
        p[k] = A[k,k+1]
    return p

#Evaluates polynomial at 't' given x-values and coefficients
def poly(t,x,p):
    n = len(x)
    out = p[n-1]
    for i in range(n-2,-1,-1):
        out = out*(t-x[i]) + p[i]
    return out


class Newton_Divided_Diff(object):
    """Newton's Divided difference, produces coefficients of
        interpolating polynomial
    """
    def __init__(self, xpt: np.array, ypt: np.array) -> None:
        # Calculates correct coefficients and graphs interpolating polynomial
        self.xpt = xpt
        self.ypt = ypt
        self.NDD()
        self.tval = np.linspace(min(self.xpt)-1, max(self.xpt)+1, 100)
        self.yval = self.poly()

    def NDD(self):
        n = len(self.xpt)
        #Construct table and load xy pairs in first columns
        A = np.zeros((n, n+1))
        A[:, 0]= self.xpt[:]
        A[:, 1]= self.ypt[:]
        #Fill in Divided differences
        for j in range(2, n + 1):
            for i in range(j - 1, n):
                A[i, j] = (A[i, j - 1] - A[i - 1, j - 1]) / (A[i, 0] - A[i - j + 1, 0])
        #Copy diagonal elements into array for returning
        self.p = np.zeros(n)
        for k in range(0, n):
            self.p[k] = A[k, k+1]

    def poly(self):
        """#Evaluates polynomial at 't' given x-values and coefficients

        Returns:
            array: array y values
        """
        n = len(self.xpt)
        out = self.p[n-1]
        for i in range(n-2, -1, -1):
            out = out*(self.tval - self.xpt[i]) + self.p[i]
        return out

    def show_plot(self, path:str):
        fig = plt.figure(figsize = (10,8))
        plt.plot(self.tval, self.yval, color='green', linestyle='-', label='poly')
        #Annotates graph and plots points used for interpolation
        plt.title('Newton Polynomial')
        plt.xlabel('x values')
        plt.ylabel('y values')
        plt.legend(loc='best')
        plt.grid()
        plt.plot(self.xpt, self.ypt, color='blue', marker='o', linestyle='')
        plt.savefig(path)

class Lagrange_Divided_Diff(object):
    """Larange polynomial
    """
    def __init__(self, xpt: np.array, ypt: np.array) -> None:
        self.xpt = xpt
        self.ypt = ypt
        self.f = lagrange(self.xpt, self.ypt)

    def show_plot(self, path:str):
        x_new = np.arange(-1.0, 20, 0.1)
        fig = plt.figure(figsize = (10,8))
        plt.plot(x_new, self.f(x_new), color='green', linestyle='-', label='poly')
        plt.title('Lagrange Polynomial')
        plt.grid()
        plt.xlabel('x values')
        plt.ylabel('y values')
        plt.legend(loc='best')
        plt.plot(self.xpt, self.ypt, color='red', marker='o', linestyle='')
        plt.savefig(path)

if __name__ == "__main__":
    test = Newton_Divided_Diff(xpt, ypt)
    test.show_plot("/home/ziuteng/ncd_proj/ncd_project/microservice/interpolation/dummy_name.png")

    test_1 = Lagrange_Divided_Diff(xpt, ypt)
    test_1.show_plot("/home/ziuteng/ncd_proj/ncd_project/microservice/interpolation/dummy_name_1.png")