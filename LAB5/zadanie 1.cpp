int fibonacci(int n) {
    // Tworzymy wektor do przechowywania wyników poprzednich obliczeń
    vector<int> fib_table(n + 1);

    // Pierwsze dwa elementy ciągu Fibonacciego
    fib_table[0] = 0;
    fib_table[1] = 1;

    // Obliczamy kolejne elementy ciągu Fibonacciego
    for (int i = 2; i <= n; i++) {
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2];
    }

    // Zwracamy n-ty element ciągu Fibonacciego
    return fib_table[n];
}

int main() {
    int n;
    cout << "Podaj n: ";
    cin >> n;

    int fib_n = fibonacci(n);
    cout << "n-ty element ciągu Fibonacciego: " << fib_n << endl;

    return 0;
}
