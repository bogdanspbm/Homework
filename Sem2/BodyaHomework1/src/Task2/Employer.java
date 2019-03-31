package Task2;

public class Employer {

    String fio, salary = "";
    int payment = 0, hours = 0;

    public Employer(String newfio, int newmoney, int newtime) {
        this.fio = newfio;
        this.payment = newmoney;
        this.hours = newtime;
        this.CalcSalary();
    }

    private void CalcSalary() {
        if (this.payment < 70 || this.hours > 60) {
            this.salary = "Ошибка";
        } else {
            int demosalary = 0;
            int mtime = this.hours - 40;
            int ftime;

            if (mtime < 0) {
                mtime = 0;
            }

            ftime = this.hours - mtime;

            this.salary += (int) (ftime * this.payment + mtime * this.payment * 1.5);
        }
    }

    public void PrintInfo() {
        System.out.println(this.fio + " " + this.payment + " " + this.hours + " " + this.salary);
    }
}
