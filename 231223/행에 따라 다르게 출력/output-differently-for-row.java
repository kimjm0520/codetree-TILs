import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt(), cnt=2;
        for(int i=0;i<n;i++){
            if(i%2==0){
                cnt--;
                for(int j=1;j<=n;j++){
                    System.out.print(cnt+" ");
                    cnt++;
                }
            }
            else{
                cnt++;
                for(int j=0;j<n;j++){
                    System.out.print(cnt+" ");
                    cnt+=2;
                }
            }
            System.out.println();
        }
    }
}