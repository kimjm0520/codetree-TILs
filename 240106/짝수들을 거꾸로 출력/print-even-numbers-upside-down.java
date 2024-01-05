import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] num=new int[n];
        int cnt=0;
        for(int i=0;i<n;i++){
            int a=sc.nextInt();
            if(a%2==0){
                num[cnt]=a;
                cnt++;
            }
        }
        for(int i=cnt-1;i>=0;i--){
            System.out.print(num[i]+" ");
        }
    }
}