import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt();
        int b=sc.nextInt();
        int c=sc.nextInt();
        if(a>=b){
            a=a;
        }
        else{
            a=b;
        }
        if(b>=c){
            b=b;
        }
        else{
            b=c;
        }
        if(a>=b){
            System.out.print(b);
        }
        else{
            System.out.print(a);
        }
    }
}