import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int cnt=0;
        for(int i=1;i<=5;i++){
            int n=sc.nextInt();
            if(n%3==0){
                cnt++;
            }
        }
        if(cnt==5){
            System.out.print(1);
        }
        else{
            System.out.print(0);
        }
    }
}