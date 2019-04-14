package Task3;

import java.util.ArrayList;
import java.util.List;

public class Handler {

    public static void copyList(List<Integer> fromCopy, List<Integer> toCopy) {

        for (int i = 0; i < fromCopy.size(); i++) {
            toCopy.add(fromCopy.get(i));
        }

    }

    public static List<Integer> rotate(List<Integer> arr) {
        List<Integer> list = new ArrayList<Integer>();
        if (arr.isEmpty()) {
            return list;
        }

        copyList(arr, list);

        int last = list.get(list.size() - 1);
        for (int i = list.size() - 1; i > 0; i--) {
            list.set(i, list.get(i - 1));
        }
        list.set(0, last);

        return list;
    }

}
