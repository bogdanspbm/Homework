package Task1;

public class IntToBinary {

    public static String JavaIntToBinary(int val) {
        return Integer.toBinaryString(val);
    }

    private static String RotateString(String str) {
        String result = "";

        for (int i = 0; i < str.length(); i++) {
            result += str.charAt(str.length() - 1 - i);
        }

        return result;

    }

    public static String MyIntToBinary(int val) {
        String result = "";
        int tmp = val;

        while (tmp != 0) {
            result += (tmp % 2);
            tmp /= 2;
        }

        if (result == "") {
            result = "0";
        }

        return RotateString(result);
    }

    public static void DebugProgram(int depth) {
        int rand;

        for (int i = 0; i < depth; i++) {
            rand = (int) (Math.random() * 100);
            System.out.println("Test - " + (i + 1));
            System.out.println(MyIntToBinary(rand));
            System.out.println(JavaIntToBinary(rand));
            System.out.println();
        }
    }

}
