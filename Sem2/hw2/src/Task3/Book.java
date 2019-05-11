
package Task3;


public class Book {

    private String title;
    private boolean borrowed;

    // Создает новую книгу
    public Book(String bookTitle) {
        // Надо написать код
    }

    // Отмечает книгу как взятую
    public void borrowed() {
        // Надо написать код
    }

    // Отмечает книгу как не взятую
    public void returned() {
        // Надо написать код
    }

    // Возвращает true, если книгу уже кто-то взял
    public boolean isBorrowed() {
        // Надо написать код
    }

    // Возвращает название книги
    public String getTitle() {
        // Надо написать код
    }

    public static void main(String[] arguments) {
        // Небольшой тест для класса Book
        Book example = new Book("Дневник кота");
        System.out.println("Название книги (должно быть 'Дневник кота'): " + example.getTitle());
        System.out.println("Взята? (должно быть false): " + example.isBorrowed());
        example.rented();
        System.out.println("Взята? (должно быть true): " + example.isBorrowed());
        example.returned();
        System.out.println("Взята? (должно быть false): " + example.isBorrowed());
    }
}