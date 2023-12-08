import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt();
        int cnt=0;
        while(a!=1){
            a/=2;
            cnt++;
        }
        System.out.print(cnt);
    }
}