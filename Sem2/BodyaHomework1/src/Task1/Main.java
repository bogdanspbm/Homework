package Task1;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {

    private static void inputException() {
        System.out.println("НЕ ВЕРНЫЙ ВВОД");
        System.exit(0);
    }

    public static void main(String[] args) {

        int val = 0;
        Scanner sc = new Scanner(System.in);

        System.out.print("Введите число: ");

        try {
            val = sc.nextInt();

            if (val < 0) {
                inputException();
            }
        } catch (InputMismatchException e) {
            inputException();
        }

        IntToBinary myInt = new IntToBinary(val);
        System.out.println(myInt.toBinary());

    }

}
