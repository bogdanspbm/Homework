package Task3;

public class Library {
    // Сюда надо добавить недостающие методы

    public static void main(String[] args) {
        // Создаем две библиотеки
        Library firstLibrary = new Library("Университетский пр., 120");
        Library secondLibrary = new Library("Московский пр., 86");

        // Добавляем четыре книги в первую библиотеку
        firstLibrary.addBook(new Book("Код да Винчи")); // При добавлении на экран должно выводиться сообщение об успешном добавлении соответствующей книги
        firstLibrary.addBook(new Book("50 оттенков серого"));
        firstLibrary.addBook(new Book("Учебник мемологии"));
        firstLibrary.addBook(new Book("Властелин Колец"));

        // Выводим на экран часы работы и адреса
        System.out.println("Часы работы библиотек:");
        printOpeningHours(); // Что-то типа "Все библиотеки работают с понедельника по субботу с 9 до 18", текст на ваше усмотрение
        System.out.println();

        System.out.println("Адреса библиотек:");
        firstLibrary.printAddress(); // Выводит адрес
        secondLibrary.printAddress();
        System.out.println();

        // Пытаемся взять Властелина Колец из обеих библиотек
        System.out.println("Берем лучшую книгу на земле:");
        firstLibrary.borrowBook("Властелин Колец");   // Должно пройти успешно, мы должны получить соответствующее сообщение об успехе
        firstLibrary.borrowBook("Властелин Колец");   // Книга уже взята, об этом нам должны написать
        secondLibrary.borrowBook("Властелин Колец");  // Такой книги нет в каталоге, это тоже отдельное сообщение для нас
        System.out.println();

        // Выводим названия всех книг в обеих библиотеках
        System.out.println("Доступные книги в первой библиотеке:");
        firstLibrary.printAvailableBooks();  // Только список книг, которые можно взять
        System.out.println();
        System.out.println("Доступные книги во второй библиотеке:");
        secondLibrary.printAvailableBooks(); // Так как во вторую книг не добавляли, то тут надо написать что-то типа "В каталоге пусто"
        System.out.println();

        // Возвращаем Властелина Колец в первую библиотеку
        System.out.println("Прочитали Властелина Колец, возвращаем:");
        firstLibrary.returnBook("Властелин Колец"); // Сообщение об успешном возвращении
        System.out.println();

        // Снова выводим список доступных книг в первой библиотеке
        System.out.println("Доступные книги в первой библиотеке:");
        firstLibrary.printAvailableBooks();
    }
}