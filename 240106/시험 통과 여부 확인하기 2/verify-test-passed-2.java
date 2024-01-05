import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int sum=0,cnt=0;
        for(int i=0;i<n;i++){
            int[] num=new int[4];
            sum=0;
            for(int j=0;j<4;j++){
                num[j]=sc.nextInt();
                sum+=num[j];
            }
            if((double)sum/4 >= 60){
                System.out.println("pass");
                cnt++;
            }
            else{
                System.out.println("fail");
            }
        }
        System.out.print(cnt);
    }
}