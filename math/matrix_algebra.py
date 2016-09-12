# Matrix Algebra
import numpy as np
A = [[1,2,3],[2,7,4]]
B = [[1,-1],[0,1]]
C = [[5,-1],[9,1],[6,0]]
D = [[3,-2,-1],[1,2,3]]
u = [6,2,-3,5]
v = [3,5,-1,4]
w = [[1],[8],[0],[5]]

# print u, v, w

matrixA = np.matrix(A)
matrixB = np.matrix(B)
matrixC = np.matrix(C)
matrixD = np.matrix(D)
matrixu = np.matrix(u)
matrixv = np.matrix(v)
matrixw = np.matrix(w)


#1.1) Write the dimensions of A
print "Dimensions of A", matrixA.shape
# 1.2) Write the dimensions of B
print "Dimensions of B", matrixB.shape
# 1.3) Write the dimensions of C
print "Dimensions of C", matrixC.shape
# 1.4) Write the dimensions of D
print "Dimensions of D", matrixD.shape
# 1.5) Write the dimensions of u
print "Dimensions of u", matrixu.shape
# 1.6) Write the dimensions of w
print "Dimensions of w", matrixw.shape

print "Dimensions of v", matrixv.shape

print "2.1) u + v: ", matrixu + matrixv
print "2.2) u - v: ", matrixu - matrixv
print "2.3) alpha * u", 6 * matrixu
# print "2.4) u * v", np.dot(matrixu,matrixv)
print "2.5) absolute value u", np.absolute(u)

print "3.1 A + C ", "Not Defined"
transposeC = matrixC.transpose()
print "3.2) A - C(Transpose)", "\n", matrixA - transposeC

threeMatrixD = matrixD*3
print "3.3) C(Tranpose) + 3D", "\n", transposeC + threeMatrixD

print "3.4) B * A", "\n", matrixB * matrixA

transposeA = matrixA.transpose()
# print "3.5) BAT", "\n", matrixB * transposeA
print "3.5) Not Defined"

print "3.6) BC = Not Defined"
print "3.7) CB = ", "\n", matrixC * matrixB
