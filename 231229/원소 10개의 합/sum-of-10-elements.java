import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int[] num=new int[10];
        int sum=0;
        for(int i=0;i<10;i++){
            num[i]=sc.nextInt();
            sum+=num[i];
        }
        System.out.print(sum);
    }
}