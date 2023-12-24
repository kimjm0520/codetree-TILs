import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt(), b=sc.nextInt(), cnt=0,t=0;
        for(int i=a;i<=b;i++){
            cnt=0;
            for(int j=1;j<=i;j++){
                if(i%j==0);
                cnt++;
            }
            if(cnt<4)
            t++;
        }
        System.out.print(t);
    }
}