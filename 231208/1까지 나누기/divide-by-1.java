import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int a=n;
        for(int i=1;i<=a;i++){
            n/=i;
            if(n<=1){
                System.out.print(i);
                break;
            }
        }
    }
}