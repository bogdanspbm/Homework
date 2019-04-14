package Task3;

import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.List;
import java.util.Scanner;

public class Main {

    static List<Integer> arr;

    public static void displayArray(List<Integer> arr) {
        if (arr.isEmpty()) {
            System.out.println("ПУСТО");
        }
        for (int i = 0; i < arr.size(); i++) {
            System.err.print(arr.get(i));
        }
    }

    public static void fillList() {
        Scanner sc = new Scanner(System.in);
        System.out.println("НАЧАЛО ВВОДА, ДЛЯ ВЫХОДА ВВЕДИТЕ НЕ INT");
        try {
            int val = sc.nextInt();
            while (true) {
                arr.add(val);
                val = sc.nextInt();
            }
        } catch (InputMismatchException e) {
            // Для ввыхода нужно ввести не Int
            System.out.println("ВЫ ЗАКОНЧИЛИ ВВОД");
        }

    }

    public static void main(String[] args) {
        arr = new ArrayList<Integer>();
        fillList();
        displayArray(Handler.moveArray(arr));

    }

}
