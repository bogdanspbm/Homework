package Task1;

public final class IntToBinary {

    public int integer;
    public String binary;

    public IntToBinary(int val) {
        this.integer = val;
        this.binary = toBinary();
    }

    private String rotateString(String str) {
        String result = "";

        for (int i = 0; i < str.length(); i++) {
            result += str.charAt(str.length() - 1 - i);
        }

        return result;

    }

    public String toBinary() {
        String result = "";
        int tmp = this.integer;

        while (tmp != 0) {
            result += (tmp % 2);
            tmp /= 2;
        }

        if (result == "") {
            result = "0";
        }

        return rotateString(result);
    }
}
