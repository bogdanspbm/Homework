package Task2;

import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.List;
import java.util.Scanner;

public class Handler {

    private static List<Employee> emps;

    public static List<Employee> startInput() {

        Scanner sc = new Scanner(System.in);
        int count = 0;
        try {
            System.out.print("Введите кол-во рабочих: ");
            count = sc.nextInt();
        } catch (InputMismatchException e) {
            System.out.println("НЕ УДАЛОСЬ ВВЕСТИ КОЛ-ВО РАБОЧИХ");
            System.exit(0);
        }
        emps = new ArrayList<Employee>();

        for (int i = 0; i < count; i++) {
            System.out.println("Введите данные " + (i + 1) + "-ого рабочего:");
            try {
                System.out.print("Имя: ");
                String fio = sc.next();
                System.out.print("Оплата часа (70-inf): ");
                int payment = sc.nextInt();
                System.out.print("Кол-во часов (0-60): ");
                int time = sc.nextInt();
                Employee obj = new Employee(fio, payment, time);
                emps.add(obj);
            } catch (InputMismatchException e) {
                System.out.println("ОШИБКА ВВОДА. РАБОЧИЙ НЕ ДОБАВЛЕН.");
                System.out.println("ПОПРОБУЙТЕ ЕЩЕ РАЗ");
                sc.next();
                i--;
            }
        }

        return emps;
    }

    public static void displayInfo() {
        if (emps.isEmpty()) {
            System.out.println("ПУСТО");
        } else {
            Employee cEmp;
            String outp;
            System.out.println("ФИО СТАВКА_В_ЧАС КОЛИЧЕСТВО_ЧАСОВ ЗАРПЛАТА");
            for (int i = 0; i < emps.size(); i++) {
                cEmp = emps.get(i);
                outp = "";
                outp += cEmp.fio + " " + cEmp.payment + " " + cEmp.hours;
                outp += " " + cEmp.salary;
                System.out.println(outp);
            }
        }
    }

}
