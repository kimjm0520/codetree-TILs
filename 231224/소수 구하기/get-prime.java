import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt(),cnt=0;
        for(int i=2;i<=n;i++){
            cnt=0;
            for(int j=2;j<i;j++){
                if(i%j==0){
                    cnt++;
                }
            }
            if(cnt==0)
            System.out.print(i+" ");
        }
    }
}