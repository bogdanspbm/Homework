package Task2;

public class Enigma {

    static String[] firstNum = {"Один", "Два", "Три", "Четыре", "Пять", "Шесть", "Семь", "Восемь", "Девять", ""};
    static String[] secondNum = {"Десять", "Двадцать", "Тридацть", "Сорок", "Пятьдесят", "Шестьдесят", "Семдесят", "Восемдесят", "Девяносто", ""};
    static String[] thirdNum = {"Сто", "Двести", "Триста", "Четыреста", "Пятьсот", "Шестьсот", "Семьсот", "Восемьсот", "Девятьсот", ""};

    public static String intToString(int num) {

        if (num == 1000) {
            return "Тысяча";
        }

        if (num == 0) {
            return "Ноль";
        }

        String result = "";
        int fIndex, sIndex, tIndex;

        fIndex = num % 10 - 1;
        if (fIndex == -1) {
            fIndex = 9;
        }
        sIndex = (num / 10) % 10 - 1;
        if (sIndex == -1) {
            sIndex = 9;
        }
        tIndex = (num / 100) % 10 - 1;
        if (tIndex == -1) {
            tIndex = 9;
        }

        switch (num % 100) {
            case 11:
                result = "Одиннадцать";
                break;
            case 12:
                result = "Двенадцать";
                break;
            case 13:
                result = "Тринадцать";
                break;
            case 14:
                result = "Четырнадцать";
                break;
            case 15:
                result = "Пятнадцать";
                break;
            case 16:
                result = "Шестнадцать";
                break;
            case 17:
                result = "Семндацать";
                break;
            case 18:
                result = "Восемнадцать";
                break;
            case 19:
                result = "Девятнадцать";
                break;
        }

        if (result == "") {
            result = thirdNum[tIndex] + secondNum[sIndex] + firstNum[fIndex];
        } else {
            result = thirdNum[tIndex] + result;
        }

        return result;
    }

    private static int getCharInString(String str) {
        return str.length();
    }

    public static int calcCharCount() {
        int result = 0;

        for (int i = 0; i <= 1000; i++) {
            result += getCharInString(intToString(i));
        }
        return result;
    }
}
