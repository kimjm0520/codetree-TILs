import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt();
        int b=sc.nextInt();
        int c=sc.nextInt();
        if(a>b){
            a=b;
        }
        else{
            a=a;
        }
        if(b>c){
            b=c;
        }
        else{
            b=b;
        }
        if(a>b){
            System.out.print(b);
        }
        else{
            System.out.print(a);
        }
    }
}