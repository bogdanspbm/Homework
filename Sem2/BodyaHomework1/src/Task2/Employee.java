package Task2;

public class Employee {

    String fio, salary = "";
    int payment = 0, hours = 0;

    public Employee(String newfio, int newmoney, int newtime) {
        this.fio = newfio;
        this.payment = newmoney;
        this.hours = newtime;
        this.getSalary();
    }

    private void getSalary() {
        if (this.payment < 70 || this.hours > 60) {
            this.salary = "Ошибка";
        } else {
            int mTime = this.hours - 40;
            int fTime;

            if (mTime < 0) {
                mTime = 0;
            }

            fTime = this.hours - mTime;

            this.salary += (int) (fTime * this.payment + mTime * this.payment * 1.5);
        }
    }

}
