class Recursividad:

    # 1. Factorial
    def factorial_iterativo(self, n: int) -> int:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

    def factorial_recursivo(self, n: int) -> int:
        if n == 0:  # caso base
            return 1
        else:  # caso recursivo
            return n * self.factorial_recursivo(n - 1)

    # 2. Fibonacci
    def fibonacci_rec(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            return self.fibonacci_rec(n - 1) + self.fibonacci_rec(n - 2)

    def fibonacci_iter(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    # 3. Imprimir
    def imprimir(self, n: int) -> None:
        if n <= 0:  # caso base
            return
        print(n)
        self.imprimir(n - 1)

    def imprimir_descendente(self, n: int) -> None:
        if n <= 0:  # caso base
            return
        print(n)
        self.imprimir_descendente(n - 1)

    def imprimir_ascendente(self, n: int) -> None:
        if n <= 0:  # caso base
            return
        self.imprimir_ascendente(n - 1)
        print(n)

        # 4. Inversor de cadenas
    def invertir_cadena(self, cadena: str) -> str:
        if len(cadena) <= 1:  # caso base
            return cadena
        else:  # caso recursivo
            return self.invertir_cadena(cadena[1:]) + cadena[0]

        # 5. Ecuación recurrente: a(n) = 2*a(n-1) + 1, con a(0) = 0
    def ecuacion_recurrente(self, n: int) -> int:
        if n == 0:  # caso base
            return 0
        return 2 * self.ecuacion_recurrente(n - 1) + 1