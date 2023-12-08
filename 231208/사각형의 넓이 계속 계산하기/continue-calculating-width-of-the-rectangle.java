import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        while(true){
            int r=sc.nextInt();
            int c=sc.nextInt();
            char a=sc.next().charAt(0);
            System.out.println(r*c);
            if(a=='C'){
                break;
            }
        }
    }
}