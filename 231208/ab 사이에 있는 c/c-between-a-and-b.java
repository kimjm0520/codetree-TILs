import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt(), b=sc.nextInt(), c=sc.nextInt(), cnt=0;
        for(int i=a;i<=b;i++){
            if(i%c==0){
                System.out.print("YES");
                cnt++;
                break;
            }
        }
        if(cnt==0){
            System.out.print("NO");
        }
    }
}