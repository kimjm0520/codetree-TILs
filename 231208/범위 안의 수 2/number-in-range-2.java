import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int sum=0, m=0;
        for(int i=1;i<=10;i++){
            int n=sc.nextInt();
            if(n>=0 && n<=200){
                sum+=n;
                m++;
            }
        }
        System.out.print(sum+" ");
        System.out.printf("%.1f",(double)sum/m);
    }
}