package Task2;

import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Handler {

    public static ArrayList StartInput(int count) {

        Scanner sc = new Scanner(System.in);
        ArrayList emps = new ArrayList();

        for (int i = 0; i < count; i++) {
            try {
                String fio = sc.next();
                int payment = sc.nextInt();
                int time = sc.nextInt();
                Employer obj = new Employer(fio, payment, time);

                obj.PrintInfo();
                emps.add(obj);
            } catch (InputMismatchException e) {

            }
        }

        return emps;

    }

}