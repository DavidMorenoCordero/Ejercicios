package java;

public class TablaDeVerdad {
    public static void main(String[] args) {
        System.out.println("A | B | A AND B | A OR B | NOT A");
        System.out.println("--------------------------------");

        boolean[] valores = {false, true};

        for (boolean A : valores) {
            for (boolean B : valores) {
                System.out.printf("%d | %d |   %d    |   %d   |   %d%n",
                        A ? 1 : 0, B ? 1 : 0, (A && B) ? 1 : 0, (A || B) ? 1 : 0, (!A) ? 1 : 0);
            }
        }
    }
}
