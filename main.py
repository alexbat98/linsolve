import matrixgen
import gauss
import kramer
import lu
import seidel
import iterative


def main():
    m = matrixgen.MatrixGenerator.generate_matrix(5)
    b = matrixgen.MatrixGenerator.generate_b(5)

    m1 = m.copy()
    b1 = b.copy()
    print(gauss.solve(m1, b1))

    m2 = m.copy()
    b2 = b.copy()
    print(kramer.solve(m2, b2))

    m3 = m.copy()
    b3 = b.copy()
    print(lu.solve(m3, b3))

    m4 = m.copy()
    b4 = b.copy()
    print(seidel.solve(m4, b4))

    m5 = m.copy()
    b5 = b.copy()
    print(iterative.solve(m5, b5))


if __name__ == '__main__':
    main()
