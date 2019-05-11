package Task2;

public class Enigma {

    static String[] firstNum = {"Один", "Два", "Три", "Четыре", "Пять", "Шесть", "Семь", "Восемь", "Девять", ""};
    static String[] secondNum = {"Десять", "Двадцать", "Тридацть", "Сорок", "Пятьдесят", "Шестьдесят", "Семдесят", "Восемдесят", "Девяносто", ""};
    static String[] thirdNum = {"Сто", "Двести", "Триста", "Четыреста", "Пятьсот", "Шестьсот", "Семьсот", "Восемьсот", "Девятьсот", ""};

    public static String intToString(int num) {

        StringBuilder result = new StringBuilder();

        if (num == 1000) {
            return "Тысяча";
        }

        if (num == 0) {
            return "Ноль";
        }

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
                result.append("Одиннадцать");
                break;
            case 12:
                result.append("Двенадцать");
                break;
            case 13:
                result.append("Тринадцать");
                break;
            case 14:
                result.append("Четырнадцать");
                break;
            case 15:
                result.append("Пятнадцать");
                break;
            case 16:
                result.append("Шестнадцать");
                break;
            case 17:
                result.append("Семндацать");
                break;
            case 18:
                result.append("Восемнадцать");
                break;
            case 19:
                result.append("Девятнадцать");
                break;
        }

        if (result.toString().isEmpty()) {
            result.append(thirdNum[tIndex]);
            result.append(secondNum[sIndex]);
            result.append(firstNum[fIndex]);
        } else {
            result.append(thirdNum[tIndex]);
        }

        return result.toString();
    }

    private static int getCharInString(String str) {
        return str.length();
    }

    public static int calcCharCount() {
        int result = 0;

        for (int i = 1; i <= 1000; i++) {
            result += getCharInString(intToString(i));
        }
        return result;
    }
}
