package Task1;

import static Task1.Sales.getSale;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner reader = new Scanner(System.in);
        System.out.println("Enter a sale: ");
        int saleF = reader.nextInt(); 
        System.out.print("Real Sale: " + getSale(saleF) + "\n");

    }

}
