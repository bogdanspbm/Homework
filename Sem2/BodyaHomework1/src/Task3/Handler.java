package Task3;

public class Handler {

    public static void MoveArray(int[] arr) {
        int last = arr[arr.length - 1];
        for (int i = arr.length - 1; i > 0; i--) {
            arr[i] = arr[i - 1];
        }
        arr[0] = last;
    }

    public static void DisplayArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.err.print(arr[i]);
        }
    }

}
