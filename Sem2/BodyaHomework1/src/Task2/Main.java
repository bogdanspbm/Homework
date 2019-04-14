package Task2;

import java.util.ArrayList;

public class Main {
     public static void DisplayInfo(ArrayList<Employer> emps) {

        System.out.println("ФИО СТАВКА_В_ЧАС КОЛИЧЕСТВО_ЧАСОВ ЗАРПЛАТА");
        for (int i = 0; i < emps.size(); i++) {
            emps.get(i).PrintInfo();
        }
    }

    public static void main(String[] args) {
        DisplayInfo(Handler.StartInput(2));
        
    }

}
