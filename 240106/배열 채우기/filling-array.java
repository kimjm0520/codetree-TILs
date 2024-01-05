import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int[] num=new int[10];
        int n,cnt=0;
        for(int i=0;i<10;i++){
            n=sc.nextInt();
            if(n==0)
            break;
            num[i]=n;
            cnt=i;
        }
        for(int i=cnt;i>=0;i--){
            System.out.print(num[i]+" ");
        }
    }
}