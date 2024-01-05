import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        double sum=0;
        double[] num=new double[n];
        for(int i=0;i<n;i++){
            num[i]=sc.nextDouble();
            sum+=num[i];
        }
        if(sum/n >= 4.0){
            System.out.printf("%.1f",sum/n);
            System.out.println();
            System.out.print("Perfect");
        }
        else if(sum/n >= 3.0){
            System.out.printf("%.1f"+"\n",sum/n);
            System.out.print("Good");
        }
        else{
            System.out.printf("%.1f"+"\n",sum/n);
            System.out.print("Poor");
        }
    }
}