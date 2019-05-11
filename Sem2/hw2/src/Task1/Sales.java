package Task1;

public class Sales {

    static public int getSale(int fakeSale) {
        int result = 0;
        int tmpResult = fakeSale;
        while (tmpResult != 0) {
            result += tmpResult % 10;
            tmpResult /= 10;
        }

        if (result >= 10) {
            result = getSale(result);
        }
        return result;
    }
}
