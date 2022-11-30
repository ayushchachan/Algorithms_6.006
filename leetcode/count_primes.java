
public class count_primes {

    public int countPrimes(int n) {


        int counter = 0;
        for (int i = 2; i < n; i++) {
            if (isPrime(i)) counter++;
        }
        return counter;
    }

    
}