import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int[] num=new int[10];
        for(int i=0;i<10;i++){
            num[i]=sc.nextInt();
        }
        int sum=0, n=0;
        for(int i=0;i<10;i++){
            if(num[i]>=250)
            break;
            sum+=num[i];
            n=i+1;
        }
        System.out.print(sum+" ");
        System.out.printf("%.1f",((double)sum/n));
    }
}