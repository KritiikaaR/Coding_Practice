import java.util.Scanner;
import java.util.Arrays;

class Student implements Comparable <Student> {
    private String lastName;
    private String firstName;
    private int score;

    Student(String lastName, String firstName,int score){
        this.lastName=lastName;
        this.firstName=firstName;
        this.score=score;
    }

    public String toString(){
        return (lastName + ", " + firstName + ": "+ score );
    }

    public int compareTo(Student other) {
        int last = this.lastName.compareToIgnoreCase(other.lastName);
        if (last == 0) {
            return this.firstName.compareToIgnoreCase(other.firstName);
        }
        return last;
    }

}

public class Main{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        
        System.out.println("How many Students? ");
        int num=sc.nextInt();
        sc.nextLine();

        if (num <= 0) {
            System.out.println("Not a valid number.");
            sc.close();
            return; // exit main if invalid
        }
        Student[] students=new Student[num];
        
        for(int i=0;i<num;i++){

            System.out.println("Details for Student "+ (i+1) + ": ");
        
            System.out.println("Last Name: ");
            String lastName=sc.nextLine();

            System.out.println("First Name: ");
            String firstName=sc.nextLine();

            int score;
            while(true){
                System.out.println("Score(0-100): ");
                score=sc.nextInt();
                sc.nextLine();
                if(score>=0 && score<=100){
                    break;
                }
                System.out.println("Invalid score, try againn. ");
            }

            students[i]=new Student(lastName,firstName,score);
        }  

        Arrays.sort(students);

        for (Student s : students) {
            System.out.println(s);
        }

    sc.close();
    }



}


