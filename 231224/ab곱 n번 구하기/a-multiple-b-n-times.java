import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt(), a, b, sum;
        for(int i=0;i<n;i++){
            sum=1;
            a=sc.nextInt(); 
            b=sc.nextInt();
            for(int j=a;j<=b;j++){
                sum*=j;
            }
            System.out.println(sum);
        }
    }
}