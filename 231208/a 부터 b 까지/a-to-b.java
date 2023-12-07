import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt();
        int b=sc.nextInt();
        for(int i=a;i<=b;i+=0){
            if(i%2!=0){
                System.out.print(i+" ");
                i*=2;
            }
            else{
                System.out.print(i+" ");
                i+=3;
            }
        }
    }
}